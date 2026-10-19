food_prices={
    "Butter Chicken": 350.00,
    "Paneer Tikka Masala": 280.00,
    "Veg Dum Biryani": 220.00,
    "Garlic Naan": 45.00,
    "Chocolate Sizzler": 180.00
}
for item, price in food_prices.items():
    if price > 200:
        print(item)