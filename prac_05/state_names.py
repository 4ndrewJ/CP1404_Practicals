"""
CP1404/CP5632 Practical
State names in a dictionary
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all states and names
max_code_length = max(len(code) for code in CODE_TO_NAME)
for code in CODE_TO_NAME:
    print(f'{code:{max_code_length}} is {CODE_TO_NAME[code]}')
