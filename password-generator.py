from random import randint, choice
from string import ascii_letters, punctuation
from subprocess import call
from sys import executable, argv

def no_password():
    while True:
        restart = input('You decided that you don\'t need a password\nHave you changed your mind? (y/n) ').lower().strip()
        if restart in ['y', 'n']:
            restart = (restart == 'y')
            break
        print("Please enter only 'y' or 'n'\n")

    if restart == True:
        subprocess.call([sys.executable] + sys.argv)
        sys.exit()
    else:
        print('\nOK, but remember - hackers never sleep 😈')

print('\033[1mPassword generator by Shady, v3\033[0m\n')

password = []

use_letters = 0
use_digits = 0
use_symbols = 0

while True:
    use_letters = input('Use Letters? (y/n) ').lower().strip()
    if use_letters in ['y', 'n']:
        use_letters = (use_letters == 'y')
        break
    print("Please enter only 'y' or 'n'\n")

while True:
    use_digits = input('Use Digits? (y/n) ').lower().strip()
    if use_digits in ['y', 'n']:
        use_digits = (use_digits == 'y')
        break
    print("Please enter only 'y' or 'n'\n")

while True:
    use_symbols = input('Use Symbols? (y/n) ').lower().strip()
    if use_symbols in ['y', 'n']:
        use_symbols = (use_symbols == 'y')
        break
    print("Please enter only 'y' or 'n'\n")

while True:
    try:
        password_length = int(input('\nPassword length: '))
        break
    except ValueError:
        print('Please enter only the number')

if password_length > 0:
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

        elif use_letters == False and use_digits == False and use_symbols == False: #000
            no_password()
            break

    password_string = ' '.join(str(char) for char in password)
    password_string = password_string.replace(' ', '')

else: no_password()

if use_letters or use_digits or use_symbols:
    if password_length > 0:
        print('\nYour password:', password_string)

input("\nPress Enter To Exit... ")
