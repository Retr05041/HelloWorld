# V1.1 of brute force password
#imports
import itertools
import string
import time
import getpass
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
#so it doesnt close immidiatly
e = input("")