from add_remove_create_inventory import *
from create_order import create_order
from inventory_functions import *
from inventory_settings import AlcoholType, SaveFilePath

settings = SaveFilePath()
file_save_path = settings.file_save_path

# create_inventory()
create_order()

# add_new_supplier(file_save_path)
# add_to_existing_supplier(file_save_path)
# remove_from_inventory(file_save_path)
# find_supplier_inventory_info(file_save_path)

