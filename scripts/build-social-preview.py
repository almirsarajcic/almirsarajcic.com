#!/usr/bin/env python3
"""Outline the site's licensed fonts and export the website's social card.

Run with Python + fonttools[woff], after npm install (uses the existing sharp).
The copy/layout below is the editable master. Outlines avoid font substitution.
"""
from html import escape
from pathlib import Path
import subprocess

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "public/brand"
FONTS = ROOT / "assets/font-sources"
LABEL = "Almir Sarajčić — Software consultant. Building Kogen. Elixir, Phoenix and agentic development."


def text(value, x, y, size, weight="Regular", color="#15140f"):
    font = TTFont(FONTS / f"IBMPlexSans-{weight}.woff2")
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    paths = []
    for character in value:
        glyph = glyphs[cmap[ord(character)]]
        pen = SVGPathPen(glyphs)
        glyph.draw(pen)
        paths.append(f'<path transform="translate({x:.3f} {y}) scale({scale} {-scale})" d="{pen.getCommands()}"/>')
        x += glyph.width * scale
    if x > 1192:
        raise ValueError(f"Text exceeds the card's right safe margin: {value}")
    return f'<g aria-label="{escape(value)}" fill="{color}">' + "".join(paths) + "</g>"


svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640" role="img" aria-labelledby="title">'
    f'<title id="title">{escape(LABEL)}</title>'
    '<rect width="1280" height="640" fill="#f2f0ea"/>'
    + text("Almir Sarajčić", 88, 214, 84, "SemiBold")
    + text("Software consultant · Building Kogen", 88, 316, 44)
    + text("Elixir · Phoenix · Agentic development", 88, 382, 34, color="#55524a")
    + '<path d="M88 476H1192" stroke="#d3cfc4" stroke-width="2"/>'
    + text("almirsarajcic.com", 88, 548, 28, color="#8a4b1f")
    + '</svg>\n'
)
master = BRAND / "social-preview.svg"
output = BRAND / "social-preview-consultant-kogen.png"
master.write_text(svg)
subprocess.run([
    "node", "-e",
    "require('sharp')(process.argv[1]).png().toFile(process.argv[2]).catch(e=>{console.error(e);process.exit(1)})",
    str(master), str(output),
], cwd=ROOT, check=True)
print(output)
