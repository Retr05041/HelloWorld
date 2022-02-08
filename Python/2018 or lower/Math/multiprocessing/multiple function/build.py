#### IMPORTS ####
from multiprocessing import Process 
import sys

rocket = 0

def func1(): # first function
    global rocket
    print("start func1")
    while rocket < 10: # sys.maxsize: (sets to systems max size) | maybe try setting max number to a hugher num and see how function 2 ends first
        rocket += 1
    print("end func1")

def func2(): # second function
    global rocket
    print("start func2")
    while rocket < 10: # sys.maxsize: (sets to systems max size)
        rocket += 1
    print("end func2")

if __name__=='__main__':
    p1 = Process(target=func1) # sets the process function to a variable with the target paramater = to the function without brakcets
    p1.start() # starts p1's process
    p2 = Process(target=func2)
    p2.start() # starts p2's process

# If you dont import Process from multiprocessing then you have to make sure to
# add the multiprocessing. before the Process() | rememeber to add a target
