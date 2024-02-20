import random

def price_matcher():
    # Select a random item and price from the lists
    random_item = random.choice(item)
    random_price = random.choice(price)

    free_change(random_item, random_price)

    return random_item, random_price
    
def free_change(random_item, random_price):
    print(random_item)
    change = 10 - random_price
    print(f"Your change for this order is {change}")


item = ["eggs", "beans", "cheese"]
price = [1.50, 2.25, 3.00]

price_matcher()
