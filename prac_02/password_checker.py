"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 8
MAX_LENGTH = 32

MIN_LOWER = 2
MIN_UPPER = 2
MIN_DIGIT = 2
MIN_SPECIAL = 2

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

TOTAL_MIN_REQUIRED = MIN_LOWER + MIN_UPPER + MIN_DIGIT + MIN_SPECIAL
assert TOTAL_MIN_REQUIRED < MAX_LENGTH
if TOTAL_MIN_REQUIRED > MIN_LENGTH:
    MIN_LENGTH = TOTAL_MIN_REQUIRED


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    if MIN_UPPER > 0:
        print(f"\t{MIN_UPPER} or more uppercase characters")
    if MIN_LOWER > 0:
        print(f"\t{MIN_LOWER} or more lowercase characters")
    if MIN_DIGIT > 0:
        print(f"\t{MIN_DIGIT} or more numbers")
    if MIN_SPECIAL > 0:
        print(f"\tand {MIN_SPECIAL} or more special characters: {SPECIAL_CHARACTERS}")

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    length = len(password)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower < MIN_LOWER:
        return False
    if count_upper < MIN_UPPER:
        return False
    if count_digit < MIN_DIGIT:
        return False
    if count_special < MIN_SPECIAL:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
