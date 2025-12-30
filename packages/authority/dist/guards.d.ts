/**
 * Authority Layer Semantic Guards
 *
 * Authority: docs/authority/*_FROZEN_001.md
 *
 * These guards enforce semantic boundaries defined in the Authority Layer.
 * Guards G-1 through G-8 must be enforced by all layers (Frontend, Backend, Storage).
 */
import type { Company, Cell, Role, Relationship, Methodology, FreezeRecord } from './types';
/**
 * G-1: Forbid Field Extensions
 *
 * Rule: Unknown fields in Authority Layer facts must be rejected.
 * This guard is enforced by validate.ts (strict mode validation).
 *
 * Note: This guard is implemented in validate.ts, not here.
 * This function serves as documentation and can be used for additional checks.
 */
export declare function guardNoFieldExtensions(entity: unknown, allowedFields: readonly string[]): boolean;
/**
 * G-2: Forbid Dynamic Vocabulary
 *
 * Rule: Any display layer must not use vocabulary implying activity or change:
 * - current, latest, recent, running, monitoring, health, status (as active indicators)
 *
 * Exception: These words are allowed in prohibition contexts (e.g., "does NOT contain: 'Current' anything")
 *
 * @param text Text to check
 * @returns true if text contains forbidden dynamic vocabulary (in non-prohibition context)
 */
export declare function guardNoDynamicVocabulary(text: string): boolean;
/**
 * G-3: Forbid State Machine Concepts
 *
 * Rule: Company status can only be Draft/Frozen.
 * Snapshot data must not contain stage/phase/progress/readiness concepts.
 *
 * @param company Company entity to check
 * @returns true if valid (no state machine concepts)
 */
export declare function guardNoStateMachine(company: Company): boolean;
/**
 * Check if data contains forbidden state machine fields
 */
export declare function hasStateMachineFields(data: Record<string, unknown>): boolean;
/**
 * G-4: Role Attachment Rule
 *
 * Rule: Role must be attached to a Cell (via attached_to_cell_identifier).
 * Role cannot exist independently.
 *
 * This is enforced in validate.ts, but this guard can be used for additional checks.
 *
 * @param role Role to check
 * @param cellIdentifiers Set of valid Cell identifiers
 * @returns true if Role is properly attached to a Cell
 */
export declare function guardRoleAttachment(role: Role, cellIdentifiers: Set<string>): boolean;
/**
 * Validate that all Roles in a collection are attached to existing Cells
 */
export declare function validateAllRolesAttached(roles: Role[], cellIdentifiers: Set<string>): boolean;
/**
 * G-5: Topology Deny Temporal Concepts
 *
 * Rule: Relationship types must be nouns only (dependency, reference, input_output).
 * Forbidden: step, order, next, trigger (verbs implying execution/temporal order).
 *
 * @param relationshipType Relationship type to check
 * @returns true if relationship type is valid (noun, not verb)
 */
export declare function guardTopologyTypeEnum(relationshipType: string): boolean;
/**
 * Check if relationship description contains forbidden temporal/execution vocabulary
 */
export declare function guardNoTemporalVocabulary(description?: string): boolean;
/**
 * G-6: FreezeRecord Deny Event Semantics
 *
 * Rule: frozen_at is a static timestamp. Must be labeled as "Frozen at", not "Last updated".
 * FreezeRecord is not an event, activation, or deployment record.
 *
 * @param freezeRecord FreezeRecord to check
 * @returns true if valid (no event semantics)
 */
export declare function guardFreezeRecordNoEventSemantics(freezeRecord: FreezeRecord): boolean;
/**
 * Check if label is valid for frozen_at timestamp
 * Must be "Frozen at", not "Last updated", "Current", "Latest", etc.
 */
export declare function guardFreezeTimestampLabel(label: string): boolean;
/**
 * G-7: Frontend No Interpretation
 *
 * Rule: Frontend must only display fields. Must not derive/display:
 * - Health scores
 * - Risk scores
 * - Completeness scores
 * - Recommendation indicators
 *
 * This guard checks UI text for forbidden interpretation indicators.
 *
 * @param uiText UI text/label to check
 * @returns true if text does not contain interpretation indicators
 */
export declare function guardNoInterpretation(uiText: string): boolean;
/**
 * G-8: Copy Behavior Read-Only
 *
 * Rule: Copy Snapshot ID is allowed (read-only operation).
 * Must not extend to export/recommend/publish/deploy actions.
 *
 * This guard checks action labels/buttons for forbidden operations.
 *
 * @param actionLabel Action label/button text to check
 * @returns true if action is allowed (copy/read-only) or not forbidden
 */
export declare function guardCopyReadOnly(actionLabel: string): boolean;
/**
 * Run all guards on a set of data (for testing/validation)
 */
export interface GuardResult {
    guard: string;
    passed: boolean;
    message?: string;
}
export declare function runAllGuards(data: {
    company?: Company;
    cells?: Cell[];
    roles?: Role[];
    relationships?: Relationship[];
    methodology?: Methodology;
    freezeRecord?: FreezeRecord;
    uiLabels?: string[];
}): GuardResult[];
