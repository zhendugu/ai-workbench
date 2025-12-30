# ENGINE Layer Overlap Audit Report

**审计类型**: READ-ONLY  
**审计目标**: 识别 ENGINE/template 层与 Blueprint 层可能重叠的约定，避免重复定义、冲突或 SSOT 分裂  
**审计时间**: 2025-12-23  
**Blueprint**: ai-virtual-company-org

---

## A. 已存在的约定类型

### A.1 子系统之间的职责边界或交互约定

**已存在**：

1. **ENGINE_HANDOFF_PROMPT.md**
   - Section: "Decision Authority Hierarchy"
   - 定义了文档优先级顺序（Human instruction > CURRENT_STATE_SNAPSHOT > Engine docs > Registry > Code）
   - 定义了 Cursor Pro 的 Pre-Action Requirements

2. **ENGINE_V1_FREEZE.md**
   - Section: "Governance Priority Order"
   - 定义了治理文档的优先级顺序（与 ENGINE_HANDOFF_PROMPT.md 一致）

3. **BLUEPRINT_INTERFACE.md**
   - Section: "Relationship to Stage"
   - Section: "Relationship to Registry"
   - Section: "Relationship to Human Approval"
   - 定义了 Blueprint 与 ENGINE 层的交互边界

4. **EXECUTION_CONTRACT.md**
   - Section: "Source of Authority (Priority Order)"
   - 定义了执行时的权威来源顺序

**不存在**：
- 系统内部子系统（如 Role、Cell、Catalyst Hub）之间的职责边界约定
- 子系统之间的交互协议约定（除 Handoff Protocol 外）

---

### A.2 系统级不变量（必须始终成立的规则）

**已存在**：

1. **ENGINE_V1_FREEZE.md**
   - Section: "AI / Cursor Behavior Invariants"
     - Default Mode（分析/准备模式）
     - Authorization Model（显式批准要求）
     - Failure Mode（停止并询问）
     - Startup Protocol（强制阅读顺序）
   - Section: "Frozen Core Scope"
     - ENGINE Identity Rules
     - Governance Priority Order
     - AI/Cursor Behavior Rules
     - CI Enforcement Architecture
     - Stage Progression Rules
     - Blueprint Interface

2. **ENGINE_HANDOFF_PROMPT.md**
   - Section: "Explicit Permission Rule"
     - "Lack of instruction is NOT permission"
     - "Absence of prohibition is NOT authorization"
     - "Silence is NOT approval"

3. **ENGINE_CI_BOOTSTRAP.md**
   - Section: "Anti-Tamper Rules"
   - Section: "Stage/Registry Alignment Rules"

4. **EXECUTION_CONTRACT.md**
   - Section: "Contract Finality"（合同不可修改）

**不存在**：
- 业务逻辑层面的系统不变量（如"Role 任务永远绑定在 Role 上，而不是 AI 上"）
- 组织结构的系统不变量（如"Cell 必须端到端负责"）

---

### A.3 明确的失败模式或兜底行为

**已存在**：

1. **ENGINE_HANDOFF_PROMPT.md**
   - Section: "Stop Conditions"
     - Ambiguity detected
     - Authorization unclear
     - Identity unclear
     - Constraint violation risk
     - Missing required file
   - Section: "Failure Mode"
     - 遇到不一致状态时的处理方式
   - Section: "Ambiguity Handling"
     - STOP all action
     - Identify the ambiguity
     - Ask the human
     - Do NOT guess

2. **HUMAN_ESCALATION.md**
   - Section: "Mandatory Escalation Conditions"
   - Section: "Forbidden Self-Resolution"
   - Section: "Escalation Format"

3. **ENGINE_V1_FREEZE.md**
   - Section: "AI / Cursor Behavior Invariants" > "Failure Mode"
     - "When uncertain: STOP, ASK the human, DO NOT guess"

4. **EXECUTION_CONTRACT.md**
   - Section: "Escalation Clause"

**不存在**：
- 业务执行层面的失败模式（如"任务不可完成时的标准输出"）
- 系统运行层面的兜底行为（如"Hub 不可用时的降级模式"）

---

### A.4 Human Escalation / Stop Conditions

**已存在**：

1. **HUMAN_ESCALATION.md**（完整文档）
   - Section: "Mandatory Escalation Conditions"
   - Section: "Forbidden Self-Resolution"
   - Section: "Escalation Format"
   - Section: "Human Role"
   - Section: "Post-Escalation"

2. **ENGINE_HANDOFF_PROMPT.md**
   - Section: "Stop Conditions"（详细列表）
   - Section: "Ambiguity Handling"
   - Section: "Failure Mode"

3. **EXECUTION_CONTRACT.md**
   - Section: "Escalation Clause"

4. **ENGINE_V1_FREEZE.md**
   - Section: "AI / Cursor Behavior Invariants" > "Failure Mode"

**不存在**：
- 业务层面的升级条件（如"高风险操作必须升级到人类"）
- 领域特定的停止条件（如"知识冲突未裁决时进入保守模式"）

---

### A.5 AI 或 Agent 的禁止行为清单

**已存在**：

1. **ENGINE_HANDOFF_PROMPT.md**
   - Section: "Default Forbidden Actions (Without Human Approval)"
     - Implement new endpoints
     - Uncomment frozen code
     - Add business logic
     - Introduce persistence or databases
     - Call external APIs
     - Modify execution behavior
     - Weaken CI or governance rules
     - Assume missing context
     - Infer intent from code
     - Activate a BLUEPRINT
     - Modify registry without approval
     - Advance STAGE without approval

2. **ENGINE_V1_FREEZE.md**
   - Section: "AI / Cursor Behavior Invariants" > "Default Mode"
     - "AI is NOT allowed to implement features, modify executable behavior, add endpoints, unfreeze frozen code, introduce side effects, change runtime behavior"

3. **EXECUTION_CONTRACT.md**
   - Section: "Forbidden Actions (Zero Tolerance)"
     - Introduce new concepts, entities, or abstractions
     - Infer or implement business logic
     - Define workflows, execution order, or system behavior
     - Add validation rules, conditions, or state transitions
     - Optimize, refactor, or "improve" structure
     - Merge or reinterpret S1 / S2 definitions
     - Generate explanatory text, suggestions, or alternatives
     - Act as a designer, architect, or decision-maker

4. **constraints.md**（Token 节约相关）
   - 禁止为每个角色创建独立 AI 实体
   - 禁止在 system prompt 中重复描述角色背景
   - 禁止在每轮请求中携带完整历史对话
   - 禁止模型自由发挥或跨角色补充内容

**不存在**：
- 业务逻辑层面的禁止行为（如"禁止 Catalyst Hub 参与执行"）
- 组织结构层面的禁止行为（如"禁止固定部门长期存在"）

---

## B. 约定层级归属

### B.1 子系统之间的职责边界或交互约定

**ENGINE 层（Blueprint 不得重复）**：
- 文档优先级顺序（Human > CURRENT_STATE_SNAPSHOT > Engine docs > Registry > Code）
- Blueprint 与 ENGINE 层的交互边界（BLUEPRINT_INTERFACE.md 已定义）
- Cursor Pro 的 Pre-Action Requirements

**Blueprint 层可细化**：
- 系统内部子系统（Role、Cell、Catalyst Hub、Task Force）之间的职责边界
- 子系统之间的交互协议（除 ENGINE 层已定义的 Handoff Protocol 外）

**已足够，不应再写**：
- Blueprint 与 ENGINE 层的交互规则（BLUEPRINT_INTERFACE.md 已完整定义）

---

### B.2 系统级不变量

**ENGINE 层（Blueprint 不得重复）**：
- AI/Cursor 行为不变量（Default Mode、Authorization Model、Failure Mode、Startup Protocol）
- 治理优先级顺序
- ENGINE Identity Rules
- CI Enforcement Architecture
- Stage Progression Rules
- Blueprint Interface 规则

**Blueprint 层可细化**：
- 业务逻辑层面的系统不变量（如"Role 任务永远绑定在 Role 上"）
- 组织结构层面的系统不变量（如"Cell 必须端到端负责"）
- 领域特定的不变量（如"Task Force 必须明确解散条件"）

**已足够，不应再写**：
- ENGINE 层的核心不变量（ENGINE_V1_FREEZE.md 已完整定义）

---

### B.3 明确的失败模式或兜底行为

**ENGINE 层（Blueprint 不得重复）**：
- Cursor Pro 的停止条件（Ambiguity、Authorization unclear、Identity unclear 等）
- Cursor Pro 的失败模式（Treat CURRENT_STATE_SNAPSHOT as authoritative、Request clarification）
- Cursor Pro 的歧义处理（STOP、Identify、Ask、Do NOT guess）

**Blueprint 层可细化**：
- 业务执行层面的失败模式（如"任务不可完成时的标准输出格式"）
- 系统运行层面的兜底行为（如"Hub 不可用时的降级模式"）
- 领域特定的失败处理（如"知识冲突时的保守模式"）

**已足够，不应再写**：
- Cursor Pro 层面的失败模式（ENGINE_HANDOFF_PROMPT.md、HUMAN_ESCALATION.md 已完整定义）

---

### B.4 Human Escalation / Stop Conditions

**ENGINE 层（Blueprint 不得重复）**：
- Cursor Pro 的强制升级条件（HUMAN_ESCALATION.md 已完整定义）
- Cursor Pro 的停止条件（ENGINE_HANDOFF_PROMPT.md 已完整定义）
- 升级格式要求（Exact blocking issue、Referenced document sections、What action is blocked、No proposed solutions）

**Blueprint 层可细化**：
- 业务层面的升级条件（如"高风险操作必须升级到人类"）
- 领域特定的停止条件（如"知识冲突未裁决时进入保守模式"）
- 业务执行层面的升级路径（如"多次失败仍无可验证输出时升级"）

**已足够，不应再写**：
- Cursor Pro 层面的升级协议（HUMAN_ESCALATION.md 已完整定义）

---

### B.5 AI 或 Agent 的禁止行为清单

**ENGINE 层（Blueprint 不得重复）**：
- Cursor Pro 的禁止行为（ENGINE_HANDOFF_PROMPT.md、EXECUTION_CONTRACT.md 已完整定义）
- Token 节约相关的禁止行为（constraints.md 已定义）
- ENGINE 治理相关的禁止行为（ENGINE_V1_FREEZE.md 已定义）

**Blueprint 层可细化**：
- 业务逻辑层面的禁止行为（如"禁止 Catalyst Hub 参与执行"）
- 组织结构层面的禁止行为（如"禁止固定部门长期存在"）
- 领域特定的禁止行为（如"禁止角色与 AI 实例强绑定"）

**已足够，不应再写**：
- Cursor Pro 层面的禁止行为（ENGINE_HANDOFF_PROMPT.md、EXECUTION_CONTRACT.md 已完整定义）
- Token 节约相关的禁止行为（constraints.md 已完整定义）

---

## C. 冲突与歧义风险

### C.1 如果在 Blueprint 中再次定义会造成冲突或歧义的内容

**高风险冲突**：

1. **文档优先级顺序**
   - ENGINE 层已定义：Human > CURRENT_STATE_SNAPSHOT > Engine docs > Registry > Code
   - 如果 Blueprint 重新定义优先级顺序，会造成 SSOT 分裂
   - **Blueprint 只能引用，不能重新表述**

2. **Cursor Pro 的停止条件**
   - ENGINE_HANDOFF_PROMPT.md Section "Stop Conditions" 已完整定义
   - HUMAN_ESCALATION.md Section "Mandatory Escalation Conditions" 已完整定义
   - 如果 Blueprint 重新定义停止条件，会造成歧义（哪些条件适用于 Cursor Pro，哪些适用于业务执行）
   - **Blueprint 只能引用，不能重新表述**

3. **Cursor Pro 的禁止行为**
   - ENGINE_HANDOFF_PROMPT.md Section "Default Forbidden Actions" 已完整定义
   - EXECUTION_CONTRACT.md Section "Forbidden Actions" 已完整定义
   - 如果 Blueprint 重新定义禁止行为，会造成歧义（哪些禁止行为适用于 Cursor Pro，哪些适用于业务执行）
   - **Blueprint 只能引用，不能重新表述**

4. **AI/Cursor 行为不变量**
   - ENGINE_V1_FREEZE.md Section "AI / Cursor Behavior Invariants" 已完整定义
   - 如果 Blueprint 重新定义行为不变量，会造成冲突
   - **Blueprint 只能引用，不能重新表述**

5. **Blueprint 与 ENGINE 层的交互规则**
   - BLUEPRINT_INTERFACE.md 已完整定义 Blueprint 与 Stage、Registry、Human Approval 的关系
   - 如果 Blueprint 重新定义交互规则，会造成冲突
   - **Blueprint 只能引用，不能重新表述**

**中等风险冲突**：

6. **Token 节约相关规则**
   - constraints.md 已定义 Token 节约规则
   - 如果 Blueprint 重新定义 Token 节约规则，可能造成冲突（除非明确说明是业务层面的补充）
   - **Blueprint 应引用 ENGINE 层规则，然后细化业务层面的补充规则**

7. **失败模式处理方式**
   - ENGINE_HANDOFF_PROMPT.md Section "Failure Mode" 已定义 Cursor Pro 的失败模式
   - 如果 Blueprint 使用相同术语但定义不同含义，会造成歧义
   - **Blueprint 应使用不同术语（如"业务失败模式"）或明确说明是业务层面的扩展**

---

### C.2 Blueprint 只能"引用"，不能"重新表述"的内容

**必须引用的内容**：

1. **ENGINE_HANDOFF_PROMPT.md**
   - Decision Authority Hierarchy
   - Stop Conditions
   - Default Forbidden Actions
   - Failure Mode
   - Ambiguity Handling
   - Explicit Permission Rule

2. **ENGINE_V1_FREEZE.md**
   - AI / Cursor Behavior Invariants
   - Governance Priority Order
   - Frozen Core Scope

3. **HUMAN_ESCALATION.md**
   - Mandatory Escalation Conditions
   - Escalation Format
   - Forbidden Self-Resolution

4. **BLUEPRINT_INTERFACE.md**
   - Relationship to Stage
   - Relationship to Registry
   - Relationship to Human Approval

5. **constraints.md**
   - Token 节约核心原则（如果 Blueprint 涉及 AI 调用）

6. **EXECUTION_CONTRACT.md**
   - Source of Authority
   - Forbidden Actions

**引用方式建议**：
- 使用明确的引用格式，如："遵循 ENGINE_HANDOFF_PROMPT.md 中定义的 Stop Conditions"
- 明确区分 ENGINE 层规则与 Blueprint 层规则
- 使用不同的术语避免歧义（如 ENGINE 层用"Stop Conditions"，Blueprint 层用"业务停止条件"）

---

## 总结

### 可安全定义的内容（Blueprint 层）

1. **系统内部子系统的职责边界**
   - Role、Cell、Catalyst Hub、Task Force 之间的职责边界
   - 子系统之间的交互协议（除 ENGINE 层已定义的 Handoff Protocol 外）

2. **业务逻辑层面的系统不变量**
   - 组织结构不变量（如"Cell 必须端到端负责"）
   - 业务执行不变量（如"Role 任务永远绑定在 Role 上"）

3. **业务执行层面的失败模式**
   - 任务不可完成时的标准输出格式
   - 系统运行层面的兜底行为（如 Hub 降级模式）

4. **业务层面的升级条件**
   - 高风险操作的升级路径
   - 领域特定的停止条件

5. **业务逻辑层面的禁止行为**
   - 组织结构禁止行为（如"禁止固定部门长期存在"）
   - 业务执行禁止行为（如"禁止 Catalyst Hub 参与执行"）

### 必须引用的内容（ENGINE 层）

1. 文档优先级顺序
2. Cursor Pro 的停止条件
3. Cursor Pro 的禁止行为
4. AI/Cursor 行为不变量
5. Blueprint 与 ENGINE 层的交互规则
6. 失败模式处理方式（Cursor Pro 层面）
7. Token 节约核心原则（如果涉及）

### 风险提示

- **术语歧义风险**：Blueprint 应使用不同术语或明确说明是业务层面的扩展，避免与 ENGINE 层术语混淆
- **SSOT 分裂风险**：Blueprint 不得重新定义 ENGINE 层已定义的规则，只能引用
- **层级混淆风险**：Blueprint 应明确区分 ENGINE 层规则与 Blueprint 层规则

---

END OF AUDIT REPORT

