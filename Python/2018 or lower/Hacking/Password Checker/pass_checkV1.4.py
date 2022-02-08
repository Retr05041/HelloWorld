import os
import sys
import time
import itertools
import string
import time
import getpass
import keyboard



#Login info
a = ["parker", "cranfield"]

#Must Access this to continue.
def main():
    while True:
        UserName = input ("Enter Username: ")
        PassWord = input ("Enter Password: ")

        if UserName == a[0] and PassWord == a[1]:
            time.sleep(1)
            print ("Login successful!")
            logged()

        elif UserName != a[0] or PassWord != a[1]:
            print("Username/Password did not match!")


#Password checking
def logged():
    #making the clear and loading
    time.sleep(1)
    os.system('cls')
    #title
    f = open("title.txt", "r")
    print(f.read())
    print("(Password will not be shown -- This program uses all printable options -- press ctrl+shift+e to cancel)")
    # getting the passoword or passphrase
    pas = getpass.getpass("Put password here: " )
    #main
    def guess_password(real):
        chars = string.printable
        attempts = 0
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=len(pas)):
                attempts += 1
                guess = ''.join(guess)
                #To cancel
                if keyboard.is_pressed("ctrl+shift+e"):
                    logged()
                # shows attempts every 100,000,000
                if (attempts % 100000==0):
                    print(guess, attempts)
                if guess == real:
                    return 'password is {}. found in {} guesses.'.format(guess, attempts)
                    # if you want to see it work then put "print(guess, attempts)" here

    print(guess_password(pas))

    #Try again?
    e = input("Do you want to Try another password? ")
    if e == "y" or e == "Y" or e == "yes" or e == "Yes":
        logged()
    elif e == "n" or e == "N" or e == "no" or e == "No":
        os.system('cls')
        print("Ok")
        time.sleep(2)
        exit()


#If pass and username doesnt match
main()