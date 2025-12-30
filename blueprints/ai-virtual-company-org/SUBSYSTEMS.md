# Logical Subsystems Decomposition

本文档将 `ai-virtual-company-org` Blueprint 拆解为若干 Logical Subsystems，描述各子系统的职责、输入/输出抽象类型、相互关系，以及 Stage 依赖关系。

---

## Subsystem 1: Role Management Subsystem

### 职责（Responsibilities）
- 定义 Role 的规范结构（Purpose、Inputs、Outputs、Boundaries、Task Log）
- 管理 Role 的注册与查询
- 验证 Role 的完整性（是否包含所有必需字段）
- 维护 Role 与 AI 实例的映射关系（多对多）
- 提供 Role 的查询接口（按 Purpose、按能力等）

### 输入/输出抽象类型

**输入类型**：
- Role 定义（包含 Purpose、Inputs、Outputs、Boundaries）
- Role 查询请求（按标识符、按 Purpose、按能力范围）
- Role-AI 实例绑定请求（绑定/解绑）
- Role 更新请求（更新 Purpose、Inputs、Outputs、Boundaries）

**输出类型**：
- Role 定义（完整规范）
- Role 列表（满足查询条件的 Role 集合）
- Role 验证结果（是否完整、是否冲突）
- Role-AI 实例映射关系

### 与其他 Subsystem 的关系
- **被 Cell Composition Subsystem 使用**：Cell 需要查询可用的 Role 来组成执行单元
- **被 Catalyst Hub Subsystem 使用**：Hub 需要查询 Role 来分配任务
- **被 Change Control Subsystem 管理**：Role 定义的变更需要走变更控制流程
- **被 Knowledge Management Subsystem 存储**：Role 定义存储在 Document Center

### Stage 依赖
- **Stage 5**：可以设计 Role 的数据结构、验证规则、查询逻辑（概念设计）
- **Stage 6 依赖**：需要持久化 Role 定义、Role-AI 映射关系、Task Log 历史

---

## Subsystem 2: Cell Composition Subsystem

### 职责（Responsibilities）
- 管理 Cell 的组成（哪些 Role 组合成一个 Cell）
- 定义 Cell 的对外接口契约（输入契约、输出格式）
- 维护 Cell 的状态（活跃、空闲、执行中、已解散）
- 管理 Cell 的生命周期（创建、激活、解散）
- 验证 Cell 的完整性（是否包含足够 Role 完成端到端任务）

### 输入/输出抽象类型

**输入类型**：
- Cell 组成请求（Role 列表、输入契约、输出格式）
- Cell 状态查询请求（按标识符、按状态、按能力）
- Cell 生命周期操作（创建、激活、解散）
- Cell 能力查询请求（能否处理某类任务）

**输出类型**：
- Cell 定义（组成、接口契约、状态）
- Cell 列表（满足查询条件的 Cell 集合）
- Cell 验证结果（是否完整、是否可执行）
- Cell 能力描述（能处理的任务类型）

### 与其他 Subsystem 的关系
- **使用 Role Management Subsystem**：查询可用的 Role 来组成 Cell
- **被 Catalyst Hub Subsystem 使用**：Hub 需要查询 Cell 来分配任务
- **被 Task Force Subsystem 使用**：Task Force 从 Cell 抽取能力
- **被 Handoff Protocol Subsystem 使用**：Cell 之间通过协议交接
- **被 Change Control Subsystem 管理**：Cell 组成的变更需要走变更控制流程
- **被 Knowledge Management Subsystem 存储**：Cell 定义存储在 Document Center

### Stage 依赖
- **Stage 5**：可以设计 Cell 的数据结构、组成规则、接口契约格式（概念设计）
- **Stage 6 依赖**：需要持久化 Cell 定义、Cell 状态、Cell 历史记录

---

## Subsystem 3: Catalyst Hub Subsystem

### 职责（Responsibilities）
- 接收外部需求并进行分析
- 将需求分流到合适的 Cell
- 持续监控工作流状态（所有 Cell 的执行状态）
- 检测异常情况（死循环、无效执行、超时、失败预算超限）
- 触发 Task Force 的创建（当需要跨 Cell 协作时）
- 终止或重构失败流程
- 执行健康检查（heartbeat/watchdog）
- 管理成本预算（读取配置、监控使用、触发断路器）

### 输入/输出抽象类型

**输入类型**：
- 外部需求（任务描述、目标、约束）
- Cell 状态更新（执行进度、结果、异常）
- 异常报告（死循环、超时、失败）
- 成本使用报告（token 消耗、API 调用次数）
- 健康检查请求

**输出类型**：
- 任务分配决策（分配给哪个 Cell、分配理由）
- Task Force 创建指令（目标、组成、解散条件）
- 流程终止指令（终止原因、回滚方案）
- 异常升级通知（需要人类介入的情况）
- 成本预算状态（当前使用、是否超限、断路器状态）

### 与其他 Subsystem 的关系
- **使用 Role Management Subsystem**：查询 Role 来理解任务需求
- **使用 Cell Composition Subsystem**：查询 Cell 来分配任务
- **使用 Task Force Subsystem**：创建和管理 Task Force
- **使用 Handoff Protocol Subsystem**：监控交接过程
- **使用 Knowledge Management Subsystem**：读取组织规范和历史经验
- **使用 Change Control Subsystem**：提交变更提案、执行审议
- **使用 Safety & Exception Handling Subsystem**：报告异常、触发安全机制
- **使用 Observability Subsystem**：记录监控数据、查询指标
- **使用 AI Resource Governance Subsystem**：管理 AI 调用配额

### Stage 依赖
- **Stage 5**：可以设计需求分析逻辑、分流规则、监控规则、异常检测规则（概念设计）
- **Stage 6 依赖**：
  - 需要后台任务（持续监控、健康检查）
  - 需要持久化监控状态、任务分配历史
  - 需要调用外部 API（AI Gateway）

---

## Subsystem 4: Task Force Subsystem

### 职责（Responsibilities）
- 管理 Task Force 的创建（从多个 Cell 抽取能力）
- 维护 Task Force 的生命周期（创建、执行、解散）
- 验证 Task Force 的完整性（明确目标、明确输出、明确解散条件）
- 在 Task Force 解散后，回收方法论总结、模板/规则、工作流更新建议

### 输入/输出抽象类型

**输入类型**：
- Task Force 创建请求（目标、所需能力、解散条件）
- Cell 能力抽取请求（从哪些 Cell 抽取哪些 Role）
- Task Force 状态更新（执行进度、结果）
- Task Force 解散请求（解散原因、回收物）

**输出类型**：
- Task Force 定义（目标、组成、解散条件、状态）
- Task Force 列表（活跃的、已解散的）
- Task Force 回收物（方法论总结、模板、工作流更新建议）
- Task Force 验证结果（是否完整、是否可执行）

### 与其他 Subsystem 的关系
- **使用 Cell Composition Subsystem**：从 Cell 抽取能力，不改变 Cell 归属
- **使用 Role Management Subsystem**：查询 Role 来组成 Task Force
- **被 Catalyst Hub Subsystem 使用**：Hub 触发 Task Force 创建
- **使用 Handoff Protocol Subsystem**：Task Force 内部通过协议协作
- **被 Change Control Subsystem 管理**：Task Force 回收的工作流更新需要走变更控制
- **被 Knowledge Management Subsystem 存储**：Task Force 回收物存储在 Knowledge Base

### Stage 依赖
- **Stage 5**：可以设计 Task Force 的数据结构、创建规则、解散条件格式（概念设计）
- **Stage 6 依赖**：需要持久化 Task Force 定义、Task Force 状态、回收物

---

## Subsystem 5: Handoff Protocol Subsystem

### 职责（Responsibilities）
- 定义 AI ↔ AI、AI ↔ 人类的统一通信与交付协议格式
- 验证交接文档的格式完整性（必需字段：sender_role、receiver_role、task_id、timestamp、assumptions、deliverables、risks）
- 执行交接文档的格式校验（不合规则拒收并要求重发）
- 管理交接文档的流转（发送、接收、确认）
- 分离工作态文档与展示态文档

### 输入/输出抽象类型

**输入类型**：
- 交接文档（包含所有必需字段的结构化文档）
- 交接请求（发送方、接收方、任务标识）
- 交接确认请求（接收方确认收到、理解、可执行）

**输出类型**：
- 交接文档（格式化的、已验证的）
- 格式验证结果（是否完整、是否合规）
- 交接状态（已发送、已接收、已确认、已拒绝）
- 格式错误报告（缺失字段、格式不符）

### 与其他 Subsystem 的关系
- **被所有执行单元使用**：Role、Cell、Task Force 都通过此协议交接
- **被 Catalyst Hub Subsystem 使用**：Hub 监控交接过程
- **被 Observability Subsystem 使用**：记录交接轨迹
- **被 Knowledge Management Subsystem 存储**：交接文档存储在 Memory（运行时）或 Document Center（模板）

### Stage 依赖
- **Stage 5**：可以设计协议格式、验证规则、必需字段定义（概念设计）
- **Stage 6 依赖**：需要持久化交接文档、交接历史记录

---

## Subsystem 6: Knowledge Management Subsystem

### 职责（Responsibilities）
- 管理 Memory（运行时与历史上下文）的存储与访问
- 管理 Document Center（组织规范与模板）的存储与访问
- 管理 Knowledge Base（可复用推理与方法论）的存储与访问
- 实现访问权限控制（Role 可读但受控写入）
- 管理版本、过期与废弃（Versioning、TTL、Deprecation）
- 检测知识冲突（同一事实的多个版本）
- 触发保守模式（当知识冲突未裁决时）

### 输入/输出抽象类型

**输入类型**：
- 知识写入请求（内容、类型、来源、版本）
- 知识查询请求（按标识符、按类型、按版本、按时间范围）
- 知识更新请求（更新内容、新版本号）
- 知识废弃请求（废弃原因、替代项）
- 冲突检测请求（检测指定知识的冲突版本）

**输出类型**：
- 知识条目（内容、元数据、版本信息）
- 知识列表（满足查询条件的知识集合）
- 访问权限验证结果（是否可读、是否可写）
- 冲突报告（冲突版本列表、证据强弱）
- 保守模式触发通知（哪些流程需要进入保守模式）

### 与其他 Subsystem 的关系
- **被所有执行单元使用**：Role、Cell、Task Force 都从此读取上下文与约束
- **被 Change Control Subsystem 管理**：Document 与 Knowledge 的升级需审计
- **被 Safety & Exception Handling Subsystem 使用**：冲突检测触发保守模式
- **被 Observability Subsystem 使用**：记录知识访问日志

### Stage 依赖
- **Stage 5**：可以设计知识的数据结构、访问权限规则、版本管理规则、冲突检测规则（概念设计）
- **Stage 6 依赖**：
  - 需要持久化存储（Memory、Document Center、Knowledge Base）
  - 需要后台任务（过期检查、TTL 管理）

---

## Subsystem 7: Change Control Subsystem

### 职责（Responsibilities）
- 接收变更提案（RFC：动机、影响面、回滚方案、验证方式）
- 执行审议流程（由 Catalyst Hub 执行，可引入独立审计角色复核）
- 管理沙盒验证（在隔离环境跑回归测试或模拟任务）
- 管理灰度发布（小流量/小任务范围启用）
- 管理版本固化（写入 Document Center，更新版本号与变更日志）
- 执行回滚（若关键指标恶化，立即回滚到上一版本）

### 输入/输出抽象类型

**输入类型**：
- 变更提案（RFC：变更对象、动机、影响面、回滚方案、验证方式）
- 审议请求（需要审议的变更提案）
- 沙盒验证请求（在隔离环境验证变更）
- 灰度发布请求（小范围启用变更）
- 版本固化请求（将变更写入 Document Center）
- 回滚请求（回滚到指定版本）

**输出类型**：
- 变更提案状态（待审议、审议中、已批准、已拒绝、已回滚）
- 审议结果（批准/拒绝、理由、条件）
- 验证结果（沙盒验证是否通过、回归测试结果）
- 灰度发布状态（当前范围、指标状态）
- 版本信息（版本号、变更日志、生效时间）
- 回滚结果（是否成功、回滚到哪个版本）

### 与其他 Subsystem 的关系
- **管理所有 Subsystem 的变更**：Role、Cell、Handoff Protocol、Knowledge Base 的变更都需走此流程
- **使用 Catalyst Hub Subsystem**：Hub 执行审议
- **使用 Knowledge Management Subsystem**：将变更固化到 Document Center
- **使用 Observability Subsystem**：查询关键指标来判断是否需要回滚
- **使用 Safety & Exception Handling Subsystem**：触发回滚机制

### Stage 依赖
- **Stage 5**：可以设计变更流程、审议规则、版本管理规则、回滚规则（概念设计）
- **Stage 6 依赖**：
  - 需要持久化变更历史、版本信息
  - 需要后台任务（灰度发布监控、指标追踪）

---

## Subsystem 8: Safety & Exception Handling Subsystem

### 职责（Responsibilities）
- 执行健康检查（heartbeat/watchdog）机制
- 实现断路器（Circuit Breaker）：超时、最大回合数、失败预算
- 管理异常检测（死循环、无效执行、超时、失败预算超限）
- 触发保守模式（当知识冲突未裁决时）
- 管理人类升级路径（Escalation）：高风险操作、多次失败、知识冲突、越权行为
- 管理任务不可完成时的标准输出（原因、建议、风险提示）

### 输入/输出抽象类型

**输入类型**：
- 健康检查请求（检查指定组件的健康状态）
- 异常报告（死循环、超时、失败、越权行为）
- 失败计数（同类失败的累计次数）
- 高风险操作请求（需要人类确认的操作）
- 知识冲突通知（需要裁决的冲突）

**输出类型**：
- 健康状态（健康、异常、不可用）
- 断路器状态（正常、触发、恢复）
- 异常处理决策（终止、重试、升级、保守模式）
- 人类升级通知（升级原因、需要的信息、建议操作）
- 任务不可完成输出（原因、建议、风险提示、保守替代方案）

### 与其他 Subsystem 的关系
- **被 Catalyst Hub Subsystem 使用**：Hub 报告异常、触发安全机制
- **被所有执行单元使用**：Role、Cell、Task Force 都受此保护
- **使用 Knowledge Management Subsystem**：检测知识冲突、触发保守模式
- **使用 Observability Subsystem**：查询失败统计、超时统计

### Stage 依赖
- **Stage 5**：可以设计异常检测规则、断路器规则、升级路径规则（概念设计）
- **Stage 6 依赖**：
  - 需要后台任务（健康检查、watchdog）
  - 需要持久化异常记录、失败统计

---

## Subsystem 9: Observability Subsystem

### 职责（Responsibilities）
- 记录任务日志（ID、目标、输入、输出、状态、耗时、成本估算）
- 记录角色/Cell 执行轨迹（关键决策点、工具调用、交接文档）
- 记录失败原因分类（用于统计与改进）
- 追踪关键指标（任务一次成功率/重试率、平均 token 成本、平均交付周期、失败类型 Top N、Task Force 触发频率）
- 提供可回放记录（任务执行过程可回放）
- 管理回归测试（对高频任务建立"黄金用例"）

### 输入/输出抽象类型

**输入类型**：
- 任务日志写入请求（任务信息、执行轨迹）
- 指标查询请求（按时间范围、按类型、按组件）
- 执行轨迹查询请求（按任务 ID、按 Role、按 Cell）
- 回归测试请求（运行黄金用例）

**输出类型**：
- 任务日志（完整的任务执行记录）
- 执行轨迹（关键决策点、工具调用、交接文档）
- 关键指标（成功率、成本、周期、失败类型分布）
- 可回放记录（任务执行过程的完整记录）
- 回归测试结果（是否通过、差异报告）

### 与其他 Subsystem 的关系
- **被所有 Subsystem 使用**：所有 Subsystem 都向此写入日志和指标
- **被 Change Control Subsystem 使用**：查询关键指标来判断是否需要回滚
- **被 Catalyst Hub Subsystem 使用**：查询指标来监控系统健康
- **被 Safety & Exception Handling Subsystem 使用**：查询失败统计

### Stage 依赖
- **Stage 5**：可以设计日志结构、指标定义、可回放记录格式（概念设计）
- **Stage 6 依赖**：
  - 需要持久化日志、指标、执行轨迹
  - 需要后台任务（指标聚合、统计分析）

---

## Subsystem 10: AI Resource Governance Subsystem

### 职责（Responsibilities）
- 统一管理所有 AI 调用（通过 AI Gateway / Service 层）
- 实现配额控制（budget：token 上限、成本阈值）
- 实现调用记录（所有调用必须可被记录、统计与限流）
- 实现限流机制（防止无上限调用）
- 实现断路器（超额/异常自动停用）
- 管理上下文构建（明确来源、最大 token 上限、可回放、可审计）
- 管理 Token 节约（单模型实例、多角色约束、上下文裁剪、滑动窗口）
- 管理模型可替换性（禁止系统语义与某个模型行为强耦合）

### 输入/输出抽象类型

**输入类型**：
- AI 调用请求（模型、用途、任务类型、角色、上下文）
- 配额查询请求（当前使用、剩余配额）
- 上下文构建请求（来源、最大 token 上限）
- 模型切换请求（切换到新模型）

**输出类型**：
- AI 调用结果（输出、token 消耗、成本）
- 配额状态（当前使用、剩余、是否超限）
- 调用记录（调用时间、模型、用途、token 消耗、成本）
- 断路器状态（正常、触发、恢复）
- 上下文构建结果（裁剪后的上下文、token 数量）

### 与其他 Subsystem 的关系
- **被所有执行单元使用**：Role、Cell、Task Force 都通过此调用 AI
- **被 Catalyst Hub Subsystem 使用**：Hub 管理成本预算
- **被 Observability Subsystem 使用**：记录 AI 调用日志和成本
- **被 Safety & Exception Handling Subsystem 使用**：触发断路器

### Stage 依赖
- **Stage 5**：可以设计调用规范、配额控制规则、上下文管理规则、Token 节约规则（概念设计）
- **Stage 6 依赖**：
  - 需要外部 API 调用（AI API Gateway）
  - 需要持久化调用记录、配额使用历史
  - 需要后台任务（配额监控、限流执行）

---

## Stage 依赖总结

### Stage 5 可设计（概念设计，不实现）
所有 10 个 Subsystem 都可以在 Stage 5 进行概念设计：
- 数据结构设计
- 职责边界定义
- 输入/输出抽象类型定义
- 交互关系设计
- 规则和约束定义

### Stage 6 依赖（需要实现）
以下 Subsystem 明确依赖 Stage 6 能力：

**需要持久化存储**：
- Subsystem 1: Role Management（Role 定义、映射关系、Task Log）
- Subsystem 2: Cell Composition（Cell 定义、状态、历史）
- Subsystem 4: Task Force（Task Force 定义、状态、回收物）
- Subsystem 5: Handoff Protocol（交接文档、交接历史）
- Subsystem 6: Knowledge Management（Memory、Document Center、Knowledge Base）
- Subsystem 7: Change Control（变更历史、版本信息）
- Subsystem 8: Safety & Exception Handling（异常记录、失败统计）
- Subsystem 9: Observability（日志、指标、执行轨迹）
- Subsystem 10: AI Resource Governance（调用记录、配额使用历史）

**需要外部 API 调用**：
- Subsystem 10: AI Resource Governance（AI API Gateway）

**需要后台任务**：
- Subsystem 3: Catalyst Hub（持续监控、健康检查）
- Subsystem 6: Knowledge Management（过期检查、TTL 管理）
- Subsystem 7: Change Control（灰度发布监控、指标追踪）
- Subsystem 8: Safety & Exception Handling（健康检查、watchdog）
- Subsystem 9: Observability（指标聚合、统计分析）
- Subsystem 10: AI Resource Governance（配额监控、限流执行）

---

END OF SUBSYSTEMS DECOMPOSITION

