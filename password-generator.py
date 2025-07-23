from random import randint, choice
from string import ascii_letters, punctuation
from subprocess import call
from sys import executable, argv

print('Password generator by Shady, v2')

password = []

use_letters = input('Use Letters? (y/n) ').lower().strip() == 'y'
use_digits = input('Use Digits? (y/n) ').lower().strip() == 'y'
use_symbols = input('Use Symbols? (y/n) ').lower().strip() == 'y'

password_length = int(input('Password length: '))

for i in range(password_length):

    if use_letters == False and use_digits == False and use_symbols == True: #001
        password.append(choice(punctuation))

    elif use_letters == False and use_digits == True and use_symbols == False: # 010
        password.append(randint(0,9))

    elif use_letters == False and use_digits == True and use_symbols == True:   #011
        charType = randint(0, 1)
        if charType == 0:
            password.append(randint(0,9))
        elif charType == 1:
            password.append(choice(punctuation))

    elif use_letters == True and use_digits == False and use_symbols == False:   #100
        password.append(choice(ascii_letters))

    elif use_letters == True and use_digits == False and use_symbols == True:   #101
        charType = randint(0, 1)
        if charType == 0:
            password.append(choice(ascii_letters))
        elif charType == 1:
            password.append(choice(punctuation))

    elif use_letters == True and use_digits == True and use_symbols == False:   #110
        charType = randint(0, 1)
        if charType == 0:
            password.append(choice(ascii_letters))
        elif charType == 1:
            password.append(randint(0,9))

    elif use_letters == True and use_digits == True and use_symbols == True:   #111
        charType = randint(0, 2)
        if charType == 0:
            password.append(randint(0,9))
        elif charType == 1:
            password.append(choice(ascii_letters))
        elif charType == 2:
            password.append(choice(punctuation))

    elif use_letters == False and use_digits == False and use_symbols == False:

        restart = input('You decided that you don\'t need a password\nHave you changed your mind? (y/n) ').lower().strip() == 'y'

        if restart == True:
            subprocess.call([sys.executable] + sys.argv)
            sys.exit()
        else:
            print('OK, but remember - hackers never sleep 😈')

password_string = ' '.join(str(char) for char in password)
password_string = password_string.replace(' ', '')

print('\nYour password:', password_string)

exit = input('\nPress any key to exit... ')
