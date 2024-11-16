# Inventory Management System - Basic Input from Keyboard

# Function to add items to the inventory
def add_items():
    inventory_data = []
    
    # Number of items to add
    num_items = int(input("Enter the number of items you want to add: "))
    
    # Loop to gather data for each item
    for i in range(num_items):
        print(f"\nEnter details for item {i + 1}:")
        product_name = input("Product Name: ")
        unit_price = float(input("Unit Price: $"))
        quantity = int(input("Quantity: "))
        net_price = unit_price * quantity  # Calculate net price
        
        # Add item to the inventory list
        inventory_data.append({
            "product_name": product_name,
            "unit_price": unit_price,
            "quantity": quantity,
            "net_price": net_price
        })
    
    # Display all entered items
    print("\nInventory Summary:")
    print("{:<15} {:<15} {:<10} {:<15}".format("Product Name", "Unit Price ($)", "Quantity", "Net Price ($)"))
    for item in inventory_data:
        print("{:<15} ${:<14.2f} {:<10} ${:<15.2f}".format(item["product_name"], item["unit_price"], item["quantity"], item["net_price"]))

# Run the inventory input function
add_items()
