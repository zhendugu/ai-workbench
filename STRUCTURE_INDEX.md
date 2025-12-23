# 代码骨架结构索引

本文档列出所有已创建的代码骨架,并标注其对应的文档来源。

**Stage 2 - Implementation Preparation**
- 仅包含类型定义和占位结构
- 无业务逻辑
- 无工作流推断
- 无状态转换

---

## 前端结构 (基于 S1_frontend_definition.md)

### 类型定义
- `frontend/src/types/s1_types.ts` - S1 核心对象类型
  - User (用户) - S1 一.1
  - Dashboard (仪表总览) - S1 一.2
  - Collection (对象列表) - S1 一.3
  - Detail (单一对象详情) - S1 一.4
  - ActionEntry (操作入口) - S1 一.5
  - Feedback (状态反馈) - S1 一.6

### 页面组件
- `frontend/src/pages/DashboardPage.tsx` - 总览页 (S1 四.1)
- `frontend/src/pages/CollectionPage.tsx` - 列表页 (S1 四.2)
- `frontend/src/pages/DetailPage.tsx` - 详情页 (S1 四.3)

### 组件
- `frontend/src/components/FeedbackLayer.tsx` - 反馈层 (S1 四.4)
- `frontend/src/components/UserIndicator.tsx` - 用户身份指示 (S1 二.Level 0)
- `frontend/src/components/GlobalNavigation.tsx` - 全局导航 (S1 二.Level 0)
- `frontend/src/components/ActionEntry.tsx` - 操作入口 (S1 一.5)

### 应用入口
- `frontend/src/App.tsx` - 主应用组件

---

## 后端结构

### S2 核心概念 (基于 S2_backend_definition.md)

#### 类型定义
- `backend/src/types/s2_types.ts` - S2 核心概念类型
  - Agent (主体) - S2 二.1
  - Goal (目标) - S2 二.2
  - ActionRecord (行为记录) - S2 二.3
  - State (状态) - S2 二.4
  - Rule (规则) - S2 二.5

- `backend/src/types/state_types.ts` - 状态类型枚举
  - ExistentialState (存在状态) - S2 三.1
  - ProgressState (进程状态) - S2 三.2
  - JudgementState (裁决状态) - S2 三.3

### GCD 组织结构 (基于 GCD.md)

#### 类型定义
- `backend/src/types/gcd_types.ts` - GCD 组织结构类型
  - Role (角色) - GCD 3.1
  - Cell (细胞/执行单元) - GCD 3.2
  - CatalystHub (轻量中枢) - GCD 3.3
  - TaskForce (临时工作小组) - GCD 3.4

#### 基础设施类型
- `backend/src/infrastructure/handoff_protocol.ts` - AI 协作交接协议 (GCD 8.1)
- `backend/src/infrastructure/memory.ts` - Memory (运行时与历史上下文) (GCD 8.2)
- `backend/src/infrastructure/document_center.ts` - Document Center (组织规范与模板) (GCD 8.2)
- `backend/src/infrastructure/knowledge_base.ts` - Knowledge Base (可复用推理与方法论) (GCD 8.2)

#### 治理类型
- `backend/src/types/governance_types.ts` - 治理与变更控制 (GCD 10)
  - ChangeTarget (变更对象) - GCD 10.2
  - ChangeProcess (变更流程) - GCD 10.3

#### 安全类型
- `backend/src/types/safety_types.ts` - 运行安全与异常处理 (GCD 11)
  - HubHealthCheck (Catalyst Hub 健康检查) - GCD 11.1
  - CircuitBreaker (断路器与超时) - GCD 11.2
  - IncompleteTaskOutput (任务不可完成时的标准输出) - GCD 11.3
  - Escalation (人类介入与升级路径) - GCD 11.4

#### 可观测性类型
- `backend/src/types/observability_types.ts` - 可观测性与质量保证 (GCD 12)
  - ObservabilityRecord (最小可观测性) - GCD 12.1
  - Metrics (关键指标) - GCD 12.2
  - RegressionTest (回归测试) - GCD 12.3

#### 角色边界类型
- `backend/src/types/role_boundary_types.ts` - 角色边界的"技术执行机制" (GCD 13)
  - SingleOwner (唯一主责角色) - GCD 13.1
  - RolePermissions (角色权限与工具白名单) - GCD 13.2
  - HandoffProtocolValidation (交接协议的"格式校验") - GCD 13.3

#### 知识管理类型
- `backend/src/types/knowledge_types.ts` - 知识一致性与生命周期管理 (GCD 14)
  - SSOT (单一事实来源) - GCD 14.1
  - KnowledgeVersioning (版本、过期与废弃) - GCD 14.2
  - ConflictResolution (冲突处理) - GCD 14.3

#### AI 相关类型
- `backend/src/ai/ai_gateway.ts` - AI Gateway/Service 层 (constraints + GCD 15.3)
- `backend/src/types/ai_types.ts` - AI API 使用与工程自律规范 (GCD 15-16)
  - AICallRecord (调用责任边界) - GCD 15.3
  - PromptContext (Prompt 与上下文管理) - GCD 15.4
  - ResourceGovernance (成本与资源治理) - GCD 15.5
  - TokenGovernance (Token 节约与上下文控制) - GCD 16 + constraints

---

## 说明

- 所有文件均为代码骨架,仅包含类型定义和占位结构
- 所有实现必须能回溯到对应的文档章节
- 不得新增功能,不得推导业务逻辑,不得解释语义
- 当前阶段: Stage 2 - Implementation Preparation (stage_status.md)
- 符合 EXECUTION_CONTRACT.md 和 WORKFLOW_RULES.md 要求
