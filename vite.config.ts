import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

// The dev server is reached through the sandbox preview proxy
// (https://<port>-<sandbox>.e2b.app), so it must bind to 0.0.0.0 and accept
// that host instead of rejecting it via Vite's host allowlist.
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: true,
    strictPort: false,
  },
  preview: {
    host: '0.0.0.0',
    port: 4173,
    allowedHosts: true,
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./vitest.setup.ts'],
    include: ['src/**/*.{test,spec}.{ts,tsx}'],
    restoreMocks: true,
    clearMocks: true,
    unstubEnvs: true,
    unstubGlobals: true,
  },
});
