#---<{ Smallest number devided by 1-x }>---
#---<{           May 25, 2020         }>---
#---<{   Coded By: Parker Cranfield   }>---

"""
This is version 2 of the smallest divisable number.. please see the last one to see what will be happening

I plan to make it so the num_to_be_checked will start at 1 and go up 1
if num_to_be_checked % iterations != 0
that way we can change the iteration to find the smallest number that can be divisable by a range of 1-x
"""
check_lst = []

num_to_be_checked = 1
iterations = 10

while 1:
    if iterations >= 1:
        if num_to_be_checked % iterations == 0:
            print("POSITIVE : " + str(iterations))
            iterations -= 1
            check_lst.append("POSITIVE")
            continue
        else:
            print("NEGATIVE : " + str(iterations))
            iterations -= 1
            continue
    else:
        print("ITERATIONS DONE")
        print(check_lst)
        print(iterations)
        if len(check_lst) < 10:
            num_to_be_checked += 1
            iterations = 10
            continue
        else:
            break

# NEEDS WORK



