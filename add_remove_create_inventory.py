import json
import pandas as pd
from time import sleep
from collections import OrderedDict
from inventory_functions import *

file_save_path = "C:\\Users\Chris\Documents\VS_CODE_LEARNING\MenuApp\\"
stock_type_options = {'1': 'Single', '2': '4-Pack', '3': '6-Pack', '4': '16-Pack', '5': '24-Pack'}

def add_to_existing_inventory():

    """Adds item to existing inventory .json file"""

    # Read in existing inventory nested dictionary from user input
    inventory_file = input("Please enter file to use.\n> ")
    inventory_file_and_path = file_save_path + inventory_file
    
    inventory_dictionary = json_file_open_add(inventory_file_and_path)
    if inventory_dictionary == False:
        return add_to_existing_inventory()

    while True:
        
        display_inventory(inventory_dictionary)
        
        print("\nPlease enter Supplier to update inventory:\n"
        "Type 'quit' to exit.\n")

        inventory_dictionary_supplier = assign_number_dict_keys(inventory_dictionary.keys())
        supplier_input = user_selection(inventory_dictionary_supplier)
        if supplier_input == False:
            break
        while True:

            temp_dict = {}

            for key, value in inventory_dictionary.items():
                if supplier_input ==  key:
                    inventory_dictionary_product = assign_number_dict_keys(value)
            
            print("\nWhat product type would you like to add to?\n"
            "Type 'quit' to exit.")
            product_input = user_selection(inventory_dictionary_product)
            if product_input == False:
                break

            print("\nPlease enter quantity to add.")
            quantity_input = int(input("> "))
            
            inventory_dictionary[supplier_input][product_input] += quantity_input

        # Save the updated inventory to json file
    json_csv_file_save(inventory_file_and_path, inventory_dictionary)
            
def add_new_supplier():
    """Add new supplier to existing inventory"""
    
    # Read in existing inventory .json file from user input
    inventory_file = input("Please enter file to use.\n> ")
    inventory_file_and_path = file_save_path + inventory_file
    inventory_dictionary = json_file_open_add_new(inventory_file_and_path)
    
    if inventory_dictionary == False:
       return add_new_supplier()

    while True:

        display_inventory(inventory_dictionary)

        temp_dict = {}
        supplier_input = supplier_selection()
        if supplier_input == False:
            break

        while True:
            print("Please enter ALL stock types for this supplier.\n"
            "Enter 0 where applicable.")
            stock_type_input = stock_type_selection(stock_type_options)
            if stock_type_input == False:
                break
            try:
                stock_quantity = int(input("Please enter quantity:\n> "))

            except ValueError:
                print("Please enter a valid number to continue.")
                continue

            # Adds key and value pairs to main dict, sorts dict
            temp_dict[stock_type_input] = stock_quantity
            sort_item = sorted(temp_dict.items(), key=lambda kv: kv[0][:1], reverse=True)
            sorted_item_dict = OrderedDict(sort_item)
            inventory_dictionary[supplier_input] = sorted_item_dict

            # Unpacks key to print as text
            unpacked_inventory = ', '.join(inventory_dictionary)
    
        print('\nYou have updated your inventory to:\n' + unpacked_inventory)
        
    display_inventory(inventory_dictionary)
    # Save the updated inventory to json file
    json_csv_file_save(inventory_file_and_path, inventory_dictionary)

def remove_from_inventory():
    """Removes item from existing inventory .json file"""

    # Read in existing inventory .json file from user input
    inventory_file = input("Please enter file to use.\n> ")
    inventory_file_and_path = file_save_path + inventory_file
    inventory_dictionary = json_file_open_remove(inventory_file_and_path)
    if inventory_dictionary == False:
        return remove_from_inventory()

    while True:

        display_inventory(inventory_dictionary)
        
        print('\nPlease enter Supplier to update in inventory:')
        print("Type 'quit' to exit.")
        inventory_dictionary_supplier = assign_number_dict_keys(inventory_dictionary.keys())
        supplier_input = user_selection(inventory_dictionary_supplier)
        if supplier_input == False:
            break
        while True:
           
            for key, value in inventory_dictionary.items():
                if supplier_input ==  key:
                    inventory_dictionary_product = assign_number_dict_keys(value)
            print("\nWhat product type would you like to remove from?")
            
            product_input = user_selection(inventory_dictionary_product)
            if product_input == False:
                break
            print("\nPlease enter quantity to remove."
            "Type 'quit' to exit.")
            quantity_input = int(input("> "))
            if quantity_input == False:
                break

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

    json_csv_file_save(inventory_file_and_path, inventory_dictionary)

def create_inventory():
    """Creates Inventory Dictionary"""

    inventory = {}
   
    while True:
        
        temp_dict = {}
        supplier_input = supplier_selection()
        if supplier_input == False:
            break

        while True:
            print("Please enter ALL stock types for this supplier.")
            stock_type_input = stock_type_selection(stock_type_options)
            if stock_type_input == False:
                break
            stock_quantity = 0

            # Adds key and value pairs to main dict, sorts dict
            temp_dict[stock_type_input] = stock_quantity
            sort_item = sorted(temp_dict.items(), key=lambda kv: kv[0][:1], reverse=True)
            sorted_item_dict = OrderedDict(sort_item)
            inventory[supplier_input] = sorted_item_dict

            # Unpacks key to print as text
            unpacked_inventory = ', '.join(inventory)
    
        print('\nYou have updated your inventory to:\n' + unpacked_inventory)

    display_inventory(inventory)
    convert_dict_to_json_csv_create_inventory(inventory)
    return inventory

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

def json_file_open_add_new(inventory_file_and_path):
    """ Open .json file for add new function"""
    try:
        with open(inventory_file_and_path) as json_file:
            inventory_dictionary = json.load(json_file)
            dict(inventory_dictionary)
    except FileNotFoundError:
        print("File not found.")
        return False
    return inventory_dictionary

