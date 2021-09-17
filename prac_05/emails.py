"""
CP1404/CP5632 Practical
Get and store name and email
"""


def main():
    """
    Get user input of names and emails
    Stores and displays the names and emails
    """
    name_to_email = {}
    email = input('Email: ')
    while email != '':
        name = find_name_from_email(email)
        if input(f'Is your name {name}? (Y/n) ').lower() in ['n', 'no']:
            name = input('Name: ')
        name_to_email[name] = email
        email = input('Email: ')
    print()
    display_names_and_emails(name_to_email)


def display_names_and_emails(name_to_email):
    """
    Display the names and emails in the dictionary name_to_email
    """
    for name_and_email in name_to_email.items():
        print('{} ({})'.format(*name_and_email))


def find_name_from_email(email):
    """
    Find the section of email commonly used for names
    Returns full name (each name seperated by '.' in email) in title case
    """
    return ' '.join(name.title() for name in email.split('@')[0].split('.'))


if __name__ == '__main__':
    main()
