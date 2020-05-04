import pandas as pd
import csv
import json
from inventory_functions import assign_number_dict_keys, user_selection

def create_order(inventory):

    """Uses inventory to create order, returns any available item after order created"""
    
    if inventory == {}:
        print("Please create an inventory to continue")
        return # return early so we don't have unnecessarily nested blocks of code
    
    user_requested = {}
        
    while inventory:

        user_item = {}
        company_input = request_supplier_from_user(inventory.keys())
        if company_input == False:
            print_order(user_requested)
        # Update base inventory, removing items in user order
            convert_dict_to_json_csv_inventory(inventory)
            break

        while True:
            product_input = request_suppliers_product_from_user(inventory[company_input])
            if product_input == False:
                break
            quantity_input = request_quantity_from_user(product_input, inventory[company_input])
            if quantity_input == False:
                break
        # Add item value to company key without overriding first selection
            user_item[product_input] = quantity_input
            user_requested[company_input] = user_item
            
        # Subtracts order items from base inventory
            inventory[company_input][product_input] -= int(quantity_input)
        
    # Convert order to separate .json file
    convert_dict_to_json_order(user_requested)
    
    return user_requested

def convert_dict_to_json_order(file_to_convert):
    """Converts order dictionary to .json file"""

    file_save_path = "C:\\Users\Chris\Documents\VS_CODE_LEARNING\MenuApp\\"
    output_file_name = input("What name would you like to use for this order?\n> ").upper()

    # Full PATH attached to desired filename for desired save location
    file_and_location = file_save_path + output_file_name +'_order.json'

    with open(file_and_location, 'w') as json_file:
        json.dump(file_to_convert, json_file)

def convert_dict_to_json_csv_inventory(file_to_convert):
    """Updates inventory to .json and .csv file"""

    file_save_path = "C:\\Users\Chris\Documents\VS_CODE_LEARNING\MenuApp\inventory.json"
    with open(file_save_path, 'w') as json_file:
        json.dump(file_to_convert, json_file)

        # Save as .csv
        # Clean up the saved filename
        csv_save_file, __, __ = file_save_path.rpartition('.')
        # Add file to DataFrame
        data = pd.DataFrame(file_to_convert)
        data = data.fillna("0")
        data.to_csv(csv_save_file + '.csv')

def import_json_inventory():
    """Import .json file containing created inventory, used as argument for create_order()"""

    file_save_path = "C:\\Users\Chris\Documents\VS_CODE_LEARNING\MenuApp\inventory.json"
    with open(file_save_path) as json_file:
        inventory = json.load(json_file)
    return inventory

def print_order(user_order):

    print("\nYour order is:")
    for supplier, product_and_quantity in user_order.items():
        print("\n" + supplier + ":")
        for product, quantity in product_and_quantity.items():
            print(product + ': ' + str(quantity))

def user_checkpoint():

    """Asks user if they want to finalise order, breaks while loop in create_order(inventory) function"""

    user_finalise_order = input("\nWould you like to continue shopping?\n"
    "Type 'y' to continue\nType 'n' to finalise order.\n")

    if user_finalise_order == 'n':
        return True
    if user_finalise_order == 'y':
        pass
    else:
        print("Please enter valid selection")
        return user_checkpoint_final()
    
def request_quantity_from_user(user_selected_product, available_suppliers_product):

    """Asks user for input on desired quantity"""

    for item, quantity in available_suppliers_product.items():
        if user_selected_product in item:
            quantity_available = quantity

    print("\nThere is " + str(quantity_available) + " in stock.\n")
    number_required = input("How many would you like to add to your order?\n"
    "Type 'quit' to exit or reselect product.\n>")
    try:
        number_required = int(number_required)
    # Handles string input, quits or recalls function
    except ValueError:
        if number_required == 'quit':
            number_required = False
            return number_required
        else:
            print("Please enter a number")
            return request_quantity_from_user(user_selected_product, available_suppliers_product)

    # Check for quantity available, rejects input that exceeds
    if int(number_required) > int(quantity_available): 
        print("\nPlease enter valid selection\n")
        return request_quantity_from_user(user_selected_product, available_suppliers_product)
    
    return number_required
   
def request_supplier_from_user(supplier_names): 
    """Asks user for input on requested supplier"""

    print("\nEnter number to select supplier.\n"
    "Type 'quit' any time to quit.\n")

    # Print number assigned supplier list, accepts user input
    # Rejects invalid selections
    number_assigned_supplier = assign_number_dict_keys(supplier_names)
    selected_supplier = user_selection(number_assigned_supplier)

    if selected_supplier == False:
        return False
    else:
        print("\n" + selected_supplier)
        return selected_supplier

def request_suppliers_product_from_user(supplier_product_dictionary):
    """Asks user for input on supplier"""

    print("\nEnter number of product to select.\n"
    "Type 'quit' any time to quit.\n")
    
    # Print number assigned product list, accepts user input
    # Rejects invalid selections
    number_assigned_product = assign_number_dict_keys(supplier_product_dictionary)
    selected_product = user_selection(number_assigned_product)

    if selected_product == False:
        return False
    else:
        print("\n" + selected_product)
        return selected_product

