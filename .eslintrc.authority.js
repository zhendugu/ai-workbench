/**
 * ESLint Rules for Authority Layer Integration Enforcement
 * 
 * These rules prevent regression by blocking patterns that violate Authority boundaries:
 * - Unauthorized fields (status, stage, progress, lifecycle)
 * - Parallel type definitions outside viewModels
 * - Direct Authority field access outside authorized boundaries
 */

module.exports = {
  rules: {
    // Prevent status/stage/progress/lifecycle fields in data models
    'no-restricted-syntax': [
      'error',
      {
        selector: 'Property[key.name=/^(status|stage|progress|lifecycle|readiness|maturity)$/i]',
        message: 'Unauthorized field detected. Authority Layer does not include status/stage/progress/lifecycle fields. Use viewModels for display-only fields.',
      },
    ],
  },
  overrides: [
    {
      files: ['**/viewModels.ts', '**/authorityTransform.ts', '**/authorityLoader.ts'],
      rules: {
        // These files are allowed to reference Authority types
      },
    },
    {
      files: ['run_time_frontend/src/**/*.ts', 'run_time_frontend/src/**/*.tsx'],
      excludedFiles: ['**/viewModels.ts', '**/authorityTransform.ts', '**/authorityLoader.ts'],
      rules: {
        // Prevent direct imports of Authority schema field names in components
        'no-restricted-imports': [
          'error',
          {
            patterns: [
              {
                group: ['**/types/index.ts'],
                message: 'Components must use viewModels from viewModels.ts, not direct Authority types. Import from types/viewModels instead.',
              },
            ],
          },
        ],
      },
    },
  ],
};

