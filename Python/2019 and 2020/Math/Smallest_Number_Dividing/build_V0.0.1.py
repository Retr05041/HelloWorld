#---<{ Smallest number devided by 1-x }>---
#---<{           May 25, 2020         }>---
#---<{   Coded By: Parker Cranfield   }>---

"""
This program will check if a number is divisable through 1-x, ex. 1-10

so.. if we wanted to check 100, we would devide 100 by every number 1-10 and if its divisable
then we add it to the list!

Lets start
"""

num_to_be_checked = 2520
iterations = 10

while 1:
    if iterations >= 1:
        if num_to_be_checked % iterations == 0:
            print("POSITIVE : " + str(iterations))
            iterations -= 1
            continue
        else:
            print("NEGATIVE : " + str(iterations))
            iterations -= 1
            continue
    else:
        print("ITERATIONS DONE")
        break



