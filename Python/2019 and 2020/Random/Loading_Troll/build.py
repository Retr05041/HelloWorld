from tqdm import tqdm # For bar
from time import sleep

def calculateTime(time):
    time = time**2
    return time

for i in tqdm(range(int(100)), bar_format="{percentage:1.0f}%|{bar:50}{r_bar}"): # tqdm() is the command for bar - bar_format is there to make bar shorter but keep its look
    sleep(calculateTime(1))

