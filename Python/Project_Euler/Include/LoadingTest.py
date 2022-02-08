from tqdm import tqdm # For bar

for i in tqdm(range(int(9e6)), bar_format="{percentage:1.0f}%|{bar:50}{r_bar}"): # tqdm() is the command for bar - bar_format is there to make bar shorter but keep its look
    pass
