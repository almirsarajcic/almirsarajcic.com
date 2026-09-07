# Cloudflare Pages deployment

[Project home](../README.md)

This is the maintained production workflow for `almirsarajcic.com`.

## Production definition

| Field | Value |
| --- | --- |
| Source | GitHub repository `almirsarajcic/almirsarajcic.com` |
| Framework | Astro, static output |
| Production provider | Cloudflare Pages |
| Canonical hostname | `almirsarajcic.com` |
| Alternate hostname | `www.almirsarajcic.com` → permanent redirect to apex |
| Build command | `npm run build` |
| Build output | `dist` |
| Runtime | Node.js 22.16.0, pinned in `.node-version` |

## Publish

Inputs: an approved source revision, the current canonical CV, access to the GitHub repository, and access to the Cloudflare account that owns the `almirsarajcic.com` zone.

1. Start in this repository and make sure the intended source revision is checked out.
2. Run `npm install`, `npm run check`, and `npm run build`.
3. Confirm `dist/index.html` exists and `dist/Almir_Sarajcic_CV.pdf` matches `public/Almir_Sarajcic_CV.pdf`.
4. In Cloudflare Pages, use the existing project for this repository. For first-time setup, connect the GitHub repository, select Astro, set the production branch to `master`, the build command to `npm run build`, and the output directory to `dist`. Cloudflare reads the pinned Node version from `.node-version`.
5. Enable automatic production deployments from `master` and set Preview branch deployments to **None**.
6. Push the checked revision to `master`. Cloudflare builds and deploys it automatically. Do not create a second Pages project or a separate GitHub Actions deployment.
7. Add `almirsarajcic.com` as the production custom domain in the Pages project. Add `www.almirsarajcic.com` to Cloudflare and configure a zone-level permanent redirect to the same path and query string on `https://almirsarajcic.com`.
8. Only after Cloudflare reports the domain active, retire the old GitHub Pages custom-domain configuration. Leave the last verified site serving until the Cloudflare deployment and certificate are ready.

## Checks

Completion requires all of the following:

1. `https://almirsarajcic.com/` returns the deployed Astro page over HTTPS.
2. `https://www.almirsarajcic.com/test?source=check` redirects once to `https://almirsarajcic.com/test?source=check`.
3. The home page has canonical URL `https://almirsarajcic.com/`, the intended title and description, and the retained Plausible script.
4. `/Almir_Sarajcic_CV.pdf` returns the canonical two-page PDF and matches the maintained JobHunt copy byte for byte.
5. Navigation, external links, email links, light/dark presentation, mobile layout, favicon/touch icons when present, and current social metadata are checked on the live host.

If DNS or certificate activation is still pending, keep the source and successful Pages deployment, record the exact Cloudflare status, and resume from custom-domain activation rather than changing hosts or projects.
