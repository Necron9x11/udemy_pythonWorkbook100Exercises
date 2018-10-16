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
# Question: Complete the script so that it produces the expected output. Please use my_range  as input data.
#
#     my_range = range(1, 21)
#
#  Expected output:
#
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
#
# ---------------------------------------------------------------------------------------------------------------------

my_range = range(1, 21)
# my_range = list(my_range)
#
# for num in my_range:
#     my_range[num-1] = num*10
# print(my_range)

my_range = [(num * 10) for num in my_range]
print(my_range)

# I did not think of using list comprehension syntax until I saw the hint at the bottom of the exercise page and even
#  then I could not quite recall the syntax. I had my_range = [num in num in my_range] at first. Don;t know why I
#  spaced the "for". Likely because I have been up all night. No sleep = diminishing returns. :/

# Instructor's solution:
#
# my_range = range(1,21)
# print([10 * x for x in my_range])
