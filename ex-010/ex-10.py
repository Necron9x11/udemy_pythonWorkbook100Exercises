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
# Question: Complete the script so that it prints out a list slice containing letters a, c, e, g, and i.
#
#     letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#
# Expected output:
#
# ['a', 'c', 'e', 'g', 'i']
# ---------------------------------------------------------------------------------------------------------------------

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(letters[0:10:2])


# Pretty self explanatory, but basically the three numbers in the list reference in the print statement are:
#
# start:stop:step
#
# So the indices we end up generating are:
#
#  0, 2, 4, 6, 8
#
# which happens to be "a", "c", "e", "g", and "i"
#
# of course we ought to have use the shorthand form if we were nto so blamed exhausted: [::2}
