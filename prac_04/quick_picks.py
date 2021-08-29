from random import shuffle


NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    max_number_length = len(str(MAX_NUMBER))
    line_format = ('{:' + str(max_number_length) + '} ')*NUMBERS_PER_LINE
    number_of_lines = int(input('How many quick picks? '))
    for i in range(number_of_lines):
        line_to_print = pick_numbers()
        print(line_format.format(*line_to_print))


def pick_numbers():
    selectable_numbers = list(range(MIN_NUMBER, MAX_NUMBER+1))
    random_pick = []
    for i in range(NUMBERS_PER_LINE):
        shuffle(selectable_numbers)
        random_pick.append(selectable_numbers.pop())
    return random_pick


main()
