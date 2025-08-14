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

# Combo items
combo_items = ["Honey Soy Chicken", "Fried Chicken", "Hot Spicy Chicken", "Soy Garlic Chicken"]


# Displaying menu with numbers
def display_menu():
    print("Menu:")
    for i, item in enumerate(menu, 1):
        print(f"  {i}. {item[1]}: ${item[2]:.2f}")

# Calculating total price
def calculate_total(order):
    total = 0
    for item in order:
        total += item[1] * item[2] 
    return total

# Main program
order = []
display_menu()

# Asking if user the wants to order or not
while True:
    order_choice = input("\nWould you like to order (Y or N)? ").strip().lower()
    if order_choice in ['y', 'n']:
        break
    print("Please answer in Y or N")

if order_choice == 'y':
    while True:
        # Getting item number
        item_input = input("Enter the item number: ").strip()
        if not item_input.isdigit():
            print("Please enter a valid item number.")
            continue

        item_num = int(item_input)
        if item_num < 1 or item_num > len(menu):
            print("Please enter a valid item number.")
            continue

        num = input("Enter quantity: ").strip()
        if not num.isdigit() or int(num) <= 0:
            print("Please enter a valid quantity.")
            continue
        num = int(num)

        # Adding item to order
        menu_item = menu[item_num - 1]
        order.append([menu_item[1], menu_item[2], num])

        # Checking if the user wants combo deal
        if menu_item[1] in combo_items:
            while True:
                combo = input(f"Would you add chips for $4.99 to make a combo deal for '{menu_item[1]}'? (Y/N): ").strip().lower()
                if combo in ['y', 'n']:
                    break
                print("Please answer in Y or N")
            if combo == 'y':
                order.append(["Chips (Combo)", 4.99, num])

        # Asking if user the wants order more or not
        while True:
            more = input("Would you like to order more? (Y or N): ").strip().lower()
            if more in ['y', 'n']:
                break
            print("Please answer in Y or N")
        if more == 'n':
            break


# Showing order
if order:
    print("\nYour Order:")
    for item in order:
        print(f"{item[0]} x {item[2]}: ${item[1] * item[2]:.2f}")
    print(f"Total: ${calculate_total(order):.2f}")
    print(f"Thanks for ordering in our store!")
else:
    print("No items ordered.")
