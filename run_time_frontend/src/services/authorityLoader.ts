/**
 * Authority Data Loader
 * 
 * Authority: This is the ingestion boundary where Authority data is loaded and validated.
 * 
 * Responsibilities:
 * 1. Load snapshot JSON files
 * 2. Construct FrozenSnapshot object
 * 3. Validate using Authority validation (MANDATORY)
 * 4. Transform to view models if valid
 * 5. Return validated data or error
 * 
 * This is the ONLY point where Authority data enters the Run-Time Frontend.
 * 
 * SNAPSHOT LOADING CONTRACT:
 * - Base path: /snapshots/authority (served from public/ directory)
 * - Snapshot directory: /snapshots/authority/{frozenCompanyIdentifier}/
 * - Required files:
 *   1. company.json (Company fact - single object)
 *   2. cells.json (Array of Cell facts)
 *   3. roles.json (Array of Role facts)
 *   4. topology.json (Array of Relationship facts)
 *   5. methodology.json (Methodology fact - single object)
 *   6. freeze_record.json (FreezeRecord fact - single object)
 * - All files MUST be valid JSON conforming to Authority schemas
 * - Invalid JSON or non-JSON responses are rejected
 * - HTML fallback responses are rejected (indicates missing files)
 */

import { validateFrozenSnapshot, type FrozenSnapshot } from '@ai-workbench/authority';
import { transformFrozenSnapshot, type FrozenSnapshotViewModel } from './authorityTransform';

export interface LoadSnapshotResult {
  success: boolean;
  data?: FrozenSnapshotViewModel;
  error?: string;
  validationErrors?: Array<{ field: string; message: string }>;
}

/**
 * Load and validate frozen snapshot from JSON files
 * 
 * @param snapshotDir Directory containing snapshot JSON files
 * @returns Loaded and validated snapshot, or error
 */
export async function loadFrozenSnapshot(
  snapshotDir: string
): Promise<LoadSnapshotResult> {
  try {
    // Load JSON files from public directory
    // Contract: All files must be valid JSON, not HTML or other formats
    const [companyResponse, cellsResponse, rolesResponse, topologyResponse, methodologyResponse, freezeRecordResponse] = await Promise.all([
      fetch(`${snapshotDir}/company.json`),
      fetch(`${snapshotDir}/cells.json`),
      fetch(`${snapshotDir}/roles.json`),
      fetch(`${snapshotDir}/topology.json`),
      fetch(`${snapshotDir}/methodology.json`),
      fetch(`${snapshotDir}/freeze_record.json`),
    ]);

    // Verify all responses are JSON (not HTML fallback)
    // Check content-type and peek at response text to detect HTML
    const responseChecks = await Promise.all(
      [companyResponse, cellsResponse, rolesResponse, topologyResponse, methodologyResponse, freezeRecordResponse].map(async (response) => {
        const contentType = response.headers.get('content-type');
        const text = await response.text();
        
        // Check for HTML fallback (Vite dev server returns index.html for missing files)
        if (text.trim().startsWith('<!') || text.trim().startsWith('<html')) {
          return {
            error: 'Snapshot file not found (HTML fallback returned). Ensure JSON files exist in public/snapshots/authority/{frozenId}/',
          };
        }
        
        // Check content-type if available (but be lenient - some servers don't set it correctly)
        if (contentType && !contentType.includes('application/json') && !contentType.includes('text/json') && !contentType.includes('text/plain')) {
          return {
            error: `Invalid content type: expected JSON, got ${contentType}`,
          };
        }
        
        // Try to parse as JSON
        try {
          return { json: JSON.parse(text) };
        } catch (parseError) {
          return {
            error: `Invalid JSON: ${parseError instanceof Error ? parseError.message : 'Unknown parse error'}`,
          };
        }
      })
    );

    // Check for errors in any response
    for (const check of responseChecks) {
      if ('error' in check) {
        return {
          success: false,
          error: check.error,
        };
      }
    }

    // All responses are valid JSON (TypeScript guard: we've checked for errors above)
    const [companyJson, cellsJson, rolesJson, topologyJson, methodologyJson, freezeRecordJson] = responseChecks.map((check) => {
      if ('json' in check) {
        return check.json;
      }
      throw new Error('Unexpected: response check missing json after error validation');
    });

    // Construct FrozenSnapshot object
    const snapshot: FrozenSnapshot = {
      company: companyJson,
      cells: cellsJson,
      roles: rolesJson,
      topology: topologyJson,
      methodology: methodologyJson,
      freeze_record: freezeRecordJson,
    };

    // MANDATORY: Validate using Authority validation
    const validationResult = validateFrozenSnapshot(snapshot);
    if (!validationResult.valid) {
      return {
        success: false,
        error: 'Snapshot validation failed',
        validationErrors: validationResult.errors.map((e) => ({
          field: e.field,
          message: e.message,
        })),
      };
    }

    // Transform to view models (naming only, no semantic changes)
    const viewModel = transformFrozenSnapshot(snapshot);

    return {
      success: true,
      data: viewModel,
    };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error loading snapshot',
    };
  }
}

/**
 * Load snapshot from a snapshot identifier
 * Constructs the snapshot directory path from the identifier
 */
export async function loadSnapshotById(
  frozenCompanyIdentifier: string,
  baseUrl: string = '/snapshots/authority'
): Promise<LoadSnapshotResult> {
  const snapshotDir = `${baseUrl}/${frozenCompanyIdentifier}`;
  return loadFrozenSnapshot(snapshotDir);
}

