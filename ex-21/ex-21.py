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
# Question: Filter the dictionary by removing all items with a value of greater than 1.
#
#     d = {"a": 1, "b": 2, "c": 3}
#
# Expected output:
#
# {'a': 1}
#
# ---------------------------------------------------------------------------------------------------------------------

# Well, I had done List Comprehensions before, but never dictionary comprehensions, so I had to go look them up.
# I got the answer. Does that count as full credit, or half because I had to go use a book?? :-)

d = {"a": 1, "b": 2, "c": 3}
d = {key: value for key, value in d.items() if value <= 1}
print(d)

# Instructors Solution:

# NOTE: The instructor used dict() but I just used the { } syntax which, far as I know so far, does the dame thing.
# It's like the [ ] notation for list comprehensions.

# Exercise for reference:
#
# Filter the dictionary by removing all items with a value of greater than 1.
#
#     d = {"a": 1, "b": 2, "c": 3}
#
# Answer:
#
#     d = {"a": 1, "b": 2, "c": 3}
#     d = dict((key, value) for key, value in d.items() if value <= 1)
#     print(d)
#
# Explanation:
#
# Here we're using a dictionary comprehension. The comprehension is the expression inside dict() .
# The comprehension iterates through the existing dictionary items and if an item is less than or
# equal to 1,the item is added to a new dict.
#
# This new dict is assigned to the existing variable d so we end up with a filtered dictionary in d.


