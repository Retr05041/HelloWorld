import keyboard
from tqdm import tqdm
import time

num = 0

while 1:
    if keyboard.is_pressed("enter"):
        for i in tqdm(range(int(num)), bar_format="{percentage:1.0f}%|{bar:50}{r_bar}"):
            pass
        exit()

    if keyboard.is_pressed("up"):
        num += 1
        time.sleep(0.1)
        print(num, end="\r", flush=True)
    elif keyboard.is_pressed("down"):
        num -=1
        time.sleep(0.1)
        print(num, end="\r", flush=True)
    else:
        continue