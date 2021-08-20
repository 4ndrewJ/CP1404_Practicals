MIN_LENGTH = 8

password = input('Enter Password: ')
while len(password) < MIN_LENGTH:
    print(f'Password must have length of at least {MIN_LENGTH}')
    password = input('Enter Password: ')
print('*'*len(password))
