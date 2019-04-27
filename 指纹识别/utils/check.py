import sys

PYVERSION = sys.version.split()[0]

if PYVERSION < "3":
    exit('[-]Python Version Need >= 3.')
