#!/usr/bin/env ts-node

/**
 * Negative Test: Invalid Authority Payload Rejection
 * 
 * This test verifies that Authority validation correctly rejects invalid payloads
 * with unauthorized fields (e.g., "status" field in Company).
 */

import * as fs from 'fs';
import * as path from 'path';
// Import from built package (or source if not built)
// In test environment, we can import from source
// Import validation function
// Note: In production, this would import from built package
// For testing, we import from source (requires TypeScript compilation)
// Alternative: Use require() for CommonJS if package is built
try {
  var { validateFrozenSnapshot } = require('../packages/authority/dist/validate.js');
} catch (e) {
  // Fallback: If package not built, use direct import (requires ts-node/tsx)
  var { validateFrozenSnapshot } = require('../packages/authority/src/validate');
}

const invalidSnapshotPath = path.join(__dirname, 'invalid_snapshot_with_status.json');

console.log('=== Negative Test: Invalid Authority Payload Rejection ===\n');

// Load invalid snapshot (contains unauthorized "status" field)
const invalidSnapshot = JSON.parse(fs.readFileSync(invalidSnapshotPath, 'utf-8'));

console.log('Invalid snapshot loaded:');
console.log(`  Company has unauthorized field: ${invalidSnapshot.company.status ? 'YES (status: ' + invalidSnapshot.company.status + ')' : 'NO'}`);
console.log('');

// Attempt validation
console.log('Running validateFrozenSnapshot()...');
const result = validateFrozenSnapshot(invalidSnapshot);

if (result.valid) {
  console.error('❌ TEST FAILED: Validation should have rejected the invalid snapshot');
  console.error('   Snapshot with unauthorized "status" field was accepted');
  process.exit(1);
} else {
  console.log('✅ TEST PASSED: Validation correctly rejected invalid snapshot');
  console.log(`   Validation errors: ${result.errors.length}`);
  console.log('');
  console.log('Validation errors:');
  result.errors.forEach((error, index) => {
    console.log(`  ${index + 1}. ${error.field}: ${error.message}`);
  });
  
  // Check that the error mentions the unauthorized field
  const hasStatusError = result.errors.some(e => 
    e.message.includes('status') || 
    e.message.includes('Unknown fields') ||
    e.field.includes('status')
  );
  
  if (hasStatusError) {
    console.log('');
    console.log('✅ Confirmed: Error correctly identifies unauthorized "status" field');
    process.exit(0);
  } else {
    console.log('');
    console.warn('⚠️  Warning: Error does not explicitly mention "status" field');
    console.warn('   Validation still correctly rejected, but error message could be clearer');
    process.exit(0);
  }
}

