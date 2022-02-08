#Password Checker V1.2
#Brute force 
#imports
import os
import sys
import time
import itertools
import string
import time
import getpass

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
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    os.system('cls')
    #title
    f = open("title.txt", "r")
    print(f.read())
    # getting the passoword or passphrase
    pas = getpass.getpass("Put password here(it will not be shown): ")
    #main
    def guess_password(real):
        chars = string.printable #if you want it to start a "aaaaa" etc then put "string.ascii_lowercase in front"
        attempts = 0
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=len(pas)):
                attempts += 1
                guess = ''.join(guess)
                if guess == real:
                    return 'password is {}. found in {} guesses.'.format(guess, attempts)
                print(guess, attempts)

    print(guess_password(pas))


    
    #Try again?
    e = input("Do you want to Try another password?y/n: ")
    if e == "y" or e == "Y":
        again()
    elif e == "n" or e == "N":
        exit()



def again(): # for doing it again
    os.system('cls')
    #title
    f = open("title.txt", "r")
    print(f.read())
    # getting the passoword or passphrase
    pas = getpass.getpass("Put password here(it will not be shown): ")
    #main
    def guess_password(real):
        chars = string.printable #if you want it to start a "aaaaa" etc then put "string.ascii_lowercase in front"
        attempts = 0
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=len(pas)):
                attempts += 1
                guess = ''.join(guess)
                if guess == real:
                    return 'password is {}. found in {} guesses.'.format(guess, attempts)
                print(guess, attempts)

    print(guess_password(pas))



    #Try again? pt2
    e = input("Do you want to Try another password?y/n: ")
    if e == "y" or e == "Y":
        again()
    elif e == "n" or e == "N":
        exit()



#If pass and username doesnt match
main()
