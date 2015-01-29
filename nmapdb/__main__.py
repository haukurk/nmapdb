#!/usr/bin/env python
"""
The main entry point. Invoke as nmapdb or python -m nmapdb.
"""

from nmapdb import main
import sys, os

def default():
	main(sys.argv, os.environ)
	sys.exit(0)
	
if __name__ == '__main__':
	main(sys.argv, os.environ)
	sys.exit(0)