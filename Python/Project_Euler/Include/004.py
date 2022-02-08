# --<{ Largest palindrome product }>--
# --<{ Coded by Parker Cranfield  }>--
# --<{      August 12, 2020       }>--

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

biggest_pal = []

for i in range(999, 99, -1):
    for n in range( 999, 99, -1):
        s = i*n
        f = str(s)
        f = f[::-1]
        f = int(f)
        if s == f:
            biggest_pal.append(s)

print(max(biggest_pal))
