import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

declare var __dirname: string;

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: "../backend/static",
    emptyOutDir: true,
    sourcemap: true
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')  // '@' points to 'src' directory
    }
  }
})
