  # Import the tabulate library for creating a nicely formatted table.
# To use this, you'll need to install it by running 'pip install tabulate' in your terminal.
from tabulate import tabulate

# --- Global Variables and Data ---

# A dictionary to store the menu items and their prices.
# This uses key-value pairs (string: float) to link each item to its price.
MENU_ITEMS = {
    "Honey Soy Chicken": 32.99,
    "Fried Chicken": 29.99,
    "Hot Spicy Chicken": 30.99,
    "Soy Garlic Chicken": 30.99,
    "Seasoned Chicken Bowl": 24.99,
    "Honey Soy Chicken Bowl": 25.99,
    "Chicken Burger": 20.99,
    "Chips": 9.99,
    "Hotdog": 6.90
}
