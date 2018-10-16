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
# Question: Complete the script so it generates the expected output using my_range  as input data. Please note that
#  the items of the expected list output are all strings.
#
#     my_range = range(1, 21)
#
#  Expected output:
#
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
#
# ---------------------------------------------------------------------------------------------------------------------

my_range = range(1, 21)

# print([str(x) for x in my_range])


# Ok so I used list comprehension (above) but then the hint when I scrolled down said to use the map function.
# So I looked up map in the interactive consoles help, but I was using map(str(), *iterator) instead of
# map(str, *iterator) at first and had to take a peek at how to call map properly. Never used it before now. But then
# in the comments the instructor said the list comprehension was a valid answer Grr... Then again, I learned something
# new and cool. So excellent!

print(list(map(str, my_range)))

# Or you could also use f-string notation in 3.6:
# print([f"{x}" for x in range(1,21)])
# I am using 3.5.2 atm. 3.6.4 is installed, but it is under pyenv control and pycharm is not currently seeing it
# properly for some reason. Not something I want to sort out just this minute.


# or if he had not wanted a list as the displayed output format, this works as well:
# for num in map(str, my_range):
#     print(num)







