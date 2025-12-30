/**
 * Authority Layer Runtime Package
 *
 * Authority: docs/authority/*_FROZEN_001.md
 * Highest Authority: docs/frontend/DT_FE_DECISION_RECORD_001.md
 *
 * This package provides:
 * - TypeScript types for Authority Layer facts
 * - Strict validation functions
 * - Semantic guards
 *
 * All frontend/backend/storage must use this package for reading/writing Authority facts.
 */
export type { Company, Cell, Role, RoleConstraintType, Relationship, RelationshipType, Topology, Methodology, FreezeRecord, FrozenSnapshot, } from './types';
export { validateCompany, validateCell, validateRole, validateRelationship, validateTopology, validateMethodology, validateFreezeRecord, validateFrozenSnapshot, type ValidationResult, type ValidationError, } from './validate';
export { guardNoFieldExtensions, guardNoDynamicVocabulary, guardNoStateMachine, hasStateMachineFields, guardRoleAttachment, validateAllRolesAttached, guardTopologyTypeEnum, guardNoTemporalVocabulary, guardFreezeRecordNoEventSemantics, guardFreezeTimestampLabel, guardNoInterpretation, guardCopyReadOnly, runAllGuards, type GuardResult, } from './guards';
