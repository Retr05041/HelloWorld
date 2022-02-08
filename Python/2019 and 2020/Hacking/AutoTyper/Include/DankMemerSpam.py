import keyboard
import time
print("AUTOTYPER READY -- PRESS 'esc' TO START")

keyboard.wait('esc')
print("INITIATE")

second_timer = 0

while 1:
    if second_timer % 45 == 0:
        keyboard.write("pls beg")
        keyboard.press_and_release('enter')
    if second_timer % 40 == 0:
        keyboard.write("pls hunt")
        keyboard.press_and_release('enter')
        keyboard.write("pls fish")
        keyboard.press_and_release('enter')    

    second_timer += 1
    time.sleep(1)


"""
beg = 45
hunt = 40
fish 40
"""