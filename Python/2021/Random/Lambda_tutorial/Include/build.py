# LAMBDA TUTORIAL
# Feb. 3, 2021

# https://www.w3schools.com/python/python_lambda.asp

"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

"lambda arguments : expression"
"""

x = lambda a : a + 10
print(x(5))

y = lambda b, c : b * c
print(y(5, 6))

"""
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""

def myfunc(n):
  return lambda z : z * n

"""
Use that function definition to make a function that always doubles the number you send in:
"""

mydoubler = myfunc(2)

print(mydoubler(11))

mytripler = myfunc(3)

print(mytripler(11))