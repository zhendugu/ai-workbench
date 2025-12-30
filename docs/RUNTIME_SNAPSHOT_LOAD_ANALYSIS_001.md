# Run-Time Frontend Snapshot Load Analysis 001

**Date**: 2025-12-29

**Purpose**: 定位 Run-Time Frontend 在启动时"实际加载的 snapshot 来源"，确认其是否为一个真实、存在、合法的 Frozen Snapshot JSON 文件。

---

## T1: 明确 Run-Time Frontend 的 Snapshot 加载入口

### 加载入口代码位置

**文件**: `run_time_frontend/src/App.tsx`

**加载逻辑** (Lines 25-51):
```typescript
useEffect(() => {
  // Extract frozenId from URL (e.g., /frozen/FROZEN-COMP-123)
  const pathParts = window.location.pathname.split('/')
  const idFromUrl = pathParts[pathParts.length - 1] || pathParts[pathParts.length - 2]
  
  const frozenId = (idFromUrl && idFromUrl !== 'frozen' && idFromUrl !== '') 
    ? idFromUrl 
    : 'FROZEN-COMP-DEFAULT' // Default for development

  loadSnapshotById(frozenId)
    .then((result) => { ... })
})
```

### 加载函数位置

**文件**: `run_time_frontend/src/services/authorityLoader.ts`

**函数**: `loadSnapshotById(frozenCompanyIdentifier: string, baseUrl: string = '/snapshots/authority')`

**实现** (Lines 153-157):
```typescript
export async function loadSnapshotById(
  frozenCompanyIdentifier: string,
  baseUrl: string = '/snapshots/authority'
): Promise<LoadSnapshotResult> {
  const snapshotDir = `${baseUrl}/${frozenCompanyIdentifier}`;
  return loadFrozenSnapshot(snapshotDir);
}
```

### 当前默认 Snapshot 路径

**默认 frozenId**: `'FROZEN-COMP-DEFAULT'` (当 URL 中没有指定时)

**完整路径结构**:
- Base URL: `/snapshots/authority` (served from `public/` directory)
- Snapshot directory: `/snapshots/authority/FROZEN-COMP-DEFAULT/`
- 实际文件系统路径: `run_time_frontend/public/snapshots/authority/FROZEN-COMP-DEFAULT/`

**需要的 6 个 JSON 文件**:
1. `/snapshots/authority/FROZEN-COMP-DEFAULT/company.json`
2. `/snapshots/authority/FROZEN-COMP-DEFAULT/cells.json`
3. `/snapshots/authority/FROZEN-COMP-DEFAULT/roles.json`
4. `/snapshots/authority/FROZEN-COMP-DEFAULT/topology.json`
5. `/snapshots/authority/FROZEN-COMP-DEFAULT/methodology.json`
6. `/snapshots/authority/FROZEN-COMP-DEFAULT/freeze_record.json`

### 加载机制

- **方法**: `fetch()` API (浏览器原生)
- **来源**: `public/` 目录 (Vite 静态资源)
- **类型**: 本地静态文件，不是 API 调用
- **不是**: Backend 服务、数据库、外部 API

---

## T2: 验证该路径在 dev 模式下"实际返回了什么"

### 文件系统验证

**检查结果**: ✅ 所有文件存在

**文件列表**:
```
run_time_frontend/public/snapshots/authority/FROZEN-COMP-DEFAULT/
├── company.json          ✅ 存在
├── cells.json            ✅ 存在
├── roles.json            ✅ 存在
├── topology.json         ✅ 存在
├── methodology.json      ✅ 存在
└── freeze_record.json    ✅ 存在
```

**文件内容验证**:

#### company.json
```json
{
  "company_identifier": "FROZEN-COMP-DEFAULT",
  "company_name": "Test Company",
  "company_description": "Minimal valid test fixture for Run-Time Frontend UI testing",
  "frozen_at": "2025-12-29T10:00:00Z",
  "frozen_by": "Test User"
}
```
✅ **格式**: 有效 JSON
✅ **字段**: 符合 Company schema (5 个字段)

#### cells.json
```json
[
  {
    "cell_identifier": "CELL-00000000-0000-0000-0000-000000000001",
    "cell_name": "Test Cell",
    "responsibility_what": "Test responsibility declaration",
    "responsibility_what_not": "Test boundary declaration",
    "role_constraints": []
  }
]
```
✅ **格式**: 有效 JSON 数组
✅ **字段**: 符合 Cell schema (5 个字段)

#### freeze_record.json
```json
{
  "freeze_record_identifier": "FREEZE-00000000-0000-0000-0000-000000000001",
  "frozen_company_identifier": "FROZEN-COMP-DEFAULT",
  "frozen_at": "2025-12-29T10:00:00Z",
  "frozen_by": "Test User",
  "freeze_summary": "Test fixture for Run-Time Frontend UI testing"
}
```
✅ **格式**: 有效 JSON
✅ **字段**: 符合 FreezeRecord schema

### 浏览器 Fetch 验证

**预期行为**:
- 在 dev 模式下 (`npm run dev`)，Vite 会将 `public/` 目录的内容作为静态资源提供
- 访问 `/snapshots/authority/FROZEN-COMP-DEFAULT/company.json` 应该返回 JSON 内容
- **不应该**返回 HTML (Vite 的 index.html fallback)

**HTML Fallback 检测**:
代码中已实现 HTML 检测 (authorityLoader.ts Lines 68-72):
```typescript
// Check for HTML fallback (Vite dev server returns index.html for missing files)
if (text.trim().startsWith('<!') || text.trim().startsWith('<html')) {
  return {
    error: 'Snapshot file not found (HTML fallback returned). Ensure JSON files exist in public/snapshots/authority/{frozenId}/',
  };
}
```

### Validation 失败原因分析

**如果 validation 失败，可能的原因**:

1. **文件不存在** → 返回 HTML fallback → 被检测并拒绝
2. **文件格式错误** → JSON 解析失败 → 返回解析错误
3. **Schema 不匹配** → `validateFrozenSnapshot()` 返回 `valid: false` → 返回验证错误
4. **字段缺失** → Authority validator 拒绝 → 返回验证错误

**当前状态**: 文件存在且格式正确，应该能通过基本 JSON 解析。

---

## T3: 对齐 Run-Time 模式的最小可运行假设

### 当前假设

**Run-Time Frontend 的假设**:
- ✅ **假设**: "必然存在一个 frozen snapshot" (通过默认值 `FROZEN-COMP-DEFAULT`)
- ✅ **实际**: 仓库中**已提供**测试 fixture (`FROZEN-COMP-DEFAULT/`)
- ✅ **状态**: 这是**有效输入**，不是缺失输入

### 最小可运行条件

**Run-Time Frontend 需要**:
1. ✅ 至少一个有效的 Frozen Snapshot (已提供: `FROZEN-COMP-DEFAULT`)
2. ✅ 所有 6 个 JSON 文件存在 (已提供)
3. ✅ 所有文件符合 Authority schemas (需要验证)
4. ✅ `validateFrozenSnapshot()` 通过 (需要运行时验证)

### 缺失输入 vs 校验失败

**当前情况**: **不是缺失输入**

- 文件已存在
- 格式正确 (JSON)
- 字段完整 (符合 schema)

**如果 validation 失败，原因可能是**:
- Schema 验证失败 (字段值不符合规则，如 identifier 格式)
- 类型验证失败 (如 timestamp 格式)
- 关系验证失败 (如 Role attachment)

**这不是"缺失输入"，而是"校验失败"**。

---

## 事实说明：Validation 为什么可能失败

### 可能的原因（按优先级）

#### 1. Identifier 格式验证
Authority validator 检查 identifier 格式：
- `company_identifier` 必须匹配 `FROZEN-COMP-{UUID}` 格式
- `cell_identifier` 必须匹配 `CELL-{UUID}` 格式
- `freeze_record_identifier` 必须匹配 `FREEZE-{UUID}` 格式

**当前 fixture 状态**:
- ✅ `company_identifier`: `"FROZEN-COMP-DEFAULT"` - 格式可能不符合 UUID 要求
- ⚠️ `cell_identifier`: `"CELL-00000000-0000-0000-0000-000000000001"` - 格式正确
- ✅ `freeze_record_identifier`: `"FREEZE-00000000-0000-0000-0000-000000000001"` - 格式正确

**确认问题**: `FROZEN-COMP-DEFAULT` **不满足** UUID 格式要求。

**Validator 要求** (validate.ts Lines 88-96):
```typescript
const uuidPart = value.substring(prefix.length + 1);
if (uuidPart.length < 30 || !uuidPart.includes('-')) {
  errors.push({
    field: path,
    message: `Identifier format invalid: expected "${prefix}-{UUID}"`,
  });
}
```

**分析**:
- `FROZEN-COMP-DEFAULT` 的 UUID 部分是 `"DEFAULT"`
- 长度: 7 个字符 (要求: ≥30 个字符)
- 包含 "-": 否 (要求: 必须包含 "-")
- **结论**: **会验证失败**

#### 2. Timestamp 格式验证
Authority validator 检查 `frozen_at` 格式：
- 必须是 ISO 8601 格式: `YYYY-MM-DDTHH:MM:SSZ`

**当前 fixture 状态**:
- ✅ `frozen_at`: `"2025-12-29T10:00:00Z"` - 格式正确

#### 3. 关系完整性验证
Authority validator 可能检查：
- 所有 Role 必须 attached 到存在的 Cell
- Topology relationships 必须引用存在的 Cell

**当前 fixture 状态**:
- ✅ `roles.json`: 空数组 `[]` - 无关系需要验证
- ✅ `topology.json`: 空数组 `[]` - 无关系需要验证

---

## 最小修正方案选项（不实施）

### 选项 1: 修复 Identifier 格式

**问题**: `FROZEN-COMP-DEFAULT` 可能不符合 UUID 格式要求

**修正**: 使用符合 UUID 格式的 identifier
```json
{
  "company_identifier": "FROZEN-COMP-00000000-0000-0000-0000-000000000001",
  ...
}
```

### 选项 2: 明确空态 UI 行为

**当前行为**: 如果 snapshot 不存在或无效，显示 "Invalid Snapshot" 页面

**建议行为**:
- 如果文件不存在 → 显示 "No Snapshot Available" (不是 validation 错误)
- 如果 validation 失败 → 显示 "Invalid Snapshot" (当前行为)

**实现**: 区分 `loadFrozenSnapshot()` 的错误类型：
- `file not found` → 空态 UI
- `validation failed` → Invalid Snapshot UI

### 选项 3: 提供多个测试 Fixture

**当前**: 只有一个 `FROZEN-COMP-DEFAULT`

**建议**: 提供多个测试 fixture：
- `FROZEN-COMP-MINIMAL` - 最小有效 snapshot
- `FROZEN-COMP-FULL` - 完整 snapshot (多个 cells, roles, relationships)
- `FROZEN-COMP-INVALID` - 故意无效的 snapshot (用于测试错误处理)

---

## 总结

### 当前状态

✅ **Snapshot 来源**: 明确
- 路径: `/snapshots/authority/FROZEN-COMP-DEFAULT/`
- 来源: `public/` 静态文件
- 文件: 6 个 JSON 文件全部存在

✅ **文件格式**: 有效 JSON
- 所有文件都是有效的 JSON
- 字段结构符合 Authority schemas

❌ **确认问题**: Identifier 格式验证**会失败**
- `FROZEN-COMP-DEFAULT` 不符合 UUID 格式要求
- UUID 部分 `"DEFAULT"` 只有 7 个字符，要求 ≥30 个字符
- UUID 部分不包含 "-"，要求必须包含 "-"

### Validation 失败的直接原因

**不是**: 缺失输入（文件已存在）

**是**: **Identifier 格式验证失败**
- `company_identifier: "FROZEN-COMP-DEFAULT"` 不符合 `FROZEN-COMP-{UUID}` 格式
- Validator 会返回错误: `"Identifier format invalid: expected "FROZEN-COMP-{UUID}""`

### 建议

1. **运行时验证**: 启动 dev server 并检查实际 validation 结果
2. **修复 identifier**: 如果格式验证失败，使用符合 UUID 格式的 identifier
3. **明确错误类型**: 区分"文件不存在"和"validation 失败"两种错误

---

**END OF ANALYSIS**

