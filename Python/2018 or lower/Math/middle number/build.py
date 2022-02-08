#
#
#   Script that you put in 3 diff. numbers and it tells you the middle one
#
#   Made by Parker Cranfield
#   Feb 16 2019
#
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))


if a < b and a > c or a < c and a > b :
    print(str(a) + " is the middle number")


if b < a and b > c or b < c and b > a :
    print(str(b) + " is the middle number")


if c < a and c > b or c < b and c > a :
    print(str(c) + " is the middle number")
