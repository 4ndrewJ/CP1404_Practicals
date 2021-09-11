from prac_06.guitar import Guitar


def main():
    print('My guitars!')
    guitars = []
    new_guitar = get_new_guitar()
    while new_guitar is not None:
        guitars.append(new_guitar)
        print(f'{new_guitar.name} ({new_guitar.year}) : ${new_guitar.cost:,.2f} added.\n')
        new_guitar = get_new_guitar()
    print('\nThese are my guitars:')
    for i, guitar in enumerate(guitars, 1):
        vintage_string = '(vintage)' if guitar.is_vintage() else ''
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_new_guitar():
    """
    Asks user for guitar information, returns guitar object
    returns None if '' entered for name
    """
    name = input('Name: ')
    if name == '':
        return
    year = int(input('Year: '))
    cost = float(input('Cost: '))
    return Guitar(name, year, cost)


main()
