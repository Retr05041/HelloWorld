# ---<{    The Josephus Problem    }>---
# ---<{        Nov. 3, 2020        }>---
# ---<{ Coded By: Parker Cranfield }>---

"""
The Josephus Problem is a mathematical problem in which a circle is made, its circumference formed of (n) people.

Starting from the person in the 0th position, each person eliminates the person to their left (the next person in the circle). 
The next living person then does the same, and the process is repeated until there is only one person left alive..

Find the position (index - starting from 0) of the last man standing for a circle of n people.

----------------------------------------------------------------------------------------------------------------------------------
What I want to do:

Call a function that takes (n) as the number of people in the circle, then tells you what spot you should be in to survive
"""

n = 10

people = list(i for i in range(n))

while len(people) >= 2:
    print(people)
    for n in people[::2]:
        print(n)
        people.remove(n)


            

print(people)