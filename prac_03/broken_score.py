"""
Broken Score program from prac 3 CP1404
"""
from random import randrange


def main():
    score = float(input("Enter score: "))
    score_description = get_score_description(score)
    print(score_description)

    score = randrange(0, 101)
    score_description = get_score_description(score)
    print(score_description)


def get_score_description(score):
    if score < 0 or score > 100:
        score_description = "Invalid score"
    elif score < 50:
        score_description = "Bad"
    elif score < 90:
        score_description = "Passable"
    else:
        score_description = "Excellent"
    return score_description


main()
