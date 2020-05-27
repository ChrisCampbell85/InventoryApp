import pandas as pd
import csv
import json
from inventory_functions import *
from inventory_settings import AlcoholType, SaveFilePath

file_settings = SaveFilePath()
file_save_path = file_settings.file_save_path
base_file_save_path = file_settings.base_file_save_path


def create_order():

    """Uses inventory to create order, saves order to .json file"""
    inventory = import_json_inventory(file_save_path)
    if inventory == {}:
        print("Please create an inventory to continue")
        return # return early so we don't have unnecessarily nested blocks of code
    
    # Removes group keys from inventory
    temp_dict = {}

    for group, supplier in inventory.items():
        temp_dict.update(supplier)

    # Dict to store entire user order
    user_requested = {}
        
    while inventory:
        # Dict to store each selected item
        user_item = {}
        company_input = request_supplier_from_user(supplier_names=temp_dict)
        if company_input == False:
            print_order(user_requested)
        # Update base inventory, removing items in user order
            json_csv_file_save(file_save_path, inventory_dictionary=inventory)
            break
        # Display current inventory for selected supplier
        items = display_supplier_inventory_info(company_input, inventory=temp_dict)

        while True:
            product_input = request_suppliers_product_from_user(items)
            if product_input == False:
                break
            quantity_input = request_quantity_from_user(items, product_input)
            if quantity_input == False:
                break
        # Add item value to company key without overriding first selection
            user_item[product_input] = quantity_input
            user_requested[company_input] = user_item

        # NEED TO FIX
        # Subtracts order items from base inventory
            temp_dict[company_input][product_input] -= int(quantity_input)
        # Pass dict back to main inventory
            for group, supplier in inventory.items():
                if supplier == temp_dict[company_input]:
                    inventory[group] = temp_dict[company_input]
        
    # Convert order to separate .json file
    convert_dict_to_json_order(file_to_convert=user_requested, base_file_save_path=base_file_save_path)
