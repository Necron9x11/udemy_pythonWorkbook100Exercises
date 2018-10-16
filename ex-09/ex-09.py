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
#  Question: Complete the script so that it prints out a list slice containing the last three items of list letters .
#
#     letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#
# Expected output:
#
# ['h', 'i', 'j']
#
# ---------------------------------------------------------------------------------------------------------------------

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(letters[-3:])

# Again negative indexing. Again shorthand indexing notation.
#
# Instructor states: When you don't put any index to the right of the colon everything is included
#  and upper-bound exclusivity is ignored.
