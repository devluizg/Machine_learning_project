import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  // O site é publicado em https://devluizg.github.io/Machine_learning_project/.
  base: '/Machine_learning_project/',
  plugins: [react()],
  test: {
    environment: 'node',
    include: ['src/**/*.test.ts'],
  },
});
