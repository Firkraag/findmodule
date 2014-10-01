#!/usr/bin/env python

__author__ = 'WangQiang'

import os
import sys
	
if len(sys.argv) < 2:
	print "Usage: %s modulename..." % sys.argv[0]
	exit(1) 

for modulename in sys.argv[1:]:
	find_command = "find %s -iname '*%s*' 2> /dev/null" % (reduce(lambda s1, s2: s1 + ' ' + s2, sys.path), modulename)
	print 'module ' + modulename + ':'
	os.system(find_command)
	print

