"""
Shop calculator first takes the number of items and the cost of each item
then displays the total price of the items
10% discount applied for total costs > $100
"""

total_price = 0
number_items = int(input('Number of items: '))
while number_items < 0:
    print('Invalid number of items!')
    number_items = int(input('Number of items: '))
for i in range(number_items):
    item_price = float(input('Price of item: '))
    total_price += item_price
if total_price > 100:
    total_price *= 0.9
print('Total price for {:.0f} items is ${:.2f}'.format(number_items, total_price))
