#!/usr/bin/env python


from __future__ import absolute_import
import sys
import pymake.parser

filename = sys.argv[1]
source = None

with open(filename, 'rU') as fh:
    source = fh.read()

statements = pymake.parser.parsestring(source, filename)
print(statements.to_source())
