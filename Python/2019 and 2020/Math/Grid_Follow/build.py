# --<{  FIND ALL THE PATHS OF A X,X GRID | TOP LEFT TO BOTTOM RIGHT }>--
# --<{                         CODED BY : Robotix                   }>--
# --<{       PROJECT FOUND ON : https://projecteuler.net/about      }>--
# updated by : Parker Cranfield
# formula used to solve
# https://math.stackexchange.com/questions/286437/arrangement-of-binary-bits


# IMPORTS
import math, time # takes math and time

# MAIN
def Path_Counter(Grid_Size): # takes the size of a grid
    formula = math.factorial(Grid_Size*2) / (math.factorial(Grid_Size)**2) # formula
    return formula

# START
if __name__ == "__main__":
    size = input("Size of grid (must be even) : ")
    Tic = time.process_time()
    Check = Path_Counter(int(size))
    Toc = time.process_time()
    Elapsed_time = Toc-Tic
    print(str(Check) + " found in " + str(Elapsed_time) + " seconds")