def main():
    lower_bound = int(input('Enter lower bound: '))
    upper_bound = int(input('Enter upper bound: '))
    sequence_type = get_menu_input()
    while sequence_type != 'Q':
        if sequence_type == 'E':
            print(' '.join(str(i) for i in range(lower_bound, upper_bound) if i % 2 == 0))
        elif sequence_type == 'O':
            print(' '.join(str(i) for i in range(lower_bound, upper_bound) if i % 2 == 1))
        elif sequence_type == 'S':
            print(' '.join(str(i) for i in range(lower_bound, upper_bound) if round(i**0.5) == i**0.5))
        else:
            print('Invalid Input')
        sequence_type = get_menu_input()


def get_menu_input():
    print('(E)ven\n(O)dd\n(S)quare\n(Q)uit')
    return input('>>> ').upper()


main()
