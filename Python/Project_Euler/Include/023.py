# --<{      Non-abundant sums       }>--
# --<{  Coded by Parker Cranfield   }>--
# --<{     September 16, 2020       }>--

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

global debug
debug = 0

def propDiv(num):
    divLst = []
    for i in range(1, num):
        if num % i == 0:
           divLst.append(i)
    return divLst

abundantLst = []
for i in range(1, 28124):
    if sum(propDiv(i)) > i:
        abundantLst.append(i)

nonAbundantNumSet = set([x for x in range(1, 28124)])

for j in range(len(abundantLst)):
    for k in range(j, len(abundantLst)):
        e = abundantLst[j] + abundantLst[k]
        if e > 28123:
            break
        else:
            if e in nonAbundantNumSet:
                nonAbundantNumSet.remove(e)

print(sum(nonAbundantNumSet))