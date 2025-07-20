from random import randint, choice
from string import ascii_letters, punctuation

password = []

password_length = int(input('Password length: '))

for i in range(password_length):
    charType = randint(0, 2)
    if charType == 0:
        password.append(randint(0,9))
    elif charType == 1:
        password.append(choice(ascii_letters))
    elif charType == 2:
        password.append(choice(punctuation))

password_string = ' '.join(str(char) for char in password)
password_string = password_string.replace(' ', '')

print('\nYour password:', password_string)

exit = input('\nPress any key to exit... ')