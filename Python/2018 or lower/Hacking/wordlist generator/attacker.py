# Made by Parker Cranfield
import os


a = input('Password: ')
c = open('wl.txt', 'r')
txt = c.read()



if a in txt:
    print('Password found' + '\n')
    e = input("again? y/n: ")
    if e == "y" or e == "Y":
		os.system('python file.py')

else:
    print("Password Not found")
    e = input("")
    if e == "n" or e == "N":
    	exit()




