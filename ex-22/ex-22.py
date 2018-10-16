#!/usr/bin/env python3
#
# USES PYTHON 3.6 f-print NOTATION
# Points Value: 2
# 
# Author: Daniel Raphael
#
# ---------------------------------------------------------------------------------------------------------------------
#
# Create a dictionary with three keys: a, b, and c. Assign each key's value a list containing ten integers, beginning
# with 1, ending with thirty, spread across the three lists sequentially in even amounts. So dict["a"] == [1-10],
# dict["b"] == [11-20] and dict["c"] = [21-30]
#
# ---------------------------------------------------------------------------------------------------------------------

import pprint

# Option One:

dict01 = {}

a = [i for i in range(1, 11)]
dict01.setdefault("a", a)

b = [i for i in range(11, 21)]
dict01.setdefault("b", b)

c = [i for i in range(21, 31)]
dict01.setdefault("c", c)

print("Dict01:")
pprint.pprint(dict01)


# Option Two:

dict02 = {"a": list(range(1, 11)), "b": list(range(11, 21)), "c": list(range(21, 31))}

print('\nDict02:')
pprint.pprint(dict02)

# Option Three:

dict03 = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))

print('\nDict03:')
pprint.pprint(dict03)




# Option Four:

dict04 = {}

a = []
b = []
c = []

for i in range(1, 31):
    if i <= 10:
        a.append(i)
    if 11 <= i <= 20:
        b.append(i)
    if 21 <= i <= 30:
        c.append(i)

dict04.setdefault("a", a)
dict04.setdefault("b", b)
dict04.setdefault("c", c)

print('\nDict04:')
# TODO: pprint output is vertical and not horizontal for list b-c but not list a if list a-c not pre-defined - why???
pprint.pprint(dict04)


# r = range(1, 31)
# key = ["a", "b", "c"]
# key_group = range(1, 3)  # There are three keys, each with a list of ten items as a value. 3 groups of 10 = 30...
# dict =  for


# Instructor's Solution

# Exercise for reference:
#
# Create a dictionary of keys a, b, c where each key has as value a list from  1 to 10, 11 to 20, and 21 to 30
# respectively.Then print out the dictionary in a nice format.
#
# Answer:
#
# from pprint import pprint
#
# d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))
# pprint(d)
#
# Explanation:
#
# We're using ranges here to construct the lists. We're also using the built - in Python pprint module which is used
# to print out well formatted views of data types in Python.
