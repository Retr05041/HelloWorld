# --<{      Smallest multiple     }>--
# --<{ Coded by Parker Cranfield  }>--
# --<{      August 12, 2020       }>--

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

num = 2
small_poss_num = 1

start_time = time.time()

while 1:
    if num > 20:
        break
    elif small_poss_num % num == 0:
        # print(f"{num} | {small_poss_num}")
        num += 1
    else:
        small_poss_num += 1
        num = 2

end_time = time.time()

print(small_poss_num)
print(f"Run time : {end_time-start_time}")

# 87.5211341381073 seconds