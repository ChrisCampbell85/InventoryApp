
def create_inventory():

    """Creates Inventory Dictionary"""

    separator = ', '
    inventory = {}
    stock_type_options = "1: Single\n2: 4-pack\n3: 6-pack\n4: Carton"

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
            stock_type = input("\nPlease enter type:\nType 'quit to exit\n" + stock_type_options + "\n> ")
            if stock_type == 'quit':
                break
            if stock_type == '1':
                stock_type = 'Single'
            elif stock_type == '2':
                stock_type = '4-pack'
            elif stock_type == '3':
                stock_type = '6-pack'
            elif stock_type == '4':
                stock_type = 'Carton'
            else:
                print("Please enter valid selection")
                continue
            print('\n' + stock_type + '\n')

            try:
                stock_quantity = int(input("Please enter quantity:\n> "))
            except ValueError:
                print("Please enter a valid number to continue.")
                continue

            # Adds key and value pairs to main dict
            item[stock_type] = stock_quantity
            inventory[company] = item

            # Unpacks key to print as text
            inv = separator.join(inventory)
    
        print('\nYou have updated your inventory to:\n' + inv)

    print("Inventory set to:")
    
    # Iterate through dict
    for key, value in inventory.items():
        print('\n' + key + '\n')
        for key, value in value.items():
            print(key+ ': ' + str(value))
                
    return inventory

create_inventory()