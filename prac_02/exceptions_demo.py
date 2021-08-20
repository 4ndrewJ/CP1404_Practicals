try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if not denominator == 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# ValueError occurs when the input cannot be converted to int
# ZeroDivisionError occurs when denominator is 0 and program trys to divide by 0
# Could check whether the input == 0 rather than catching ZeroDivisionError
