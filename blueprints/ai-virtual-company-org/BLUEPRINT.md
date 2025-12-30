# BLUEPRINT: AI Virtual Company Organizational Structure

## Section 0. BLUEPRINT META

- **blueprint_id**: `ai-virtual-company-org`
- **blueprint_version**: 1.0
- **target_engine_version**: v1
- **status**: approved
- **created_by**: cursor
- **created_at**: 2025-12-23
- **description**: 定义一套适用于 AI 驱动虚拟公司的通用组织结构系统，以角色为接口、细胞为执行体、中枢为安全机制、任务小组为进化手段，实现可自组织、可演化、但不失控的执行系统。

---

## Section 1. PROJECT INTENT

### 1.1 Problem Statement

**问题**：
- 需要为 AI 驱动的虚拟公司建立稳定、可扩展的执行结构
- 需要支持多类型业务（产品/顾问/研发）
- 需要支持动态方法论与工作流插拔
- 需要避免组织复杂度随规模指数级上升
- 需要实现全流程可审计、可控、可纠偏

**目标用户**：
- 需要构建 AI 虚拟公司的组织者
- 需要管理 AI 协作系统的运营者
- 需要实现可扩展 AI 执行架构的架构师

### 1.2 Success Definition

**成功标准**（可观察结果）：
- 系统能够接收需求并完成端到端交付（成功或标准化的"不可完成"输出）
- 组织结构能够动态编组而不失控
- 所有执行过程可审计、可回放
- 系统能够积累知识而不结构性崩坏
- 变更控制机制能够防止组织僵化或失控
- 异常情况能够被检测并升级到人类

**成功不依赖于**：
- 特定技术栈的实现
- 固定数量的 AI 实例
- 特定的业务领域

### 1.3 Non-Goals

**本项目不会尝试**：
- 照抄人类公司的部门制与层级制结构
- 模拟"公司"的组织形式
- 建立固定的管理层级
- 为特定业务领域提供现成解决方案
- 定义具体的编程实现方式
- 指定特定的 AI 模型或 API 提供商

---

## Section 2. SCOPE AND BOUNDARIES

### 2.1 In Scope

**明确允许的能力**：
- **角色（Role）系统**：定义 AI 行为的最小约束单位，包含 Purpose、Inputs、Outputs、Boundaries、Task Log
- **细胞（Cell/Pod）系统**：最小可独立交付执行单元，跨职能、端到端负责
- **轻量中枢（Catalyst Hub）**：工作流稳定器与纠偏系统，负责需求分流、状态监控、异常检测、触发临时工作小组
- **临时工作小组（Task Force）**：为特定目标临时组建的一次性执行结构
- **基础设施层**：
  - AI 协作交接协议（Handoff Protocol）
  - 记忆/文档中心/知识库（Memory/Document Center/Knowledge Base）
- **治理与变更控制**：对 Role 规范、Cell 组成、协议、知识库的变更进行审议与版本管理
- **运行安全与异常处理**：健康检查、断路器、超时、失败预算、人类升级路径
- **可观测性**：任务日志、执行轨迹、关键指标追踪
- **AI 资源治理**：AI 调用规范、Token 节约、上下文控制、成本追踪

### 2.2 Out of Scope

**明确禁止的能力**：
- 固定部门长期存在
- 角色与 AI 实例强绑定
- Catalyst Hub 直接参与执行
- Task Force 无解散条件
- 为"管理便利"牺牲执行闭环
- 在业务逻辑中直接散落 AI 调用
- 无上限的 AI 调用
- 为每个角色创建独立 AI 实体或独立会话（除非确实需要并行执行、隔离记忆或使用不同模型档位）

### 2.3 Hard Boundaries

**必须永远禁止的行为**：
- 固定部门长期存在（临时结构必须可解散）
- 角色与 AI 实例强绑定（任务绑定在 Role 上，而非 AI 上）
- Catalyst Hub 参与执行（只能监控与纠偏）
- Task Force 无解散条件（必须明确解散条件）
- 一次性经验直接污染长期知识（需审计）
- 在业务逻辑中直接散落 AI 调用（必须通过统一服务层）
- 无上限的 AI 调用（必须有配额控制）
- 为每个角色创建独立 AI 实体（除非明确需要）
- 在每轮请求中携带完整历史对话（必须实现上下文裁剪）
- 将 AI 输出直接视为"事实"或"决策"（高风险领域必须人工确认）

---

## Section 3. CONCEPTUAL SYSTEM SHAPE

### 3.1 Core Concepts

**角色（Role）**：
- AI 行为的最小约束单位，非职位
- 包含：Purpose（存在目的）、Inputs（输入类型）、Outputs（可验证输出）、Boundaries（禁止事项）、Task Log（任务清单）
- 一个 AI 实例可同时承担多个 Role
- 一个 Role 可被多个 AI 实例化
- 任务永远绑定在 Role 上，而不是 AI 上

**细胞（Cell/Pod）**：
- 最小可独立交付执行单元
- 由若干角色组合而成
- 跨职能、端到端负责
- 不依赖外部部门即可完成任务
- 建议规模：3-7 个 AI 实例
- 对外接口：明确输入契约、明确输出格式、不暴露内部协作细节

**轻量中枢（Catalyst Hub）**：
- 工作流稳定器与纠偏系统，非管理层
- 允许职责：需求分流与 Cell 分配、工作流状态监控、发现死循环/无效执行、触发 Task Force、终止或重构失败流程
- 禁止：直接参与执行、替 Cell 做业务决策、长期占有资源

**临时工作小组（Task Force）**：
- 为特定目标临时组建的一次性执行结构
- 从多个 Cell 抽取能力，不改变原有 Cell 归属
- 必须具备：明确目标、明确输出、明确解散条件
- 结束后只保留：方法论总结、模板/规则、工作流更新建议

**基础设施层**：
- **AI 协作交接协议（Handoff Protocol）**：AI ↔ AI、AI ↔ 人类的统一通信与交付协议层
- **记忆/文档中心/知识库**：
  - Memory：运行时与历史上下文
  - Document Center：组织规范与模板
  - Knowledge Base：可复用推理与方法论

### 3.2 Major Logical Components

**组织结构层**：
- Role 定义与约束系统
- Cell 组成与接口系统
- Catalyst Hub 监控与纠偏系统
- Task Force 临时编组系统

**基础设施层**：
- Handoff Protocol 执行系统
- Memory/Document Center/Knowledge Base 存储与访问系统

**治理层**：
- 变更控制与版本管理系统
- 运行安全与异常处理系统
- 可观测性与质量保证系统
- AI 资源治理系统

### 3.3 High-Level Interaction

**工作流运行模式**：
1. 需求进入系统
2. Catalyst Hub 进行需求分流
3. 一个或多个 Cell 执行任务
4. （如需要）触发 Task Force 完成跨 Cell 任务
5. 结果交付（成功或"不可完成"标准输出）
6. 结构与规则回收/更新

**角色交互**：
- 任务必须指定主责 Role（对最终输出负责）和协作 Role（仅对其子输出负责）
- Role 通过 Handoff Protocol 进行交接
- Role 从 Memory/Document Center/Knowledge Base 读取上下文与约束
- Role 受 Catalyst Hub 监控，异常时触发纠偏

**知识管理交互**：
- Role 可读但受控写入 Memory/Document Center/Knowledge Base
- Document 与 Knowledge 的升级需审计
- 知识冲突时，相关流程进入保守模式，等待治理流程裁决

**变更控制交互**：
- 变更提案（RFC）提交到治理流程
- Catalyst Hub 执行审议（可引入独立审计角色复核）
- 沙盒验证 → 灰度发布 → 版本固化
- 关键指标恶化时立即回滚

---

## Section 4. CAPABILITY DECLARATION

### 4.1 Required ENGINE Stage

**required_stage**: 6

**理由**：
- 需要持久化存储（Memory/Document Center/Knowledge Base）
- 需要外部 API 调用（AI API Gateway）
- 可能需要后台任务（监控、健康检查、异步处理）

### 4.2 Persistence

**requires_persistence**: yes

**理由**：
- Memory：运行时与历史上下文需要持久化
- Document Center：组织规范与模板需要持久化
- Knowledge Base：可复用推理与方法论需要持久化
- Task Log：任务历史需要持久化
- 变更历史：版本管理需要持久化

### 4.3 External Interaction

**requires_external_api**: yes

**理由**：
- 需要通过 AI Gateway/Service 层调用 AI API
- 可能需要调用外部工具或服务（取决于具体业务需求）

### 4.4 Background Execution

**requires_background_jobs**: yes

**理由**：
- Catalyst Hub 需要持续监控工作流状态
- 需要健康检查（heartbeat/watchdog）
- 可能需要异步处理任务
- 可能需要定时任务（如知识库过期检查）

---

## Section 5. EXPLICIT PROHIBITIONS

**禁止的行为**：
- 禁止固定部门长期存在
- 禁止角色与 AI 实例强绑定
- 禁止 Catalyst Hub 参与执行
- 禁止 Task Force 无解散条件
- 禁止为"管理便利"牺牲执行闭环
- 禁止在业务逻辑中直接散落 AI 调用
- 禁止无上限的 AI 调用
- 禁止为每个角色创建独立 AI 实体（除非确实需要并行执行、隔离记忆或使用不同模型档位）
- 禁止在每轮请求中携带完整历史对话
- 禁止将 AI 输出直接视为"事实"或"决策"（高风险领域必须人工确认）
- 禁止一次性经验直接污染长期知识
- 禁止以"开发方便"为理由传入全量上下文
- 禁止在 system prompt 中重复描述角色背景或职责
- 禁止在 system prompt 中放置任何业务数据、任务描述或临时信息

**禁止的假设**：
- 禁止推断未声明的需求
- 禁止隐式扩展范围
- 禁止未经明确批准就实施
- 禁止假设"看起来像多个 AI"就需要多 agent
- 禁止假设 AI 输出是确定性的
- 禁止假设系统语义与某个模型行为强耦合

**禁止的捷径**：
- 禁止为管理便利牺牲执行闭环
- 禁止跳过变更控制流程
- 禁止跳过审计直接写入知识库
- 禁止跳过治理流程裁决知识冲突
- 禁止跳过人类确认执行高风险操作

---

## Section 6. MILESTONES

**Milestone 1: 核心结构定义完成**
- **描述**：Role、Cell、Catalyst Hub、Task Force 的概念定义与边界规则完成
- **完成标准**：所有核心概念的定义文档完成，边界规则明确，反模式清单完整

**Milestone 2: 基础设施层设计完成**
- **描述**：Handoff Protocol、Memory/Document Center/Knowledge Base 的设计规范完成
- **完成标准**：协议格式定义完成，存储结构设计完成，访问权限规则明确

**Milestone 3: 治理机制设计完成**
- **描述**：变更控制流程、运行安全机制、异常处理流程设计完成
- **完成标准**：变更流程文档完成，安全机制设计完成，升级路径明确

**Milestone 4: 可观测性设计完成**
- **描述**：日志结构、指标定义、回归测试机制设计完成
- **完成标准**：可观测性规范完成，关键指标清单完成，验证机制设计完成

**Milestone 5: AI 资源治理规范完成**
- **描述**：AI 调用规范、Token 节约规则、上下文控制机制设计完成
- **完成标准**：调用规范完成，成本控制机制设计完成，上下文管理规则明确

**Milestone 6: 系统集成验证**
- **描述**：所有组件集成，端到端工作流验证完成
- **完成标准**：需求能够从进入到交付完成闭环，异常能够被检测并升级，变更能够被控制并回滚

---

## Section 7. DECISION BOUNDARIES

**明确的决策边界**（不在此处给出具体答案，但明确决策范围）：

### 7.1 Stage Dependency

**决策边界**：
- 本 Blueprint 声明需要 Stage 6 能力（持久化、外部 API、后台任务）
- 这是 Blueprint 的 Stage Dependency 声明，不要求立即切换 ACTIVE_STAGE
- 实现时，必须等待 Stage 6 激活，或调整 Blueprint 要求以适配当前 Stage
- 决策权：由人类在激活 Blueprint 时决定是否等待 Stage 6，或调整 Blueprint 要求

### 7.2 Business Domain Scope

**决策边界**：
- 本 Blueprint 为 **domain-agnostic**（领域无关）的组织结构框架
- 不绑定任何特定业务领域
- 可在任何业务场景中应用，但需要根据具体业务领域填充 Role 的具体 Purpose 和 Boundaries
- 决策权：由人类在应用时决定具体业务领域，Blueprint 本身保持通用性

### 7.3 AI Gateway Interface Boundary

**决策边界**：
- AI Gateway / Service 层的职责边界：统一管理所有 AI 调用，提供配额控制、调用记录、限流、可替换性
- 不在此 Blueprint 中定义具体接口规范（API 签名、参数格式等）
- 具体接口规范留待实现时定义，但必须满足上述职责边界
- 决策权：由实现团队在实现时定义具体接口，但必须符合职责边界

### 7.4 Knowledge Base Conflict Resolution Process

**决策边界**：
- 治理流程必须包含：冲突检测、并列记录冲突观点与证据、保守模式触发、人类或治理角色裁决、裁决结果版本化
- 不在此 Blueprint 中定义具体裁决算法（如何比较证据强弱、如何自动裁决等）
- 具体裁决算法留待实现时定义，但必须遵循上述治理流程
- 决策权：由实现团队在实现时定义具体算法，但必须遵循治理流程

### 7.5 Cost Budget Configuration

**决策边界**：
- 成本预算（budget）必须作为配置项存在，可被 Catalyst Hub 或治理模块读取和控制
- 不在此 Blueprint 中定义具体预算数值（如 token 上限、成本阈值等）
- 具体预算数值留待部署时配置，但系统必须支持配置项机制
- 决策权：由运营团队在部署时配置具体数值，但系统必须提供配置机制

---

END OF BLUEPRINT

