#!/usr/bin/env python3
#
# Python Workbook - 100 Exercises
# Exercise # NN
#
# Points Value: NN
# 
# Author: Daniel Raphael
#
# --------------------------------------------------------------------------------------------------------------------
#
# Create a script that dynamically generates a list of numbers from 1 to 20 and then prints it out to the console.
#
# --------------------------------------------------------------------------------------------------------------------

my_list = []
for i in range(1, 21):
    my_list.append(i)

print(my_list)
#
# # my_list is a list and therefore you need to use the .append method.
#
# Instructor's solution
#
# Exercise for reference:
#
# Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.
#
# Answer:
#
#     my_range = range(1, 21)
#     print(list(my_range))
#
# Explanation:
#
# range()  is a Python built-in function that generates a range of integers. However, range()  creates a Python range
# object. To get a real list object you need to use the list() function to convert the range object into a list object.