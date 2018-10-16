#!/usr/bin/env python3
#
# Python Workbook - 100 Exercises
# Exercise # NN
#
# Points Value: NN
# 
# Author: Daniel Raphael
#
# Question: List slicing is important in various data manipulation activities. Let's do a few more exercises on that.
#
# Please complete the script so that it prints out the first three items of list letters.
#
#   letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#
# Expected output:
#
# ['a', 'b', 'c']

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(letters[:3])

# Again, indexing is zero indexed, hence we start at "0" (zero is inferred when the starting index is left blank), and
# upper bound exclusive, hence a "3" for the upper bound.

