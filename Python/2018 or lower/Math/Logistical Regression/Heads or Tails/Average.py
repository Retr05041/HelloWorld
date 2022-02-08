import numpy as np

def flip_coin():
    # Simulate flipping a coin.
    # Returns
    # -------
    # str
    #     "H" for heads/ "T" for tails.
    flip = np.random.binomial(1, .5, 1)
    # binomial(n, p, size=None)
    # Parameters
    # ----------
    # n: int or array_like of ints
    #   >=0
    #
    # p: - p: float or array_like of floats
    #   >= 0 and <=1, porbability of n==True
    #
    # size: list
    #   how long the list is
    if flip[0] == 1:
        side = "H"
    else:
        side = "T"
    return side

def flip_condition(stop_condition=['H', 'T'], print_opt=False):
    # Flip coin until flip pattern is met.
    # Parameters
    # ----------
    # stop_condition: list
    #     The sequence of flips to be matched before flipping stops.
    #
    # print_opt: bool
    #     Option to print the sequence of flips.
    #
    # Returns
    # -------
    # int
    #     The number of flips it took to match the pattern.
    flip_list = []

    current_index = 0
    current_condition = None
    while current_condition != stop_condition:
        flip_list.append(flip_coin())
        if len(flip_list) >= len(stop_condition):
            current_condition = [flip_list[i] for i in range(current_index - len(stop_condition) +1 , current_index + 1)]
        else:
            pass
        current_index +=1

    if print_opt:
        print(flip_list)
    return current_index

average_h = np.mean([flip_condition(['H']) for i in range(1000)])
average_t = np.mean([flip_condition(['T']) for i in range(1000)])


print("Average # of flips to flip a head again: {}".format(average_h))
print("Average # of flips to flip a head again: {}".format(average_t))
