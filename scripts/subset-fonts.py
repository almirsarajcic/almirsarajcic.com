#!/usr/bin/env python3
"""Derive Latin webfonts from licensed masters. Requires fontTools[woff].
Run from any directory; commit outputs. The normal Astro build needs no Python.
"""
from pathlib import Path
from fontTools import subset
ROOT = Path(__file__).resolve().parents[1]
# Latin/Latin Extended, combining accents, punctuation, currencies and arrows.
UNICODES = 'U+0000-024F,U+0300-036F,U+1E00-1EFF,U+2000-206F,U+20A0-20CF,U+2100-214F,U+2190-21FF,U+FFFD'
for source in (ROOT/'assets/font-sources').glob('*.woff2'):
    options = subset.Options()
    options.flavor = 'woff2'
    options.layout_features = ['*']
    font = subset.load_font(str(source), options)
    worker = subset.Subsetter(options=options)
    worker.populate(unicodes=subset.parse_unicodes(UNICODES))
    worker.subset(font)
    target = ROOT/'src/assets/fonts'/source.name
    subset.save_font(font, str(target), options)
    print(source.name, source.stat().st_size, '->', target.stat().st_size)
