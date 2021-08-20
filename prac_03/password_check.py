"""
Password check program from prac 3 CP1404
"""
MIN_LENGTH = 8


def main():
    """
    Tests get_password() and print_password_asterisks()
    """
    password = get_password()
    print_password_asterisks(password)


def print_password_asterisks(password):
    """
    Prints asterisks of same length as password
    """
    print('*' * len(password))


def get_password():
    """
    Prompts user for password until entered len(password) >= MIN_LENGTH
    Returns the password
    """
    password = input('Enter Password: ')
    while len(password) < MIN_LENGTH:
        print(f'Password must have length of at least {MIN_LENGTH}')
        password = input('Enter Password: ')
    return password


main()
