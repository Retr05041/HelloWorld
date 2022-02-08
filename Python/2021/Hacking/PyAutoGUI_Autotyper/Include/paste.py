import pyautogui
from time import sleep

sleep (5)

while 1:
    pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
    pyautogui.press('enter')

    sleep(3)


