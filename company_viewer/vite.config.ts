import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // Server configuration for stable development experience
  server: {
    port: 5173,
    strictPort: false, // Allow port fallback if 5173 is in use
    host: true, // Allow external connections if needed
  },
})
