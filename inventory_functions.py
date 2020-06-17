import pandas as pd
import json
from collections import OrderedDict

def display_inventory(inventory_dictionary):
    """Displays current inventory to user"""

    print("\nInventory:")
        
    # Displays current inventory
    for supplier, product in inventory_dictionary.items():
        print('\n-' + supplier + '-')
        for item_type, item_quantity in product.items():
            print(item_type + ': ' + str(item_quantity))

def stock_type_count(csv_file):
    pass

def assign_number_dict_keys(supplier_names):
    """Assigns and prints each item a number for numerical user input"""

    dictionary = {}
    number = 0
    max_length = len(supplier_names)
    while number < max_length:
        for name in supplier_names:
            number += 1
            dictionary[number] = name
    for key, value in dictionary.items():
        print(str(key) + ': ' + value)
    return dictionary

def user_selection(dict_selection_options):
    """Stores user input for selecting item in add & remove function"""

    user_input = input("\n> ")
    if user_input == "quit":
        return False
    else:
        try:
            user_input = int(user_input)
        except ValueError:
            return user_selection(dict_selection_options)

    for key, value in dict_selection_options.items():
        if user_input not in dict_selection_options:
            print("Please enter valid selection.")
            return user_selection(dict_selection_options)
        if user_input == key:
            return dict_selection_options[key]

def supplier_selection():
    """ To select supplier in create_inventory & add_new_supplier function"""
    supplier_input = str(input(
    "\nPlease enter Supplier to add to inventory.\n"
    "Enter 'quit' any time to exit\n"
    "> "))

    if supplier_input == 'quit'.lower():
        return False
    return supplier_input.title()

def supplier_type_selection(beer, wine, spirits):

    print("\nPlease select stock type for this supplier from the following options:\n"
    "1: Beer\n2: Wine\n3: Spirits\Vermouth")
    
    stock_type_user_input = input("\n> ")

    if stock_type_user_input == '1':
        return beer, 'Beer'
    elif stock_type_user_input == '2':
        return wine, 'Wine'
    elif stock_type_user_input == '3':
        return spirits, 'Spirits'
    else:
        return supplier_type_selection(beer, wine, spirits)

def convert_dict_to_json_order(file_to_convert, base_file_save_path):
    """Converts user ORDER dictionary to .json file"""

    output_file_name = input("What name would you like to use for this order?\n> ").upper()

    # Full PATH attached to desired filename for desired save location, 
    # located in InventorySettings
    file_and_location = base_file_save_path + output_file_name +'_order.json'

    with open(file_and_location, 'w') as json_file:
        json.dump(file_to_convert, json_file)

def import_json_inventory(file_save_path):
    """Import .json file containing created inventory, used as argument for create_order()"""

    with open(file_save_path) as json_file:
        inventory = json.load(json_file)
   
    return inventory

def print_order(user_order):

    print("\nYour order is:")
    for supplier, product_and_quantity in user_order.items():
        print("\n" + supplier + ":")
        for product, quantity in product_and_quantity.items():
            print(product + ': ' + str(quantity))

def request_quantity_from_user(available_suppliers_product, user_selected_product):

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

def request_suppliers_product_from_user(items):

    print("\nEnter number of product to select.\n"
    "Type 'quit' any time to quit.\n")
    
    # Print number assigned product list, accepts user input
    # Rejects invalid selections
    number_assigned_product = assign_number_dict_keys(items)
    selected_product = user_selection(number_assigned_product)
    if selected_product == False:
        return False
    else:
        print("\n" + selected_product)
    return selected_product

def display_supplier_inventory_info(user_input, inventory):
    """Displays selected supplier inventory for user creating order"""
    name_dict = {}
    # Displays current inventory
    for supplier, product in inventory.items():
        if user_input == supplier:
            print('\n-' + supplier + '-\n')
            for key, value in product.items():
                if value > 0:
                    print(key + ": " + str(value))
                    name_dict[key] = value
    return name_dict

def json_csv_file_save(file_save_path, inventory_dictionary):
    """Save to .json and .csv file"""
    with open(file_save_path, 'w') as json_file:
        json.dump(inventory_dictionary, json_file)

        # Save as .csv
        # Clean up the saved filename
        csv_save_file, __, __ = file_save_path.rpartition('.')
        # Add file to DataFrame
        data = pd.DataFrame.from_dict({(key,value): inventory_dictionary[key][value] 
                           for key in inventory_dictionary.keys() 
                           for value in inventory_dictionary[key].keys()},
                       orient='columns')
        data = data.fillna("0")
        data.to_csv(csv_save_file + '.csv')