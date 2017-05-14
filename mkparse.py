#!/usr/bin/env python


from __future__ import absolute_import
import sys
import pymake.parser

for f in sys.argv[1:]:
    print("Parsing %s" % f)
    fd = open(f, 'rU')
    s = fd.read()
    fd.close()
    stmts = pymake.parser.parsestring(s, f)
    print(stmts)
