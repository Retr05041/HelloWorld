# --<{      Reciprocal cycles       }>--
# --<{  Coded by Parker Cranfield   }>--
# --<{     September 29, 2020       }>--

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from decimal import *

def get_cycle(num):
    ######## NOT MY CODE ########
    cycle_length = 0
    list_of_remainders = []
    x = 1
    while True:
        if x % num == 0:
            break
        elif x in list_of_remainders:
            break
        list_of_remainders.append(x)
        x = (x*10) % num
        cycle_length += 1
    return cycle_length
#########################################

def main():
    d = 1000
    longest_cycle = 0
    longest_cycle_denom = 0
    for i in range(2, d+1):
        if get_cycle(i) > longest_cycle:
            longest_cycle = get_cycle(i)
            longest_cycle_denom = i
    return longest_cycle_denom

print(main())