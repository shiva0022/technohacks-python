import random

letters: str = 'abcdefghijklmnopqrstuvwxyz'
cap_letters: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers: str = '0123456789'
symbols: str = "~`! @#$%^&*()_-+={[}]|\\:;\"'<,>.?/"

print('Welcome to python password generator!\n')
print('\nFor making your password strong consider the following :')
print('''
  !Password must contain 8 - 14 characters
  !Password must contain both upper case and lower case characters
  !Password must contain at-least one numeric and one special symbol
''')

no_of_letters: int = int(input('How many letters would you like to have in your password : '))
no_of_cap_letters: int = int(input('How many capital letters would you like to have in your password : '))
no_of_numbers: int = int(input('How many numbers would you like to have in your password : '))
no_of_symbols: int = int(input('How many symbols would you like to have in your password : '))

summ: int = no_of_numbers + no_of_cap_letters + no_of_letters + no_of_symbols

if summ < 8:
    print('\nlength for the password is too short !!!')
    print('Please try again by setting more number of characters\n')
else:
    password: list[str] | str = []
    password += random.sample(letters, no_of_letters)
    password += random.sample(cap_letters, no_of_cap_letters)
    password += random.sample(numbers, no_of_numbers)
    password += random.sample(symbols, no_of_symbols)

    random.shuffle(password)
    password = ''.join(password)

    print()
    print(password)
