#Password Checker V1.2
#Brute force 
#imports
import os
import time
import itertools
import string
import time
import getpass



#Must Access this to continue.
def main():
    while True:
        UserName = input ("Enter Username: ")
        PassWord = input ("Enter Password: ")

        if UserName == 'abc' and PassWord == '123':
            time.sleep(1)
            print ("Login successful!")
            logged()

        elif UserName != 'abc' or PassWord != '123':
            print("Username/Password did not match!")



#Password checking
def logged():
    time.sleep(1)
    print("PASSWORD CHECKER 3000...")
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
        logged()
    elif e == "n" or e == "N":
        exit()




#If pass and username doesnt match
main()