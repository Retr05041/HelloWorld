# --<{        Lattice paths         }>--
# --<{  Coded by Parker Cranfield   }>--
# --<{       August 19, 2020        }>--

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

from math import factorial

n = 20
print(int(factorial(2 * n) / (factorial(n) * factorial(n))))



"""
I had a hard time figureing out a formula for this, so I used one that has been created already, I understand it for the most part ::

To move from the top left corner of an n×n grid to the opposite one you have to move n times to the right and n times down. 
So in total you will do 2n moves. If you could make those in any order there would be (2n)! ways of doing them. 
But you don't have that freedom, because the order within the movements to the right and within the movements down is fixed, 
e.g. you have to move from row 4 to row 5 before you can move from row 5 to row 6. 
So of the n! ways the movements to the right can be ordered, only one is valid, and similarly with the movements down.

Summing it all up, the closed form answer to that problem is:

(2n)!/n!n!
"""