# --<{       10001st prime        }>--
# --<{ Coded by Parker Cranfield  }>--
# --<{      August 13, 2020       }>--

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = []
a = 2

while 1:
    if len(primes) >= 10_001:
        break
    else:
        if all(a % i for i in range(2, a)) == True:
            primes.append(a)
            a += 1
        else:
            a += 1


print(max(primes))