import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''


def check():
    while True:
        user_input = input("enter number: ")
        if user_input.isdigit():
            return int(user_input)
        print("error: please enter a positive integer.")


def numbers():
    while True:
        choice = input('\nuse numbers in password? y/n\n').lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print('\nenter y or n')


def password_options():
    check()
    numbers()


if __name__ == '__main__':
    password_options()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
