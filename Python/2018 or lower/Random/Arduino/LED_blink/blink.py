# First Arduino Projects -- Arduino UNO
# Coded by Parker Cranfield -- June 30, 2019
# Makes Pin 13 blink, built in LED
# https://www.makeuseof.com/tag/program-control-arduino-python/

# IMPORTS
from pyfirmata import Arduino, util
from time import sleep

# VARIABLES
# gets board
board = Arduino("COM3")
# gets user input
loopTimes = input("How many times would you like the LED to blink: ")

# prints that it has started
print("Blinking " + loopTimes + " times.")

# loops as many times as user stated, prints * every time
# "digital[13]" is the built in pin LED, known as RX on some boards
# "board.digital[13].write(1)" | board = our board | digital[] = what "pin" (i think) | write() = i dont know
for x in range(int(loopTimes)):
    board.digital[13].write(1)
    print("*")
    sleep(0.2)
    board.digital[13].write(0)
    sleep(0.2)

# REMEMBERME: Press reset button when you want to rerun different code
# REMEMBERME: Run through command prompt
# FIXME: Arduino blinks 2x more than stated amount, no matter what time it takes
# NOTE: Try to make it so if you input a 1 the LED goes on and a 0 makes the LED turn off
