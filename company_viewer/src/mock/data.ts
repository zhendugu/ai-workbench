/**
 * Mock Data for UI Prototype
 * Based on UI_DESIGN_DRAFT_001.md
 */

export interface Company {
  id: string
  name: string
  nameEn: string
  foundedDate?: string
  description?: string
  descriptionEn?: string
  vision?: string
  visionEn?: string
  mission?: string
  missionEn?: string
}

export interface Cell {
  id: string
  name: string
  nameEn: string
  type: 'department' | 'project' | 'other'
  parentCellId?: string
  leader?: string
  leaderEn?: string
  description?: string
  descriptionEn?: string
  status: 'active' | 'paused' | 'archived'
  createdAt: string
  memberCount: number
}

export interface Role {
  id: string
  name: string
  nameEn: string
  type: 'technical' | 'management' | 'operations' | 'design' | 'other'
  description: string
  descriptionEn: string
  requiredSkills?: string[]
  level?: 'junior' | 'intermediate' | 'senior' | 'expert'
  linkedMethodologyId?: string
}

export interface TaskForce {
  id: string
  name: string
  nameEn: string
  objective: string
  objectiveEn: string
  leader: string
  leaderEn: string
  startDate: string
  endDate?: string
  status: 'planning' | 'active' | 'completed' | 'cancelled'
  memberIds: string[]
  sourceCellIds: string[]
}

export interface Connection {
  id: string
  sourceEntityId: string
  sourceEntityType: 'cell' | 'taskforce' | 'person'
  targetEntityId: string
  targetEntityType: 'cell' | 'taskforce' | 'person'
  type: 'reporting' | 'collaboration' | 'support' | 'dependency' | 'mentoring'
  strength?: number // 0-100
  description?: string
  descriptionEn?: string
}

export interface Methodology {
  id: string
  name: string
  nameEn: string
  category: 'development' | 'design' | 'management' | 'other'
  description: string
  descriptionEn: string
  useCases?: string
  useCasesEn?: string
  processSteps?: string[]
  processStepsEn?: string[]
  relatedTools?: string[]
  references?: string[]
  appliedToCellIds?: string[]
  appliedToRoleIds?: string[]
}

// Mock Data
export const mockCompany: Company = {
  id: 'company-1',
  name: '示例科技公司',
  nameEn: 'Example Tech Company',
  foundedDate: '2020-01-15',
  description: '一家专注于创新科技解决方案的公司',
  descriptionEn: 'A company focused on innovative technology solutions',
  vision: '成为行业领先的科技服务提供商',
  visionEn: 'To become a leading technology service provider in the industry',
  mission: '通过技术创新为客户创造价值',
  missionEn: 'Create value for customers through technological innovation',
}

export const mockCells: Cell[] = [
  {
    id: 'cell-1',
    name: '研发部门',
    nameEn: 'R&D Department',
    type: 'department',
    leader: '张三',
    leaderEn: 'Zhang San',
    description: '负责产品研发和技术创新',
    descriptionEn: 'Responsible for product development and technological innovation',
    status: 'active',
    createdAt: '2020-01-20T00:00:00Z',
    memberCount: 15,
  },
  {
    id: 'cell-2',
    name: '设计部门',
    nameEn: 'Design Department',
    type: 'department',
    leader: '李四',
    leaderEn: 'Li Si',
    description: '负责产品设计和用户体验',
    descriptionEn: 'Responsible for product design and user experience',
    status: 'active',
    createdAt: '2020-02-01T00:00:00Z',
    memberCount: 8,
  },
  {
    id: 'cell-3',
    name: '产品小组',
    nameEn: 'Product Team',
    type: 'project',
    parentCellId: 'cell-1',
    leader: '王五',
    leaderEn: 'Wang Wu',
    description: '负责核心产品的开发和维护',
    descriptionEn: 'Responsible for the development and maintenance of core products',
    status: 'active',
    createdAt: '2021-03-15T00:00:00Z',
    memberCount: 5,
  },
]

export const mockRoles: Role[] = [
  {
    id: 'role-1',
    name: '前端开发工程师',
    nameEn: 'Frontend Developer',
    type: 'technical',
    description: '负责前端界面开发和技术实现',
    descriptionEn: 'Responsible for frontend interface development and technical implementation',
    requiredSkills: ['React', 'TypeScript', 'CSS'],
    level: 'senior',
  },
  {
    id: 'role-2',
    name: 'UI设计师',
    nameEn: 'UI Designer',
    type: 'design',
    description: '负责用户界面设计和视觉规范',
    descriptionEn: 'Responsible for user interface design and visual guidelines',
    requiredSkills: ['Figma', 'Adobe XD', 'Design System'],
    level: 'intermediate',
  },
  {
    id: 'role-3',
    name: '产品经理',
    nameEn: 'Product Manager',
    type: 'management',
    description: '负责产品规划和管理',
    descriptionEn: 'Responsible for product planning and management',
    requiredSkills: ['Product Strategy', 'Agile', 'Analytics'],
    level: 'senior',
  },
]

export const mockTaskForces: TaskForce[] = [
  {
    id: 'tf-1',
    name: '移动端优化项目',
    nameEn: 'Mobile Optimization Project',
    objective: '优化移动端用户体验和性能',
    objectiveEn: 'Optimize mobile user experience and performance',
    leader: '赵六',
    leaderEn: 'Zhao Liu',
    startDate: '2024-01-01',
    endDate: '2024-06-30',
    status: 'active',
    memberIds: ['member-1', 'member-2', 'member-3'],
    sourceCellIds: ['cell-1', 'cell-2'],
  },
  {
    id: 'tf-2',
    name: 'API重构项目',
    nameEn: 'API Refactoring Project',
    objective: '重构后端API架构，提升系统性能',
    objectiveEn: 'Refactor backend API architecture to improve system performance',
    leader: '孙七',
    leaderEn: 'Sun Qi',
    startDate: '2024-02-01',
    status: 'active',
    memberIds: ['member-4', 'member-5'],
    sourceCellIds: ['cell-1'],
  },
]

export const mockConnections: Connection[] = [
  {
    id: 'conn-1',
    sourceEntityId: 'cell-1',
    sourceEntityType: 'cell',
    targetEntityId: 'cell-2',
    targetEntityType: 'cell',
    type: 'collaboration',
    strength: 80,
    description: '研发部门与设计部门密切协作',
    descriptionEn: 'R&D Department closely collaborates with Design Department',
  },
  {
    id: 'conn-2',
    sourceEntityId: 'cell-3',
    sourceEntityType: 'cell',
    targetEntityId: 'cell-1',
    targetEntityType: 'cell',
    type: 'reporting',
    description: '产品小组向研发部门汇报',
    descriptionEn: 'Product Team reports to R&D Department',
  },
]

export const mockMethodologies: Methodology[] = [
  {
    id: 'method-1',
    name: '敏捷开发方法',
    nameEn: 'Agile Development Methodology',
    category: 'development',
    description: '采用敏捷开发流程，快速迭代和响应变化',
    descriptionEn: 'Adopting agile development process for rapid iteration and response to changes',
    useCases: '适用于快速变化的产品开发场景',
    useCasesEn: 'Suitable for rapidly changing product development scenarios',
    processSteps: ['需求分析', '迭代规划', '开发实现', '测试验证', '发布上线'],
    processStepsEn: ['Requirement Analysis', 'Iteration Planning', 'Development', 'Testing', 'Release'],
    relatedTools: ['Jira', 'Confluence', 'Git'],
    appliedToCellIds: ['cell-1', 'cell-3'],
    appliedToRoleIds: ['role-1', 'role-3'],
  },
  {
    id: 'method-2',
    name: '设计思维方法',
    nameEn: 'Design Thinking Methodology',
    category: 'design',
    description: '以用户为中心的设计思维流程',
    descriptionEn: 'User-centered design thinking process',
    useCases: '适用于需要深度理解用户需求的设计项目',
    useCasesEn: 'Suitable for design projects that require deep understanding of user needs',
    processSteps: ['同理心', '定义问题', '构思方案', '原型制作', '测试验证'],
    processStepsEn: ['Empathize', 'Define', 'Ideate', 'Prototype', 'Test'],
    relatedTools: ['Figma', 'Miro', 'User Research Tools'],
    appliedToCellIds: ['cell-2'],
    appliedToRoleIds: ['role-2'],
  },
]

