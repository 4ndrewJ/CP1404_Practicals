"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def print_data(data):
    max_len_subject = max(len(line[0]) for line in data)
    max_len_lecturer = max(len(line[1]) for line in data)
    max_len_number_of_students = max(len(str(line[2])) for line in data)
    for line in data:
        print(f'{line[0]:{max_len_subject}} is taught by '
              f'{line[1]:{max_len_lecturer}} and has '
              f'{line[2]:{max_len_number_of_students}} students')


main()
