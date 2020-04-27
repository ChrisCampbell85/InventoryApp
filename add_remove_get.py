import json
from time import sleep

def add_to_inventory():

    """Adds item to existing inventory .json file"""

    # Read in existing inventory nested dictionary from user input
    inventory_file = input("Please enter file to use.\n> ")
    
    try:
        with open(inventory_file) as json_file:
            inventory_dictionary = json.load(json_file)
    except FileNotFoundError:
        return add_to_inventory()

    # Displays current inventory
    print("\nInventory:")
    for supplier, product in inventory_dictionary.items():
         print('\n' + supplier)
         for item_type, item_quantity in product.items():
             print(item_type + ': ' + str(item_quantity))
        
    while True:
        
        print('\nPlease enter Supplier to update/add to inventory:')
        print("Type 'quit' exit.")
        supplier_input = str(input('> '))
        if supplier_input == 'quit':
            break

        print("\nWhat product type would you like to add?")
        product_input = input("> ")
        
        print("\nPlease enter quantity.")
        quantity_input = int(input("> "))

        # Check to see if supplier/product exists, adds to existing or creates new entry
        try:
            inventory_dictionary[supplier_input][product_input] += quantity_input
        except KeyError:
            inventory_dictionary[supplier_input][product_input] = quantity_input
                           
        # Save the updated inventory to json file
    with open(inventory_file, 'w') as json_file:
        json.dump(inventory_dictionary, json_file)
            

def remove_from_inventory():
    """Removes item from existing inventory .json file"""

    # Read in existing inventory nested dictionary from user input
    inventory_file = input("Please enter file to use.\n> ")
    
    try:
        with open(inventory_file) as json_file:
            inventory_dictionary = json.load(json_file)
    except FileNotFoundError:
        return remove_from_inventory()

    # Displays current inventory
        
    while True:
        
        print("\nInventory:")
        for supplier, product in inventory_dictionary.items():
            print('\n' + supplier)
            for item_type, item_quantity in product.items():
                print(item_type + ': ' + str(item_quantity))
        
        print('\nPlease enter Supplier to update in inventory:')
        print("Type 'quit' to exit.")
        supplier_input = str(input('> '))
        if supplier_input == 'quit':
            break
        if supplier_input not in inventory_dictionary:
            continue

        print("\nWhat product type would you like to remove from?")
        product_input = input("> ")
        
        print("\nPlease enter quantity to remove.")
        quantity_input = int(input("> "))

        # Check to see if supplier/product exists, if found, updates quantity from user input
        try:     
            inventory_dictionary[supplier_input][product_input] -= quantity_input
            if inventory_dictionary[supplier_input][product_input] < 0:
                print("Error: item count below 0\n{}: {} set to 0".format(supplier_input, product_input))
                inventory_dictionary[supplier_input][product_input] = 0
                sleep(1)
        except KeyError:
            print("Item/s not found, please try again.")
            return remove_from_inventory()
                           
        # Save the updated inventory to json file
    with open(inventory_file, 'w') as json_file:
        json.dump(inventory_dictionary, json_file)




    
