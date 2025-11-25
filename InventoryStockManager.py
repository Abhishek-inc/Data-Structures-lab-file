# Inventory list to store product records
inventory = []

# Function to insert one or more products
def insert_product():
    SKUs = input("Enter SKU(s): ").replace(',', ' ').split()
    names = input("Enter product name(s): ").replace(',', ' ').split()
    quantities = input("Enter quantity/quantities: ").replace(',', ' ').split()

    # Validation checks
    if len(names) != len(SKUs):
        print("Error: The number of SKUs and product names must match.")
        return
    if len(quantities) != len(SKUs):
        print("Error: The number of SKUs and quantities must match.")
        return

    for i in range(len(SKUs)):
        sku = SKUs[i].strip()
        name = names[i].strip()
        qty_str = quantities[i].strip()

        if not sku:
            print("Error: SKU cannot be empty.")
            continue
        if sku in [item['sku'] for item in inventory]:
            print(f"Error: SKU {sku} already exists in the inventory.")
            continue
        try:
            qty = int(qty_str)
            inventory.append({'sku': sku, 'name': name, 'quantity': qty})
            print(f"Product '{name}' with SKU {sku} inserted successfully.")
        except ValueError:
            print(f"Error: Quantity '{qty_str}' for SKU {sku} is not a valid number.")

# Function to display inventory
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")
    print("SKU\t\tProduct Name\t\tQuantity")
    print("-------------------------------------------------")
    for item in inventory:
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}")
    print()

# Function to process sale
def process_sale():
    sku = input("Enter SKU for sale: ")
    try:
        qty_sold = int(input("Enter quantity sold: "))
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    for item in inventory:
        if item['sku'] == sku:
            if item['quantity'] >= qty_sold:
                item['quantity'] -= qty_sold
                print(f"Sale processed: {qty_sold} units of SKU {sku}.")
            else:
                print(f"Insufficient stock for SKU {sku}. Available: {item['quantity']}")
            return
    print(f"SKU {sku} not found in inventory.")

# Function to identify zero stock
def identify_zero_stock():
    zero_stock_list = [item['sku'] for item in inventory if item['quantity'] == 0]
    if zero_stock_list:
        print("Zero stock SKUs:")
        for sku in zero_stock_list:
            print(sku)
    else:
        print("No zero stock items found.")
    return zero_stock_list

# Function to calculate total and average stock (operates on dict-based inventory)
def total_and_avg():
    if not inventory:
        return 0, 0  # handle empty inventory
    total = sum(item['quantity'] for item in inventory)
    avg = total / len(inventory)
    return total, avg

# Function to find the item with maximum stock (returns SKU and Quantity)
def max_stock_item():
    if not inventory:
        return None, None
    max_item = max(inventory, key=lambda x: x['quantity'])
    return max_item['sku'], max_item['quantity']

# Main program loop
def menu():
    while True:
        print("\nInventory Stock Manager")
        print("1. Insert New Product(s)")
        print("2. Display Inventory")
        print("3. Process Sale")
        print("4. Identify Zero Stock Items")
        print("5. Calculate Total and Average Stock")
        print("6. Find Maximum Stock Item")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            insert_product()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            process_sale()
        elif choice == '4':
            identify_zero_stock()
        elif choice == '5':
            total, avg = total_and_avg()
            print(f"Inventory: {inventory}")
            print(f"Total Stock: {total}")
            print(f"Average Stock: {avg:.2f}")
        elif choice == '6':
            sku, qty = max_stock_item()
            if sku is None:
                print("Inventory is empty! Add products first.")
            else:
                # attempt to display name if present
                name = next((it['name'] for it in inventory if it['sku'] == sku), None)
                if name:
                    print(f"Item with Maximum Stock: SKU {sku}, Name: {name}, Quantity {qty}")
                else:
                    print(f"Item with Maximum Stock: SKU {sku}, Quantity {qty}")
        elif choice == '7':
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

# Start the program when executed directly
if __name__ == "__main__":
    menu()
