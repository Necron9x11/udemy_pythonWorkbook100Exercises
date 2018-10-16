#!/usr/bin/env python3
#
# Python Workbook - 100 Exercises
# Exercise # NN
#
# Points Value: NN
# 
# Author: Daniel Raphael
#
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
from pprint import pprint

# solution 1 (answer)
d1 = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))
pprint(d1)

# solution 2 (brackets)
d2 = {'a': list(range(1, 11)), 'b': list(range(11, 21)), 'c': list(range(21, 31))}
pprint(d2)

# solution 3 (for loop)
r = range(1, 31)
keys = ['a', 'b', 'c']
d3 = {}
for p in range(0, 3):
    d3[keys[p]] = list(r[10*p:10*(p+1)])
pprint(d3)

# solution 4 (dict comprehension)
r = range(1, 31)
keys = ['a', 'b', 'c']
d4 = {str(keys[p]): list(r[10*p:10*(p+1)]) for p in range(0, 3)}
pprint(d4)
