import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://almirsarajcic.com",
  output: "static",
  build: { inlineStylesheets: "always" },
});
