import json
import pandas as pd
from collections import OrderedDict
from inventory_functions import *
from inventory_settings import AlcoholType, SaveFilePath

alcohol_type = AlcoholType()
file_settings = SaveFilePath()

file_save_path = file_settings.file_save_path

beer = alcohol_type.beer_stock_types
wine = alcohol_type.wine_stock_types
spirits = alcohol_type.spirit_stock_types

def create_inventory():
    """Create inventory, grouped by supplier alcohol types"""

    main_inventory = {'Beer': {}, 'Wine': {}, 'Spirits': {}}

    while True:
        
        supplier_input = supplier_selection()
        if supplier_input == False:
            break            
        stock_type_input, category = supplier_type_selection(beer, wine, spirits)
        if stock_type_input == False:
            break
        for group, supplier in main_inventory.items():
            if category == group:
                 supplier[supplier_input] = stock_type_input
                 main_inventory[group] = supplier

        # Unpacks key to print as text
        print('\nYou have updated your inventory to:')
        for key, value in main_inventory.items():
            for supplier in value.keys():
                print('-' + supplier + '-')
            
        json_csv_file_save(file_save_path, inventory_dictionary=main_inventory)

    print("Would you like to add quantity to any suppliers? (y/n)")
    user_checkpoint = input("> ")
    if user_checkpoint == 'y':
        return add_to_existing_supplier(file_save_path)
    else:
        return main_inventory

def add_to_existing_supplier(file_save_path):
    """Adds item to existing inventory .json file"""

    inventory_dictionary = json_file_open_add(file_save_path)
    # Function used to check if file exists, returns False if not found
    if inventory_dictionary == False:
        print("File does not exist, please check path is correct.")
        return add_to_existing_supplier(file_save_path)

    # Create new temp dict to remove beer, wine, spirits keys
    temp_dict = {}

    for group, supplier in inventory_dictionary.items():
        temp_dict.update(supplier)

    while True:
        
        display_inventory(temp_dict)
        
        print("\nPlease enter Supplier to update inventory:\n"
        "Type 'quit' to exit.\n")

        inventory_dictionary_supplier = assign_number_dict_keys(temp_dict.keys())
        supplier_input = user_selection(inventory_dictionary_supplier)
        
        if supplier_input == False:
            break
        while True:

            for supplier, products in temp_dict.items():
                if supplier_input == supplier:
                    inventory_dictionary_product = assign_number_dict_keys(products)
            print("\nWhat product type would you like to add to?\n"
            "Type 'quit' to exit.")
            product_input = user_selection(inventory_dictionary_product)
            if product_input == False:
                break

            print("\nPlease enter quantity to add.")
            quantity_input = int(input("> "))

            
            temp_dict[supplier_input][product_input] += quantity_input

            # Pass the updated temp_dict back to inventory_dictionary
            for group, supplier in inventory_dictionary.items():
                if supplier == temp_dict[supplier_input]:
                    inventory_dictionary[group] = temp_dict[supplier_input]

    
    # Save the updated inventory to .json and .csv file
    json_csv_file_save(file_save_path, inventory_dictionary)

def remove_from_inventory(file_save_path):
    """Removes item from existing inventory .json file"""

    inventory_dictionary = json_file_open_remove(file_save_path)
    # Function used to check if file exists, returns False if not found
    if inventory_dictionary == False:
        print("File does not exist, please check path is correct.")
        return remove_from_inventory(file_save_path)

    # Create new temp dict to remove beer, wine, spirits keys
    temp_dict = {}

    for group, supplier in inventory_dictionary.items():
        temp_dict.update(supplier)

    while True:

        print('\nPlease enter Supplier to update in inventory:')
        print("\nType 'quit' to exit.")

        inventory_dictionary_supplier = assign_number_dict_keys(temp_dict.keys())
        supplier_input = user_selection(inventory_dictionary_supplier)

        if supplier_input == False:
            break
        available_items = display_supplier_inventory_info(user_input=supplier_input, inventory=temp_dict)
        
        while True:
           
            print("\nWhat product type would you like to remove from?\n")
            inventory_dictionary_product = assign_number_dict_keys(available_items)
            
            product_input = user_selection(inventory_dictionary_product)
            if product_input == False:
                break
            print("\nPlease enter quantity to remove."
            "\nType 'quit' to exit.")
            quantity_input = int(input("> "))
            if quantity_input == False:
                break
            
            # Check to see if supplier/product exists, if found, updates quantity from user input
            try:     
                temp_dict[supplier_input][product_input] -= quantity_input
                if temp_dict[supplier_input][product_input] < 0:
                    print("Error: item count below 0\n{}: {} set to 0".format(supplier_input, product_input))
                    temp_dict[supplier_input][product_input] = 0
            except KeyError:
                print("Item/s not found, please try again.")
                return remove_from_inventory(file_save_path)
            
            # Pass the updated temp_dict back to inventory_dictionary
            for group, supplier in inventory_dictionary.items():
                if supplier == temp_dict[supplier_input]:
                    inventory_dictionary[group] = temp_dict[supplier_input]
    
    # Save the updated inventory to .json and .csv file
    json_csv_file_save(file_save_path, inventory_dictionary)

def add_new_supplier(file_save_path):
    """Add new supplier to existing inventory"""
    
    inventory_dictionary = json_file_open_add(file_save_path)

    # Create temp dict to store new supplier
    # To be added to main dict at the end of the function
    temp_dict = {}
    
    if inventory_dictionary == False:
       return add_new_supplier(file_save_path)

    while True:

        supplier_input = supplier_selection()
        if supplier_input == False:
            break
        # Check to prevent adding same supplier more than once
        for group, suppliers in inventory_dictionary.items():
            if supplier_input in suppliers:
                print("\nSupplier already exists.\n"
                "Type 'quit' to exit or try again")
                return add_new_supplier(file_save_path)

        stock_type_input, category = supplier_type_selection(beer, wine, spirits)
        if stock_type_input == False:
            break
        for group, supplier in inventory_dictionary.items():
            if category == group:
                temp_dict[supplier_input] = stock_type_input
                inventory_dictionary[group].update(temp_dict)
                        
        print("Would you like to add quantity to any suppliers? (y/n)")
        user_checkpoint = input("> ")
        if user_checkpoint == 'y':
            json_csv_file_save(file_save_path, inventory_dictionary)
            return add_to_existing_supplier(file_save_path)
        # Save the updated inventory to .json and .csv file
        else:
            json_csv_file_save(file_save_path, inventory_dictionary)


def json_file_open_remove(inventory_file_and_path):
    """Open .json file for remove function"""
    try:
        with open(inventory_file_and_path) as json_file:
            inventory_dictionary = json.load(json_file)
    except FileNotFoundError:
        print("File not found.")
        return False
    return inventory_dictionary

def json_file_open_add(inventory_file_and_path):
    """ Open .json file for add function"""
    try:
        with open(inventory_file_and_path) as json_file:
            inventory_dictionary = json.load(json_file)
            dict(inventory_dictionary)
    except FileNotFoundError:
        print("File not found.")
        return False    
    return inventory_dictionary

def find_supplier_inventory_info(file_save_path):
    """Finds specific info on selected supplier"""
    supplier_to_find = json_file_open_add(file_save_path)
    user_selected_supplier = input("\nWhich supplier are you looking for?\n"
    "Type 'quit to exit\n> ").title()
    # Displays current inventory
    for group, suppliers in supplier_to_find.items():
        for supplier, product in suppliers.items():
            if user_selected_supplier == 'quit'.title():
                return
            elif user_selected_supplier not in supplier:
                print("Supplier not found, please try again.")
                return find_supplier_inventory_info(file_save_path)
            elif user_selected_supplier == supplier:
                print('\n-' + supplier + '-\n')
                for key, value in product.items():
                    if value > 0:
                        print(key + ": " + str(value))
    return find_supplier_inventory_info(file_save_path)
                        
