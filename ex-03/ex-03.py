#
#
# Question: Executing the code will throw an error. Can you explain why?

a = 1
b = 2
print(a == b)
print(b == c)

#
# In the 4th line, variable c is undefined so the code will throw a NameError.
#
# Ran it in the interpreter on the CLI so I could add the output that proves my answer.
#
# @>>> a = 1
# @>>> b = 2
# @>>> print(a == b)
# False
# @>>> print(b == c)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'c' is not defined
#


