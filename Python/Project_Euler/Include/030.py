# --<{      Digit fifth powers       }>--
# --<{  Coded by Parker Cranfield    }>--
# --<{        March 04, 2021         }>--

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

counter_num = 2
flag = False
hold = 0
answer = 0

def split_num(x):
    y = str(x)
    z = [int(char) for char in y]
    return z

while 1:
    test_num = split_num(counter_num)
    for num in test_num:
        hold = hold + num**5
    if hold == counter_num:
        flag = True
        answer += counter_num
    if flag == True:
        print(f"{counter_num} | {test_num} | {answer}")
        flag = False
    counter_num += 1
    hold = 0
    
        