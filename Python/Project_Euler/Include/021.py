# --<{      Amicable numbers        }>--
# --<{  Coded by Parker Cranfield   }>--
# --<{     September 03, 2020       }>--

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10_000.
"""

def allPropDiv(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

count = 1

lst = [0]

while max(lst) < 10_000:
    if count == allPropDiv(allPropDiv(count)):
        if allPropDiv(count) != allPropDiv(allPropDiv(count)):
            lst.append(count)
            count += 1
        else:
            count += 1
    else:
        count += 1

lst.remove(lst[-1])
print(lst)
print(sum(lst))
