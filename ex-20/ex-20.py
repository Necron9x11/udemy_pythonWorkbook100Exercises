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
# Question: Calculate the sum of all dictionary values.
#
#     d = {"a": 1, "b": 2, "c": 3}
#
# Expected output:
#
#  6
#
# ---------------------------------------------------------------------------------------------------------------------

d = {"a": 1, "b": 2, "c": 3}
sum_x=0
for key in d.keys():
     sum_x = sum_x + d[key]
 print(sum_x)

# I got loops on the brain this morning... Instructors solution is way more Pythonic. 

# print([sum(x)for x in d.keys])

# Instructor's Solution
#
# Exercise for reference:
#
# Calculate the sum of all dictionary values.
#
#     d = {"a": 1, "b": 2, "c": 3}
#
# Answer:
#
#     d = {"a": 1, "b": 2, "c": 3}
#     print(sum(d.values()))
#
# Explanation:
#
# d.values()  returns a list-like dict_values  object while the sum  function calculates the sum of the dict_values items.

