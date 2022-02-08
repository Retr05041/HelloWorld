# --<{    Sum square difference   }>--
# --<{ Coded by Parker Cranfield  }>--
# --<{      August 12, 2020       }>--

"""
The sum of the squares of the first ten natural numbers is,

            1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

            (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,

            3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_of_squares = []
square_of_sum = []

for i in range(101):
    f = i ** 2
    sum_of_squares.append(f)
    finale = sum(sum_of_squares)

print(finale)

for n in range(101):
    square_of_sum.append(n)
    u = sum(square_of_sum)
    total = u ** 2

print(total)

print(total - finale)