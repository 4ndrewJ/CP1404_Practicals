from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU_TEXT = 'q)uit, c)hoose taxi, d)rive'


def main():
    print('Let\'s drive!')

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print(MENU_TEXT)
    selected_option = get_menu_input()
    while selected_option != 'q':
        if selected_option == 'd':
            if current_taxi is not None:
                drive_distance = int(input('Drive how far? '))
                current_taxi.start_fare()
                current_taxi.drive(drive_distance)
                print(f'Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}')
                total_bill += current_taxi.get_fare()
            else:
                print('You need to choose a taxi before you can drive')

        elif selected_option == 'c':
            print('Taxis available:')
            display_taxis(taxis)
            taxi_number_choice = int(input('Choose taxi: '))
            if taxi_number_choice < len(taxis):
                current_taxi = taxis[taxi_number_choice]
            else:
                print('Invalid taxi choice')

        else:
            print('Invalid option')

        print(f'Bill to date: ${total_bill:.2f}')
        print(MENU_TEXT)
        selected_option = get_menu_input()

    print(f'Total trip cost: ${total_bill:.2f}')
    print('Taxis are now:')
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


def get_menu_input():
    return input('>>> ').lower()


main()
