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
// Export validation functions
export { validateCompany, validateCell, validateRole, validateRelationship, validateTopology, validateMethodology, validateFreezeRecord, validateFrozenSnapshot, } from './validate';
// Export guard functions
export { guardNoFieldExtensions, guardNoDynamicVocabulary, guardNoStateMachine, hasStateMachineFields, guardRoleAttachment, validateAllRolesAttached, guardTopologyTypeEnum, guardNoTemporalVocabulary, guardFreezeRecordNoEventSemantics, guardFreezeTimestampLabel, guardNoInterpretation, guardCopyReadOnly, runAllGuards, } from './guards';
