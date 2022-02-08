# --<{     Summation of primes     }>--
# --<{  Coded by Parker Cranfield  }>--
# --<{       August 18, 2020       }>--

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

num = 2_000_000

lst = set([i for i in range(2, num+1)])

n = 2
print("LIST CREATED")


while n*n <= num:
    for j in range(n*n, num+1, n):
        if j in lst:
            lst.remove(j)
        else:
            continue
    print(f"FINISHED THE {n} MULTIPLES")
    n+=1


print(sum(lst))





