# --<{  Graphing the numeric chain useing a formula }>---
# --<{          Coded by: Parker Cranfield          }>---
# --<{               Sep. 17, 2020                  }>---

"""

ALGORITHM

n = n/2 (n is even)

n = 3n+1 (n is odd)
"""

import matplotlib.pyplot as plt # graph
from time import time # time it

def createChain(num): # takes num
    chain = [num] # makes an list with starting num as num
    tic = time() # starts timer
    while chain[-1] != 1: # makes sure the final obj in list is not 1 - else do calculation on num and append to list
        if num % 2 == 0:
            num = num/2
            chain.append(num)
        else:
            num = 3*num+1
            chain.append(num)
    toc = time() # stop timing
    timeSpent = toc-tic # calc time spent
    return chain, timeSpent # return var

calculate, time = createChain(13) # set variables for return of function
plt.xlabel("Chain Index", fontsize = 14, color = "red") # set graph xlabel
plt.ylabel("Number in Chain", fontsize = 14, color = "red") # set graph ylabel
plt.plot(calculate) # graph line of list
plt.axis([0, len(calculate), 0, max(calculate)]) # set max hight and width of graph
plt.show() # show graph
print(f"{calculate} | {time}") # print hard copy