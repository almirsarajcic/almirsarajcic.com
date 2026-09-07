# Personal website redesign proposal

7 September 2026. Accepted for website and CV publication by Almir after private review. The initial trial and provenance below are retained as design history.

## Visual thesis

An editorial record of a working engineer: strong opening statement, quiet metadata, numbered project rows and consistent text columns. The fixed sidebar becomes a compact wrapping masthead. Kogen informs the IBM Plex type family, deliberate spacing and restrained structure; no Kogen mark or third-party portfolio artwork is repurposed as a personal logo.

The website designer received only Almir's own source and Kogen references. A separate Claude researcher saw ambrosino.io and returned general principles; the website designer did not receive that reference or its code. Approved copy and destinations remain in `src/pages/index.astro`.

## Owners and asset map

| Concern | Owner / deployment copy |
| --- | --- |
| Facts and wording | JobHunt `artifacts/cv/cv.json`, accepted career decisions and website/profile copy; page is a presentation of those owners |
| Page and content hierarchy | `src/pages/index.astro` |
| Personal visual tokens / reusable CSS | `src/styles/site.css` |
| Metadata, canonical, structured data and domain-gated analytics | `src/layouts/Base.astro` |
| Font masters used in this site | `assets/font-sources/IBMPlex*.woff2`; subset source in `src/assets/fonts/`, derived by `scripts/subset-fonts.py`; bundled license and `public/font-license.txt` |
| Website CV | `public/Almir_Sarajcic_CV.pdf` is the accepted IBM Plex CV, identical to JobHunt’s canonical application PDF |
| Private review integration | JobHunt `scripts/prepare-redesign-review.py` → existing career-review Sites project; no Sites identity in this production worktree |

Light tokens: paper #f2f0ea, ink #15140f, secondary #55524a, metadata #6b675e. Dark tokens: paper #14130f, ink #eeebe2, secondary #a8a496, metadata #928e81. Sienna accent is reserved for interactions. IBM Plex Sans carries headings/body; Mono carries metadata. Body is 16.5–18px; metadata/navigation is 14px. The spacing rhythm uses 8, 16, 24, 32, 48, 64 and 96px. Text enlargement can wrap long project names and email addresses. These are proposals owned by this stylesheet, not new accepted career rules.

## Checks and limitations

- `npm run check`: zero errors, warnings or hints. `npm run build`: successful Astro static output.
- Original outbound destinations and content were compared by Claude; punctuation discrepancies were reconciled with the original.
- Parent checked 320, 390, 768 and 1440px widths, dark mode at 390px, and 200% text enlargement at 390px: zero page-wide overflow. Mobile and tablet renders inspected. Tests use desktop Chromium viewport emulation, not a physical device.
- Claude's first narrow command-line screenshot appeared clipped; actual viewport measurements did not reproduce that overflow. Parent raised navigation/metadata from 13 to 14px and added explicit long-text wrapping/minimum grid widths.
- Source-derived contrast ratios were checked by Claude, which strengthened secondary labels for AA contrast.
- The Claude website agent exhausted its session allowance during final layout verification. Codex completed the bounded verification, small accessibility changes, this handoff and private Sites integration. No public deployment occurred.

## Refresh and promotion

Read repository README and `docs/deployment.md`. Run checks and build after source edits. The private redesign workflow in JobHunt owns rebasing assets and proposed PDF links. Do not copy preview-only metadata into production. After design acceptance, reconcile changes since base `bc144e4`, promote this branch through the production procedure, deliberately select/archive the canonical CV, and verify the live Cloudflare Pages website and PDF checksum. Until then, this worktree is the editable proposal; `master` and the public application PDF retain their approved state.

Publication preparation: minified inline CSS, Latin font subsets with original licensed masters retained, hashed asset caching, and the original A favicon were added after the initial Lighthouse audit. Current production sources are the main checkout; the original isolated branch is historical evidence. JobHunt’s publication receipt owns live measurements and checks.
