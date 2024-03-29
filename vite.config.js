import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [
    react({
      include: "**/*.{jsx,tsx,js}",
    }),
  ],
  server: {
    port: 3000,
  },
  build: {
    outDir: "build",
    assetsDir: "static",
  },
});
