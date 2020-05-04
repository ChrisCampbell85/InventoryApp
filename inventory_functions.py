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

def json_csv_file_save(inventory_file_and_path, inventory_dictionary):
    """Save to .json file"""
    with open(inventory_file_and_path, 'w') as json_file:
        json.dump(inventory_dictionary, json_file)

        # Save as .csv
        # Clean up the saved filename
        csv_save_file, __, __ = inventory_file_and_path.rpartition('.')
        # Add file to DataFrame
        data = pd.DataFrame(inventory_dictionary)
        data = data.fillna("0")
        data.to_csv(csv_save_file + '.csv')

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

    if supplier_input == 'quit':
        return False
    return supplier_input
    
def stock_type_selection(stock_type_options):
    """Stores input regarding stock type"""

    print("\nStock type options to choose from are:\n")
    for key, value in stock_type_options.items():
        print(key +': ' + value)
    stock_type_input = input("\nPlease enter type:\nType 'quit' to exit\n")

    if stock_type_input == 'quit':
        return False

    if stock_type_input not in stock_type_options:
        print("Please enter valid selection")
        return stock_type_selection(stock_type_options)
        
    for key, value in stock_type_options.items():
        if stock_type_input == key:
            stock_type_input = value
    print('\nYou have have selected: ' + stock_type_input + '\n')
    return stock_type_input

def convert_dict_to_json_csv_create_inventory(inventory):
    """Converts dictionary to .json file"""

    # Full PATH attached to desired filename for desired save location
    file_save_path = "C:\\Users\Chris\Documents\VS_CODE_LEARNING\MenuApp\\"
    user_input = input("Please type output file name\n> ")
    file_and_location = file_save_path + user_input +'.json'

    with open(file_and_location, 'w') as json_file:
        json.dump(inventory, json_file)
        
        # Save as .csv
        # Clean up the saved filename
        csv_save_file, __, __ = file_and_location.rpartition('.')
        # Add file to DataFrame
        data = pd.DataFrame(inventory)
        data = data.fillna("0")
        data.to_csv(csv_save_file + '.csv')
