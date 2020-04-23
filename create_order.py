def create_order(inventory):

    """Uses inventory to create order, returns any available item after order created"""


    separator = ', '

    if inventory == {}:

        print("Please create an inventory to continue")

        return # return early so we don't have un nessicarily nested blocks of code

    user_requested = {}

    while inventory:

        user_item = {}

        company_input = request_supplier_from_user(inventory.keys())
        product_input = request_suppliers_product_from_user(inventory[company_input])
        quantity_input = request_quantity_from_user(product_input, inventory[company_input])

        user_item[product_input] = quantity_input
        user_requested[company_input] = user_item
        
        inventory[company_input][product_input] -= int(quantity_input)
        
        final = finalise_order()
        
        if final == True:
            print_order(user_requested)
            break

def print_order(user_requested):

    print("\nYour order is:")
    for supplier, product_and_quantity in user_requested.items():
        print("\n" + supplier + ":")
        for product, quantity in product_and_quantity.items():
            print(product + ': ' + str(quantity))

        
def finalise_order():

    """Asks user if they want to finalise order, breaks while loop in create_order(inventory) function"""

    user_finalise_order = input("\nWould you like to continue shopping?\n"
    "Type 'y' to continue\nType 'n' to finalise order.\n")

    if user_finalise_order == 'n':
        return True
    if user_finalise_order == 'y':
        pass
    else:
        print("Please enter valid selection")
        return finalise_order()

    
def request_quantity_from_user(user_selected_product, available_suppliers_product):

    """Asks user for input on desired quantity"""

    for item, quantity in available_suppliers_product.items():
        if user_selected_product in item:
            quantity_available = quantity

    print("\nThere is " + str(quantity_available) + " in stock.\n")
    number_required = input("How many would you like to add to your order?\nType 'quit' any time to quit.\n>")

    if number_required == 'quit':

        return None

    if int(number_required) > int(quantity_available):
        
        print("\nPlease enter valid selection\n")

        return request_quantity_from_user(user_selected_product, available_suppliers_product)
    

    return number_required
   

def request_supplier_from_user(supplier_names):

    """Asks user for input on requested supplier"""

    print("\nYour suppliers to choose from are:\n-"
+ '\n-'.join(name for name in supplier_names))

    selected_supplier = input("\nWhich supplier would you like to select from?\n"

    "Type 'quit' any time to quit.\n> ")

    if selected_supplier == 'quit':

        return None

# Check if key in main dict, rejects invalid selections

    if selected_supplier not in supplier_names:

        print("Please enter valid selection")
        
        return request_supplier_from_user(supplier_names)

    return selected_supplier



def request_suppliers_product_from_user(supplier_product_dictionary):

    """Asks user for input on supplier"""


    print("\nYour products to choose from are:\n-"
    + '\n-'.join(name for name in supplier_product_dictionary.keys()))

    selected_product = input("\nWhich product would you like to select?\n"

    "Type 'quit' any time to quit.\n> ")

    if selected_product == 'quit':

        return None

    # Check if key in main dict, rejects invalid selections

    if selected_product not in supplier_product_dictionary.keys():

        print("Please enter valid selection")

        return request_supplier_from_user(supplier_product_dictionary) 

    return selected_product
