# --<{ Special Pythagorean triplet }>--
# --<{  Coded by Parker Cranfield  }>--
# --<{       August 14, 2020       }>--

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for i in range(1, 1000):
    for n in range(i+1, 1000):
        for j in range(n+1, 1000):
            f_product = i**2 + n**2
            if f_product == j**2:
                s_product = i + n + j
                if s_product == 1000:
                    final = i*n*j
                    print(f"a = {i} | b = {n} | c = {j} --- {s_product} -- {final}")
                    exit()


