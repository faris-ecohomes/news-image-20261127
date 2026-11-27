#!/usr/bin/env python3
"""news-image-20261127 entry program.

The entry image is the checked-in poster.png beside this file: a one-page
newspaper summary of world news from Friday 27 November 2026, drawn in code
with PIL at build time. This program only copies it to the output directory.

No network, no rendering, no writes outside $MAKEFUN_OUTPUT_DIR, no
dependence on time, randomness, or environment beyond the output dir.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "poster.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
