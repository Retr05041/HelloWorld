# ---<{ Graphing the fib Sequnce Until a Certain Index  }>---
# ---<{         Coded by: Parker Cranfield              }>---
# ---<{             Sep. 17, 2020                       }>---

"""
I wanna create a graph that shows the exponential growth of the sequence until a certain index

lets start
"""

import matplotlib.pyplot as plt # graph
from time import time # timer

def createSequence(num): # takes index at witch to stop
    fibSequence = [] # holds sequence
    # starts calculating - please take time to understand how i calculated each num
    a = 0 
    b = 1
    tic = time() # start timer
    while (len(fibSequence)+1) <= num: # stops at desired index
        fibSequence.append(a)
        c = a + b
        a = b
        b = c
    toc = time() # stops timer
    timeSpent = toc-tic # calc timeSpent
    return fibSequence, timeSpent # returns sequence and time

sequence, time = createSequence(20) # holds both returned values for createSequence with an index of 20
plt.ylabel("Number", fontsize=14, color="red") # creates y axis labels
plt.xlabel("Bib Index", fontsize=14, color="red") # creates x axis labels
plt.plot(sequence) # plots the sequence list
plt.axis([0, len(sequence), 0, max(sequence)]) # sets x and y to fit entire sequence
plt.show() # shows graph
print(f"{sequence} |  {time}") # hard copy