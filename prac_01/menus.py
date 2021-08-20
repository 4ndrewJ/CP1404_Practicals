def main():
    name = input('Enter name: ')
    display_menu()
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'H':
            print('Hello ' + name)
        elif choice == 'G':
            print('Goodbye ' + name)
        else:
            print('Invalid Choice')
        display_menu()
        choice = input('>>> ').upper()
    print('Finished.')


def display_menu():
    print('(H)ello\n(G)oodbye\n(Q)uit')
    return


main()
