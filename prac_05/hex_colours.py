"""
CP1404/CP5632 Practical
Hex codes for colours in a dictionary
"""

COLOUR_NAME_TO_HEX = {'aliceblue': '#f0f8ff', 'blueviolet': '#8a2be2', 'cadetblue': '#5f9ea0',
                      'chocolate': '#d2691e', 'coral': '#ff7f50', 'darkgreen': '#006400',
                      'darkorange': '#ff8c00', 'darkorchid': '#9932cc', 'darkslategray': '#2f4f4f',
                      'firebrick': '#b22222'}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_NAME_TO_HEX:
        print(f'Hex Code: {COLOUR_NAME_TO_HEX[colour_name]}')
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
