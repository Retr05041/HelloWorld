# --<{   Longest Collatz sequence   }>--
# --<{  Coded by Parker Cranfield   }>--
# --<{       August 19, 2020        }>--

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),

it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

n = 1
longest_chain_so_far = 0
chain = [n]

while n < 1_000_000:
    if chain[-1] <= 1:
        if len(chain) > longest_chain_so_far:
            longest_chain_so_far = len(chain)
            print(f"{n} | {longest_chain_so_far}")
        chain.clear()
        n += 1
        chain.append(n)
        continue
    else:
        if chain[-1] % 2 == 0:
            chain.append(int(chain[-1]/2))
        else:
            chain.append(int(3*chain[-1] + 1))


