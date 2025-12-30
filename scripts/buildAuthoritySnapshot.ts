#!/usr/bin/env ts-node

/**
 * Authority Snapshot Builder
 * 
 * Authority: docs/authority/*_FROZEN_001.md
 * 
 * This script generates a frozen snapshot bundle from Design-Time Draft data.
 * 
 * Usage:
 *   ts-node scripts/buildAuthoritySnapshot.ts <input-draft.json> <output-dir>
 */

import * as fs from 'fs';
import * as path from 'path';
import {
  validateFrozenSnapshot,
  type FrozenSnapshot,
  type Company,
  type Cell,
  type Role,
  type Relationship,
  type Methodology,
  type FreezeRecord,
} from '../packages/authority/src';

// UUID generation (simple implementation to avoid external dependency)
function generateUUID(): string {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0;
    const v = c === 'x' ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}
import {
  validateFrozenSnapshot,
  type FrozenSnapshot,
  type Company,
  type Cell,
  type Role,
  type Relationship,
  type Methodology,
  type FreezeRecord,
} from '../packages/authority/src';

// ============================================================================
// Input Types (Design-Time Draft format)
// ============================================================================

interface DraftCompany {
  id: string;
  name: string;
  description: string;
  createdAt?: string;
  createdBy?: string;
}

interface DraftCell {
  id: string;
  name: string;
  responsibilityWhat: string;
  responsibilityWhatNot: string;
  roles?: DraftRole[];
}

interface DraftRole {
  id: string;
  name: string;
  constraintType: 'allow' | 'forbid' | 'condition';
  description: string;
}

interface DraftRelation {
  id: string;
  sourceCellId: string;
  targetCellId: string;
  type: 'dependency' | 'reference' | 'input_output';
  description?: string;
}

interface DraftMethodology {
  name: string;
  description?: string;
}

interface DraftData {
  company: DraftCompany;
  cells: DraftCell[];
  relations: DraftRelation[];
  methodology?: DraftMethodology;
}

// ============================================================================
// Conversion Functions
// ============================================================================

function generateFrozenCompanyIdentifier(): string {
  return `FROZEN-COMP-${generateUUID()}`;
}

function generateFreezeRecordIdentifier(): string {
  return `FREEZE-${generateUUID()}`;
}

function generateMethodologyIdentifier(): string {
  return `METH-${generateUUID()}`;
}

function convertCompany(draft: DraftCompany, frozenBy: string): Company {
  const frozenAt = new Date().toISOString().replace(/\.\d{3}Z$/, 'Z');
  const frozenCompanyId = generateFrozenCompanyIdentifier();

  return {
    company_identifier: frozenCompanyId,
    company_name: draft.name,
    company_description: draft.description,
    frozen_at: frozenAt,
    frozen_by: frozenBy,
  };
}

function convertCells(draftCells: DraftCell[]): Cell[] {
  return draftCells.map((draft) => ({
    cell_identifier: draft.id.startsWith('CELL-') ? draft.id : `CELL-${draft.id}`,
    cell_name: draft.name,
    responsibility_what: draft.responsibilityWhat,
    responsibility_what_not: draft.responsibilityWhatNot,
    role_constraints: draft.roles?.map((r) => r.id.startsWith('ROLE-') ? r.id : `ROLE-${r.id}`) || [],
  }));
}

function convertRoles(draftCells: DraftCell[]): Role[] {
  const roles: Role[] = [];
  draftCells.forEach((cell) => {
    if (cell.roles) {
      cell.roles.forEach((draftRole) => {
        roles.push({
          role_identifier: draftRole.id.startsWith('ROLE-') ? draftRole.id : `ROLE-${draftRole.id}`,
          role_name: draftRole.name,
          constraint_type: draftRole.constraintType,
          constraint_description: draftRole.description,
          attached_to_cell_identifier: cell.id.startsWith('CELL-') ? cell.id : `CELL-${cell.id}`,
        });
      });
    }
  });
  return roles;
}

function convertTopology(draftRelations: DraftRelation[]): Relationship[] {
  return draftRelations.map((rel) => ({
    relationship_identifier: rel.id.startsWith('REL-') ? rel.id : `REL-${rel.id}`,
    source_cell_identifier: rel.sourceCellId.startsWith('CELL-') ? rel.sourceCellId : `CELL-${rel.sourceCellId}`,
    target_cell_identifier: rel.targetCellId.startsWith('CELL-') ? rel.targetCellId : `CELL-${rel.targetCellId}`,
    relationship_type: rel.type,
    relationship_description: rel.description,
  }));
}

function convertMethodology(draft?: DraftMethodology): Methodology {
  if (!draft) {
    return {
      methodology_identifier: generateMethodologyIdentifier(),
      methodology_name: 'Default',
    };
  }

  return {
    methodology_identifier: generateMethodologyIdentifier(),
    methodology_name: draft.name,
    methodology_description: draft.description,
  };
}

function createFreezeRecord(
  frozenCompanyId: string,
  frozenAt: string,
  frozenBy: string,
  draftId?: string,
  freezeSummary?: string
): FreezeRecord {
  return {
    freeze_record_identifier: generateFreezeRecordIdentifier(),
    frozen_company_identifier: frozenCompanyId,
    frozen_at: frozenAt,
    frozen_by: frozenBy,
    freeze_summary: freezeSummary,
    draft_identifier: draftId,
  };
}

// ============================================================================
// Snapshot Generation
// ============================================================================

function buildSnapshot(draftData: DraftData, frozenBy: string, freezeSummary?: string): FrozenSnapshot {
  const company = convertCompany(draftData.company, frozenBy);
  const cells = convertCells(draftData.cells);
  const roles = convertRoles(draftData.cells);
  const topology = convertTopology(draftData.relations);
  const methodology = convertMethodology(draftData.methodology);
  const freeze_record = createFreezeRecord(
    company.company_identifier,
    company.frozen_at,
    company.frozen_by,
    draftData.company.id,
    freezeSummary
  );

  const snapshot: FrozenSnapshot = {
    company,
    cells,
    roles,
    topology,
    methodology,
    freeze_record,
  };

  // Validate before returning
  const validationResult = validateFrozenSnapshot(snapshot);
  if (!validationResult.valid) {
    const errors = validationResult.errors.map((e) => `${e.field}: ${e.message}`).join('\n');
    throw new Error(`Snapshot validation failed:\n${errors}`);
  }

  return snapshot;
}

// ============================================================================
// File I/O
// ============================================================================

function writeSnapshot(snapshot: FrozenSnapshot, outputDir: string): void {
  const snapshotDir = path.join(outputDir, snapshot.company.company_identifier);

  // Create directory
  if (!fs.existsSync(snapshotDir)) {
    fs.mkdirSync(snapshotDir, { recursive: true });
  }

  // Write individual JSON files
  fs.writeFileSync(
    path.join(snapshotDir, 'company.json'),
    JSON.stringify(snapshot.company, null, 2),
    'utf-8'
  );

  fs.writeFileSync(path.join(snapshotDir, 'cells.json'), JSON.stringify(snapshot.cells, null, 2), 'utf-8');
  fs.writeFileSync(path.join(snapshotDir, 'roles.json'), JSON.stringify(snapshot.roles, null, 2), 'utf-8');
  fs.writeFileSync(
    path.join(snapshotDir, 'topology.json'),
    JSON.stringify(snapshot.topology, null, 2),
    'utf-8'
  );
  fs.writeFileSync(
    path.join(snapshotDir, 'methodology.json'),
    JSON.stringify(snapshot.methodology, null, 2),
    'utf-8'
  );
  fs.writeFileSync(
    path.join(snapshotDir, 'freeze_record.json'),
    JSON.stringify(snapshot.freeze_record, null, 2),
    'utf-8'
  );

  // Write manifest.json
  const manifest = {
    snapshot_id: snapshot.company.company_identifier,
    frozen_company_identifier: snapshot.company.company_identifier,
    frozen_at: snapshot.company.frozen_at,
    frozen_by: snapshot.company.frozen_by,
    schema_bundle_version: '001',
  };

  fs.writeFileSync(path.join(snapshotDir, 'manifest.json'), JSON.stringify(manifest, null, 2), 'utf-8');

  console.log(`✓ Snapshot written to: ${snapshotDir}`);
  console.log(`✓ Frozen Company Identifier: ${snapshot.company.company_identifier}`);
}

// ============================================================================
// CLI
// ============================================================================

function main(): void {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.error('Usage: ts-node buildAuthoritySnapshot.ts <input-draft.json> <output-dir> [frozen-by] [freeze-summary]');
    process.exit(1);
  }

  const [inputFile, outputDir, frozenBy = 'system', freezeSummary] = args;

  // Read input
  if (!fs.existsSync(inputFile)) {
    console.error(`Error: Input file not found: ${inputFile}`);
    process.exit(1);
  }

  const draftData: DraftData = JSON.parse(fs.readFileSync(inputFile, 'utf-8'));

  // Build snapshot
  try {
    const snapshot = buildSnapshot(draftData, frozenBy, freezeSummary);
    writeSnapshot(snapshot, outputDir);
    console.log('✓ Snapshot generation completed successfully');
  } catch (error) {
    console.error('Error generating snapshot:', error);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

export { buildSnapshot, writeSnapshot };

