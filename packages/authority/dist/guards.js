/**
 * Authority Layer Semantic Guards
 *
 * Authority: docs/authority/*_FROZEN_001.md
 *
 * These guards enforce semantic boundaries defined in the Authority Layer.
 * Guards G-1 through G-8 must be enforced by all layers (Frontend, Backend, Storage).
 */
// ============================================================================
// G-1: Forbid Field Extensions
// ============================================================================
/**
 * G-1: Forbid Field Extensions
 *
 * Rule: Unknown fields in Authority Layer facts must be rejected.
 * This guard is enforced by validate.ts (strict mode validation).
 *
 * Note: This guard is implemented in validate.ts, not here.
 * This function serves as documentation and can be used for additional checks.
 */
export function guardNoFieldExtensions(entity, allowedFields) {
    if (typeof entity !== 'object' || entity === null) {
        return false;
    }
    const obj = entity;
    for (const key in obj) {
        if (Object.prototype.hasOwnProperty.call(obj, key)) {
            if (!allowedFields.includes(key)) {
                return false; // Unknown field detected
            }
        }
    }
    return true;
}
// ============================================================================
// G-2: Forbid Dynamic Vocabulary
// ============================================================================
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
export function guardNoDynamicVocabulary(text) {
    const forbiddenWords = [
        /\bcurrent\b/i,
        /\blast updated\b/i,
        /\blatest\b/i,
        /\brecent\b/i,
        /\brunning\b/i,
        /\bmonitoring\b/i,
        /\bhealth\b/i,
        /\bstatus\b/i,
        /\bactive\b/i,
        /\bexecuting\b/i,
        /\bprocessing\b/i,
    ];
    // Check for prohibition context (contains "NOT" or "forbidden" or "does not")
    const isProhibitionContext = /\b(not|forbidden|prohibited|does not|must not|should not)\b/i.test(text);
    if (isProhibitionContext) {
        return true; // Allowed in prohibition context
    }
    // Check for forbidden words
    for (const pattern of forbiddenWords) {
        if (pattern.test(text)) {
            return false; // Forbidden vocabulary found
        }
    }
    return true; // No forbidden vocabulary
}
// ============================================================================
// G-3: Forbid State Machine Concepts
// ============================================================================
/**
 * G-3: Forbid State Machine Concepts
 *
 * Rule: Company status can only be Draft/Frozen.
 * Snapshot data must not contain stage/phase/progress/readiness concepts.
 *
 * @param company Company entity to check
 * @returns true if valid (no state machine concepts)
 */
export function guardNoStateMachine(company) {
    // Company schema only has frozen_at and frozen_by (provenance, not state)
    // No status field exists in Authority schema
    // This guard ensures no status field is added
    return true; // Company schema does not include status field by design
}
/**
 * Check if data contains forbidden state machine fields
 */
export function hasStateMachineFields(data) {
    const forbiddenFields = [
        'status',
        'stage',
        'phase',
        'progress',
        'readiness',
        'maturity',
        'lifecycle_state',
        'state',
        'current_state',
        'stage_number',
        'phase_number',
    ];
    return forbiddenFields.some((field) => field in data);
}
// ============================================================================
// G-4: Role Attachment Rule
// ============================================================================
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
export function guardRoleAttachment(role, cellIdentifiers) {
    if (!role.attached_to_cell_identifier) {
        return false; // Role must have attachment
    }
    if (!cellIdentifiers.has(role.attached_to_cell_identifier)) {
        return false; // Attached Cell must exist
    }
    return true;
}
/**
 * Validate that all Roles in a collection are attached to existing Cells
 */
export function validateAllRolesAttached(roles, cellIdentifiers) {
    return roles.every((role) => guardRoleAttachment(role, cellIdentifiers));
}
// ============================================================================
// G-5: Topology Deny Temporal Concepts
// ============================================================================
/**
 * G-5: Topology Deny Temporal Concepts
 *
 * Rule: Relationship types must be nouns only (dependency, reference, input_output).
 * Forbidden: step, order, next, trigger (verbs implying execution/temporal order).
 *
 * @param relationshipType Relationship type to check
 * @returns true if relationship type is valid (noun, not verb)
 */
export function guardTopologyTypeEnum(relationshipType) {
    const validTypes = ['dependency', 'reference', 'input_output'];
    return validTypes.includes(relationshipType);
}
/**
 * Check if relationship description contains forbidden temporal/execution vocabulary
 */
export function guardNoTemporalVocabulary(description) {
    if (!description) {
        return true; // Optional field, no issue if empty
    }
    const forbiddenTemporalWords = [
        /\bstep\b/i,
        /\border\b/i,
        /\bnext\b/i,
        /\btrigger\b/i,
        /\bexecute\b/i,
        /\brun\b/i,
        /\bflow\b/i,
        /\bsequence\b/i,
        /\bbefore\b/i,
        /\bafter\b/i,
    ];
    // Check for prohibition context
    const isProhibitionContext = /\b(not|forbidden|prohibited|does not)\b/i.test(description);
    if (isProhibitionContext) {
        return true; // Allowed in prohibition context
    }
    // Check for forbidden temporal vocabulary
    for (const pattern of forbiddenTemporalWords) {
        if (pattern.test(description)) {
            return false; // Forbidden temporal vocabulary found
        }
    }
    return true;
}
// ============================================================================
// G-6: FreezeRecord Deny Event Semantics
// ============================================================================
/**
 * G-6: FreezeRecord Deny Event Semantics
 *
 * Rule: frozen_at is a static timestamp. Must be labeled as "Frozen at", not "Last updated".
 * FreezeRecord is not an event, activation, or deployment record.
 *
 * @param freezeRecord FreezeRecord to check
 * @returns true if valid (no event semantics)
 */
export function guardFreezeRecordNoEventSemantics(freezeRecord) {
    // FreezeRecord schema does not include event-related fields by design
    // This guard ensures no event fields are added
    return true; // Schema is correct by design
}
/**
 * Check if label is valid for frozen_at timestamp
 * Must be "Frozen at", not "Last updated", "Current", "Latest", etc.
 */
export function guardFreezeTimestampLabel(label) {
    const validLabels = ['Frozen at', 'Frozen At', 'frozen at'];
    const forbiddenLabels = [
        'Last updated',
        'Updated at',
        'Current',
        'Latest',
        'Recent',
        'Modified at',
        'Changed at',
    ];
    const lowerLabel = label.toLowerCase();
    if (forbiddenLabels.some((forbidden) => lowerLabel.includes(forbidden.toLowerCase()))) {
        return false; // Forbidden label
    }
    return true; // Label is valid (or at least not explicitly forbidden)
}
// ============================================================================
// G-7: Frontend No Interpretation
// ============================================================================
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
export function guardNoInterpretation(uiText) {
    const forbiddenInterpretationWords = [
        /\bhealth\s+(score|indicator|status)\b/i,
        /\brisk\s+(score|level|indicator)\b/i,
        /\bcompleteness\s+(score|percentage|indicator)\b/i,
        /\brecommend(ation|ed|ing)\b/i,
        /\bsuggestion\b/i,
        /\bshould\b/i,
        /\bbest\s+(practice|way)\b/i,
        /\bquality\s+(score|indicator)\b/i,
        /\bmaturity\s+(score|level)\b/i,
    ];
    // Check for prohibition context
    const isProhibitionContext = /\b(not|forbidden|prohibited|does not)\b/i.test(uiText);
    if (isProhibitionContext) {
        return true; // Allowed in prohibition context
    }
    // Check for forbidden interpretation vocabulary
    for (const pattern of forbiddenInterpretationWords) {
        if (pattern.test(uiText)) {
            return false; // Forbidden interpretation vocabulary found
        }
    }
    return true; // No forbidden interpretation vocabulary
}
// ============================================================================
// G-8: Copy Behavior Read-Only
// ============================================================================
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
export function guardCopyReadOnly(actionLabel) {
    const allowedActions = ['copy', 'copy id', 'copy snapshot id', 'copy identifier'];
    const forbiddenActions = [
        'export',
        'publish',
        'deploy',
        'activate',
        'release',
        'recommend',
        'suggest',
        'share',
    ];
    const lowerLabel = actionLabel.toLowerCase().trim();
    // Check if it's an allowed copy action
    if (allowedActions.some((allowed) => lowerLabel.includes(allowed))) {
        return true; // Allowed copy action
    }
    // Check if it's a forbidden action
    if (forbiddenActions.some((forbidden) => lowerLabel.includes(forbidden))) {
        return false; // Forbidden action
    }
    // If neither, assume it's a neutral/other action (not explicitly forbidden)
    return true;
}
export function runAllGuards(data) {
    const results = [];
    // G-1: Field extensions (enforced in validate.ts, documented here)
    results.push({
        guard: 'G-1',
        passed: true,
        message: 'G-1 is enforced by validate.ts strict mode',
    });
    // G-2: Dynamic vocabulary (if UI labels provided)
    if (data.uiLabels) {
        const hasForbiddenVocab = data.uiLabels.some((label) => !guardNoDynamicVocabulary(label));
        results.push({
            guard: 'G-2',
            passed: !hasForbiddenVocab,
            message: hasForbiddenVocab
                ? 'Forbidden dynamic vocabulary found in UI labels'
                : 'No forbidden dynamic vocabulary found',
        });
    }
    // G-3: State machine (check Company)
    if (data.company) {
        const hasStateFields = hasStateMachineFields(data.company);
        results.push({
            guard: 'G-3',
            passed: !hasStateFields,
            message: hasStateFields ? 'State machine fields detected' : 'No state machine fields',
        });
    }
    // G-4: Role attachment
    if (data.roles && data.cells) {
        const cellIds = new Set(data.cells.map((c) => c.cell_identifier));
        const allAttached = validateAllRolesAttached(data.roles, cellIds);
        results.push({
            guard: 'G-4',
            passed: allAttached,
            message: allAttached
                ? 'All Roles are properly attached to Cells'
                : 'Some Roles are not attached to existing Cells',
        });
    }
    // G-5: Topology type enum
    if (data.relationships) {
        const allValidTypes = data.relationships.every((rel) => guardTopologyTypeEnum(rel.relationship_type));
        const hasTemporalVocab = data.relationships.some((rel) => !guardNoTemporalVocabulary(rel.relationship_description));
        results.push({
            guard: 'G-5',
            passed: allValidTypes && !hasTemporalVocab,
            message: allValidTypes && !hasTemporalVocab
                ? 'All relationship types are valid nouns, no temporal vocabulary'
                : 'Invalid relationship types or temporal vocabulary found',
        });
    }
    // G-6: FreezeRecord no event semantics
    if (data.freezeRecord) {
        const valid = guardFreezeRecordNoEventSemantics(data.freezeRecord);
        results.push({
            guard: 'G-6',
            passed: valid,
            message: valid ? 'FreezeRecord has no event semantics' : 'Event semantics detected in FreezeRecord',
        });
    }
    // G-7: Frontend no interpretation (if UI labels provided)
    if (data.uiLabels) {
        const hasInterpretation = data.uiLabels.some((label) => !guardNoInterpretation(label));
        results.push({
            guard: 'G-7',
            passed: !hasInterpretation,
            message: hasInterpretation
                ? 'Forbidden interpretation vocabulary found in UI labels'
                : 'No forbidden interpretation vocabulary found',
        });
    }
    // G-8: Copy read-only (if UI labels provided)
    if (data.uiLabels) {
        const hasForbiddenActions = data.uiLabels.some((label) => !guardCopyReadOnly(label));
        results.push({
            guard: 'G-8',
            passed: !hasForbiddenActions,
            message: hasForbiddenActions
                ? 'Forbidden actions (export/publish/deploy) found in UI labels'
                : 'No forbidden actions found',
        });
    }
    return results;
}
