import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      // Use source files for development (Vite handles TypeScript)
      '@ai-workbench/authority': path.resolve(__dirname, '../packages/authority/src/index.ts'),
    },
    // Ensure Vite resolves workspace packages correctly
    dedupe: ['@ai-workbench/authority'],
  },
  optimizeDeps: {
    include: ['@ai-workbench/authority'],
    // Force pre-bundling of the authority package
    force: true,
  },
  // Ensure Vite can handle TypeScript in node_modules/workspace packages
  server: {
    fs: {
      // Allow serving files from workspace root
      allow: ['..'],
    },
  },
})

