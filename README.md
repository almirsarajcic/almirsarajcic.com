# almirsarajcic.com

Source for Almir Sarajčić’s public portfolio and career website. The approved page is built with Astro as a static site and published at [almirsarajcic.com](https://almirsarajcic.com).

## Start here

| Need | Location |
| --- | --- |
| Edit the public page | [`src/pages/index.astro`](src/pages/index.astro) |
| Replace the downloadable CV | [`public/Almir_Sarajcic_CV.pdf`](public/Almir_Sarajcic_CV.pdf) |
| Preview locally | Run `npm install`, then `npm run dev` |
| Verify a production build | Run `npm run check` and `npm run build` |
| Publish or change domains | [Cloudflare Pages workflow](docs/deployment.md) |

## Current state

The Astro migration preserves the approved content, layout, responsive behavior, dark theme, metadata, Plausible analytics, CV URL, and canonical apex domain. Cloudflare Pages is the selected production host. Pushes to `master` deploy through Cloudflare’s GitHub integration; branch previews are disabled.

## Folder map

- `src/pages/` — authored site pages.
- `public/` — files copied unchanged to the built site, including the CV.
- `docs/` — maintained production and domain workflow.
- `dist/` — generated production output; not committed.

Career copy and the canonical application CV are maintained in the adjacent JobHunt workspace. Update those owners first when facts or positioning change, then synchronize this repository and verify the public result.
