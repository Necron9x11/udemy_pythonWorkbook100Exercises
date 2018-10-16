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
# Instructor's code is:
# d = {"Name": "John", "Surname": "Smith"}
# print(d["Smith"])
#
# This throws an error when run:
#
# Traceback (most recent call last):
#  File "<pyshell#32>", line 1, in <module>
#   print(d["Smith"])
# KeyError: 'Smith'
# >>>
#
# *** Explain why this is ***
# ---------------------------------------------------------------------------------------------------------------------

# It is because "Smith" is a dictionary item, not a key. Access it print(d["Surname"])

d = {"Name": "John", "Surname": "Smith"}
print(d["Surname"])

# Instructor's Answer:
# Exercise for reference:
#
#     d = {"Name": "John", "Surname": "Smith"}
#     print(d["Smith"])
#
# Answer:
#
# There is no key Smith  in the dictionary. Smith  is a value. You want to use Surname  if you want to access Smith :
#
#     print(d["Surname"])
#
# Explanation:
#
# A KeyError always means Python could not find a key with the name shown next to KeyError (e.g. Smith ).


