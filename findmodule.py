#!/usr/bin/env python

__author__ = 'WangQiang'

import os
import sys
def findmodule():
	if len(sys.argv) != 2:
		print "Usage: %s modulename" % sys.argv[0]
		exit(1) 

	find_command = "find %s -iname '*%s*' 2> /dev/null" % (reduce(lambda s1, s2: s1 + ' ' + s2, sys.path), sys.argv[1])
	os.system(find_command)

if __name__ == '__main__':
	findmodule()
