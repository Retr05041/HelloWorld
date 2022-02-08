# Speed Optimization with Numpy | Useing numpy==1.20.0

# https://numpy.org/doc/stable/reference/

# https://towardsdatascience.com/one-simple-trick-for-speeding-up-your-python-code-with-numpy-1afc846db418

"""
There’s a couple of points we can follow when looking to speed things up:

If there’s a for-loop over an array, there’s a good chance we can replace it with some built-in Numpy function

If we see any type of math, there’s a good chance we can replace it with some built-in Numpy function
"""

# IMPORTS
import time
import numpy as np

# REGULAR WAY
start_time = time.time()

num_multiplies = 5_000_000
data = range(num_multiplies) # Makes a range object from 0-5_000_000, altho if you print it you need to put it in list() to see the list correctly
number = 1

for i in data: # cycles through 0 -> 5_000_000
    number *= 1.0000001 # Makes it longer and longer to calculate
    # print(f"{number}", end="\r", flush=True)

end_time = time.time()

print(number)
print(f"Run time : {end_time - start_time}")

# desetup clock
start_time = 0
end_time = 0

"""
We’ve done something very simple: we saw that we had a for-loop in which we were repeating the same mathematical operation many times. 
That should trigger immediately that we should go look for a Numpy function that can replace it.
We found one — the power function which simply applies a certain power to an input value. The dramatically sped of the code to run in 7.6293e-6 seconds
"""

# NUMPY WAY
start_time = time.time()

num_multiplies = 5_000_000_000
data = range(num_multiplies)
number = 1

number *= np.power(1.0000001, num_multiplies) # this multiplies 

end_time = time.time()

print(number)
print(f"Run time : {end_time - start_time}")