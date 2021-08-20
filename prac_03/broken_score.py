"""
Broken Score program from prac 3 CP1404
"""

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
elif score <= 100:
    print("Excellent")
else:
    print("Invalid score")
