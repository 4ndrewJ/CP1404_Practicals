import random


"""
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""

# Line 1, smallest 5, largest 20
# Line 2, smallest 3, largest 9, couldnt produce even num such as 4
# Line 3, smallest possible 2.5, largest possible 5.5

# Random number not integer
print(random.uniform(1, 100))
