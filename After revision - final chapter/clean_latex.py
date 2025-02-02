#!/usr/bin/env python
" A script to remove all temporary files in repo"
import os

remove_symbols = [
    "~",
    "#",
    ".pyc",
    ".aux",
    ".blg",
    ".fdb_latexmk",
    ".nav",
    ".snm" ".out",
    ".bbl",
    ".log",
    ".toc",
    ".vrb",
    ".fls",
    ".ilg",
    ".ind",
    ".out",
    ".thm",
    ".idx",
    "__latexindent_temp.tex",
    "eps-converted-to.pdf",
    ".synctex.gz",
]

remove = []

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if any(symbol in filename for symbol in remove_symbols):
            remove.append(os.path.join(dirpath, filename))

if remove:
    message = "Found %d files that will be removed:" % len(remove)
    print(message)
    print("-" * len(message))
    for filename in remove:
        print("  removing:", filename)
        os.unlink(filename)
else:
    print("\nNo temp files removed")
