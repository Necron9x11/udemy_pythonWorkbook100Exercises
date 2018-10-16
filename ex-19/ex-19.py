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
#
# Question: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.
#
#     d = {"a": 1, "b": 2}
#
# Expected output:
#
#   {'a': 1, 'c': 3, 'b': 2}
#
# ---------------------------------------------------------------------------------------------------------------------

d = {"a": 1, "b": 2}

d.setdefault("c", 3)


print(d)

# NOTE: My solution differs, but I was taught that te way I did it, versus the instructor's solution, is the best
# way to add a key as setdefault will check if the key you are adding already exists and will simply do nothing if this
# is the case. So you save the exception handling as well as using less lines of code for the add.  win/win.

# Instructor's Solution

# Exercise for reference:
#
# Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.
#
#     d = {"a": 1, "b": 2}
#
# Answer:
#
#     d = {"a": 1, "b": 2}
#     d["c"] = 3
#     print(d)
#
# Explanation:
#
# Adding pairs of keys and values is straightforward as you can see. Note though that you cannot fix the order of the
# dictionary items. Dictionaries are unordered collections of items.
