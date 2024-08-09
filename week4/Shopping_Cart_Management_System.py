"""
Create a 

Develop a Python program to simulate a straighvorward shopping cart
management system, allowing users to perform operations such as adding items,
viewing the cart contents, removing items, and calculating the total cost of items in
the cart. Utilize dictionaries to store item details, including name, price, and quantity,
and use a list to represent the shopping cart.
"""

# Define the inventory of items
inventory = {
    '001': {'name': 'Laptop', 'price': 999.99, 'quantity': 10},
    '002': {'name': 'Mouse', 'price': 25.50, 'quantity': 50},
    '003': {'name': 'Keyboard', 'price': 45.00, 'quantity': 30},
    '004': {'name': 'Monitor', 'price': 200.00, 'quantity': 20},
    '005': {'name': 'Headphones', 'price': 75.00, 'quantity': 15},
}

# Initialize an empty shopping cart
cart = []

def add_item_to_cart(item_code, quantity):
    """Add items to the shopping cart."""
    if item_code not in inventory:
        print("Item code not found.")
        return
    
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return
    
    item = inventory[item_code]
    if quantity > item['quantity']:
        print("Insufficient stock available.")
        return
    
    # Check if item is already in the cart
    for cart_item in cart:
        if cart_item['code'] == item_code:
            cart_item['quantity'] += quantity
            item['quantity'] -= quantity
            print(f"Updated {item['name']} quantity to {cart_item['quantity']}.")
            return
    
    # Add new item to the cart
    cart.append({'code': item_code, 'quantity': quantity})
    item['quantity'] -= quantity
    print(f"Added {item['name']} ({quantity}) to the cart.")

def view_cart():
    """View the contents of the shopping cart."""
    if not cart:
        print("Your cart is empty.")
        return
    
    print("\nShopping Cart Contents:")
    for item in cart:
        item_code = item['code']
        item_details = inventory[item_code]
        print(f"Item: {item_details['name']}, Price: ${item_details['price']:.2f}, Quantity: {item['quantity']}")
    print()

def remove_item_from_cart(item_code):
    """Remove items from the shopping cart."""
    global cart
    
    cart = [item for item in cart if item['code'] != item_code]
    print(f"Removed item with code {item_code} from the cart.")

def calculate_total_cost():
    """Calculate the total cost of items in the cart."""
    total_cost = 0
    for item in cart:
        item_code = item['code']
        item_details = inventory[item_code]
        total_cost += item_details['price'] * item['quantity']
    return total_cost

def main():
    """Main function to interact with the user."""
    while True:
        print("\nShopping Cart Management System")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Calculate total cost")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            item_code = input("Enter item code: ").strip()
            quantity = int(input("Enter quantity: ").strip())
            add_item_to_cart(item_code, quantity)
        
        elif choice == '2':
            view_cart()
        
        elif choice == '3':
            item_code = input("Enter item code to remove: ").strip()
            remove_item_from_cart(item_code)
        
        elif choice == '4':
            total_cost = calculate_total_cost()
            print(f"Total cost of items in the cart: ${total_cost:.2f}")
        
        elif choice == '5':
            print("Exiting the system. Thank you!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
