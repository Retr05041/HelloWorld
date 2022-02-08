# --<{    Largest prime factor   }>--
# --<{ Coded by Parker Cranfield }>--
# --<{       July 27, 2020       }>--

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600_851_475_143 ?
"""

primes = []
num = 600_851_475_143
prime_check = 2

while 1:
    if num < prime_check:
        break
    elif num % prime_check == 0:
        primes.append(prime_check)
        num = num/prime_check
        prime_check = 2
    else:
        prime_check += 1

print(max(primes))

