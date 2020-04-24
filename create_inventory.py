def create_inventory():

    """Creates Inventory Dictionary"""

    inventory = {}
    stock_type_options = {'1': 'Single', '2': '4-pack', '3': '6-pack', '4': 'Carton'}

    while True:
        
        item = {}
        company = str(input(
        "\nPlease enter Company name for inventory:\n"
        "Enter 'quit' any time to quit and create inventory\n"
        "> "
        ))
        if company == 'quit':
            break

        while True:
            print("\nStock type options to choose from are:\n")
            for key, value in stock_type_options.items():
                print(key +': ' + value)
            stock_type = input("\nPlease enter type:\nType 'quit to exit\n")

            if stock_type == 'quit':
                break
            if stock_type not in stock_type_options:
                print("Please enter valid selection")
                continue
            for key, value in stock_type_options.items():
                if stock_type == key:
                    stock_type = value
            print('\nYou have have selected: ' + stock_type + '\n')

            try:
                stock_quantity = int(input("Please enter quantity:\n> "))
            except ValueError:
                print("Please enter a valid number to continue.")
                continue

            # Adds key and value pairs to main dict
            item[stock_type] = stock_quantity
            inventory[company] = item

            # Unpacks key to print as text
            inv = ', '.join(inventory)
    
        print('\nYou have updated your inventory to:\n' + inv)

    print("Inventory set to:")
    
    # Iterate through dict
    for key, value in inventory.items():
        print('\n-' + key + '-')
        for key, value in value.items():
            print(key+ ': ' + str(value))
                
    return inventory
