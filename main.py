import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''


def check_numbers():
    while True:
        user_input = input("enter the desired length of your password: ")
        if user_input.isdigit():
            return int(user_input)
        print("error: please enter a positive integer.")


def use_digits():
    while True:
        choice = input('\nuse numbers in your password? y/n \n').lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print('\nenter y or n')


def use_lowercase_letters():
    while True:
        choice = input('\nuse lowercase letters in your password? y/n\n').lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print('\nenter y or n')


def use_uppercase_letters():
    while True:
        choice = input('\nuse uppercase letters in your password? y/n\n').lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print('\nenter y or n')


def use_punctuation():
    while True:
        choice = input('\nuse special characters in your password? y/n\n').lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print('\nenter y or n')


def use_ambiguous_symbols():
    while True:
        choice = input('\nshould ambiguous symbols be eliminated? y/n\n').lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print('\nenter y or n')


def password_options():
    global chars
    if use_digits():
        chars += DIGITS
    if use_lowercase_letters():
        chars += LOWERCASE_LETTERS
    if use_uppercase_letters():
        chars += UPPERCASE_LETTERS
    if use_punctuation():
        chars += PUNCTUATION
    if use_ambiguous_symbols():
        for i in chars:
            if i in 'il1Lo0O':
                chars = chars.replace(i, "")


def password_generate():
    result = ''.join(random.choices(chars, k=check_numbers()))
    print(f'your password: {result}')


if __name__ == '__main__':
    password_options()
    password_generate()
