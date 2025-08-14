# Menu [category, item, price]
menu = [
    ["Fried Chicken", "Honey Soy Chicken", 32.99],
    ["Fried Chicken", "Fried Chicken", 29.99],
    ["Fried Chicken", "Hot Spicy Chicken", 30.99],
    ["Fried Chicken", "Soy Garlic Chicken", 30.99],
    ["Chicken Bowls", "Seasoned Chicken Bowl", 24.99],
    ["Chicken Bowls", "Honey Soy Chicken Bowl", 25.99],
    ["Burgers", "Chicken Burger", 20.99],
    ["Sides", "Chips", 9.99],
    ["Sides", "Hotdog", 6.90]
]

# Display menu with numbers
def display_menu():
    print("Menu:")
    for i, item in enumerate(menu, 1):
        print(f"  {i}. {item[1]}: ${item[2]:.2f}")

# Calculate total
def calculate_total(order):
    total = 0
    for item in order:
        total += item[1] * item[2]  # price * quantity
    return total

# Main program
order = []
display_menu()  # Show menu once

# Combo-eligible items
combo_items = ["Honey Soy Chicken", "Fried Chicken", "Hot Spicy Chicken", "Soy Garlic Chicken"]

while True:
    item_input = input("\nEnter item number or 'done': ").strip().lower()
    if item_input == 'done':
        break

    # Check if input is a valid number
    if not item_input.isdigit():  # CHANGED: Moved check to prompt for re-entry
        print("Please enter correct item number.")  # ADDED: Error message
        continue
    item_num = int(item_input)
    if item_num < 1 or item_num > len(menu):
        print("Please enter correct item number.")  # ADDED: Error message for out-of-range
        continue

    qty = input("Enter quantity: ").strip()
    if not qty.isdigit() or int(qty) <= 0:
        continue
    qty = int(qty)

    # Get item from menu (adjust index for 1-based input)
    menu_item = menu[item_num - 1]
    order.append([menu_item[1], menu_item[2], qty])
    
    # Combo deal for specific items
    if menu_item[1] in combo_items:
        combo = input(f"Would you add chips for $5 to make a combo deal for '{menu_item[1]}'? (y/n): ").strip().lower()
        if combo == 'y':
            order.append(["Chips (Combo)", 5.00, qty])

# Show order
if order:
    print("\nYour Order:")
    for item in order:
        print(f"{item[0]} x {item[2]}: ${item[1] * item[2]:.2f}")
    print(f"Total: ${calculate_total(order):.2f}")
else:
    print("No items ordered.")
