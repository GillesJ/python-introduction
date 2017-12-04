#!/usr/bin/env python
# Note, updated version of 
# https://github.com/ipython/ipython-in-depth/blob/master/tools/nbjoin.py
"""
usage:

python nbjoin.py A.ipynb B.ipynb C.ipynb > joined.ipynb
"""

import io
import os
import sys

import nbformat

def join_notebooks(filenames):
    joined = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if joined is None:
            joined = nb
        else:
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            joined.cells.extend(nb.cells)
    if not hasattr(joined.metadata, 'name'):
        joined.metadata.name = ''
    joined.metadata.name += "_joined"
    print(nbformat.writes(joined))

if __name__ == '__main__':
    notebooks = sys.argv[1:]
    if not notebooks:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
        
    join_notebooks(notebooks)