import os, sys

# Make sure this module is on the path regardless of where its imported from.
myDir = os.path.dirname(__file__)
sys.path.append(myDir)

# Grab all our submodules and include them whenever we include this package:
__all__ = [x.replace('.py','') for x in os.listdir(myDir)
	if x.endswith('.py') and not x.startswith('__')]

# Import of all the sub-modules:
for name in __all__: exec('import ' + name)