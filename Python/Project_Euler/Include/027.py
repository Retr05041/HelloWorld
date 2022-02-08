# --<{       Quadratic primes        }>--
# --<{  Coded by Parker Cranfield    }>--
# --<{       February 03, 2021       }>--

"""
Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39. However, when n=40, 40^2+40+41 = 40(40+1)+41 is divisible by 41, and certainly when
n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2-79n+1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|<=1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |-4|=4 
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""
from primesieve import primes # Prime Generator | make primes() into a list
import numpy as np

primes = list(primes(87400))

# NOT MY CODE - Edited from C
def isPrime(testNumber):
    i = 0
    while primes[i] <= testNumber:
        if primes[i] == testNumber:
            return True
        i += 1
    return False

aMax = 0
bMax = 0
nMax = 0
 
for a in range(-1000, 1001):
    for b in range(-1000, 1001): 
        n = 0
        while isPrime(np.absolute(n * n + a * n + b)):
            n += 1

        if n > nMax:
            aMax = a
            bMax = b
            nMax = n

print(f"aMax : {aMax} | bMax : {bMax} | Product of the coefficients : {aMax*bMax}")