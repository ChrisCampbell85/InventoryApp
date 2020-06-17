

class InventoryApp:

    """Create instance of App""" 

    def __init__(self, name, inventory={}):
        self.name = name
        self.inventory = inventory
        print("Welcome to", name.title(), "app!")
        

    def create_inventory(self):

        """Creates Inventory Dictionary"""

        separator = ', '
        available_items = {}
        
        while True:
            
            inv_item = input(
                "\nPlease enter an item for inventory:\n"
                "Enter 'quit' any time to quit and create inventory\n"
                "> "
            )
            if inv_item == 'quit':
                break
            print("\nPlease enter quantity:")
            try:
                quantity = int(input('> '))
            except ValueError:
                print("Please enter a number.")
                continue
            
            available_items[inv_item] = quantity        
            updated_available = separator.join(available_items)
            self.inventory = available_items
            print('\nYou have set your inventory to:', updated_available)

        """Adds created inventory to text file"""

        txt = 'inventory.txt'
        try:
            with open(txt, 'w') as txt_object:
                for key, value in self.inventory.items():
                    txt_object.write(key.title()+ ': '+str(value) +'\n')

        except FileNotFoundError:
            msg = "Sorry, the file", txt, "does not exist."
            print(msg)

    def get_inventory(self):
        """Retrieves txt file of inventory"""

        inv_txt = 'inventory.txt'
        print("Inventory:\n")
        with open(inv_txt) as obj:
            print(obj.read())
    
    def add_inventory(self):
        """Adds item to inventory and txt file"""
        
        while True:
            
            print('\nPlease enter item to add to inventory:')
            print("Type 'quit' anytime to finish adding items.")
            item = input('> ')
            if item == 'quit':
                print('\nThe new inventory is:\n'+ 
                ''.join('{}: {} \n'.format(key, int(value)) for key, value in self.inventory.items()))
                break
            print("\n Please enter quantity:")
            quantity = int(input('> '))
            try:
                self.inventory[item] += quantity

            except KeyError:
                self.inventory[item] = quantity

        txt = 'inventory.txt'
        try:
            with open(txt, 'w') as txt_object:
                for item, quantity in self.inventory.items():
                    txt_object.write(item +': ' + str(quantity) + '\n')

        except FileNotFoundError:
            msg = "Sorry, the file", txt, "does not exist."
            print(msg)

    def remove_from_inventory(self):
        """Removes item from inventory and txt file"""
        item_and_quantity = ''.join('{}: {} \n'.format(key, int(value)) for key, value in self.inventory.items())
        print("The current inventory is:\n" + item_and_quantity)
        while True:
            
            print('\nPlease enter item to remove from inventory:')
            print("Type 'quit' anytime to finish removing items.")
            item = input('> ')
            
            
            if item == 'quit':
                print('\nThe new inventory is:\n'+ 
                ''.join('{}: {} \n'.format(key, int(value)) for key, value in self.inventory.items()))
                break
            
            print("\n Please enter quantity:")
            quantity = int(input('> '))
            try:
                self.inventory[item] -= quantity
                if self.inventory[item] < 0:
                    print("Error: Item quantity " + str(self.inventory[item]))
                    self.inventory[item] = 0

            except KeyError:
                self.inventory[item] = quantity

        txt = 'inventory.txt'
        try:
            with open(txt, 'w') as txt_object:
                for item, quantity in self.inventory.items():
                    txt_object.write(item +': ' + str(quantity) + '\n')

        except FileNotFoundError:
            msg = "Sorry, the file", txt, "does not exist."
            print(msg)
        
    def create_order(self):
        """Uses inventory to create meal, 
        returns any available item after order created"""

        if self.inventory == {}:
            print("Please create an inventory to continue")
            
        else:
            user_requested = {}
            separator = ', '

            while self.inventory:
                item_and_quantity = ''.join('{}: {} \n'.format(key, int(value)) for key, value in self.inventory.items())
                print("\nYour items to choose from are:\n" + item_and_quantity)
                prompt = input("\nWhat would you like to add to your order?\n"
                "Type 'quit' any time to quit.\n> ")
                if prompt == 'quit':
                    break
                for key in self.inventory.items():
                    if prompt != key:
                        print("Please enter valid selection.")
                number_req = int(input('How many would you like to add?\n> '))
                for key, value in self.inventory.items():
                    if prompt == key:
                        user_requested[key] = number_req
                        self.inventory[key] -= number_req
                        if self.inventory[key] == 0:
                            print("Item " + key + " now sold out.")
                            
                # print('Your remaining items are:\n' + separator.join(self.inventory))
                response = input('\nWould you like to add something else? (y/n)\n')
                new_response = response
                if new_response == 'n':
                    break
                elif new_response == 'y':
                    continue
                
            updated_user = ''.join('{}: {} \n'.format(key, int(value)) for key, value in user_requested.items())
            updated_items = ''.join('{}: {} \n'.format(key, int(value)) for key, value in self.inventory.items())
    
            if user_requested == {}:
                print('No order to prepare')
            else:
                print('\nWe are preparing your order: \n' + updated_user)
            print('\nRemaining items available:\n' + updated_items)
            
        txt = 'inventory.txt'
        try:
            with open(txt, 'w') as txt_object:
                for item, quantity in self.inventory.items():
                    txt_object.write(item +': ' + str(quantity) + '\n')

        except FileNotFoundError:
            msg = "Sorry, the file", txt, "does not exist."
            print(msg)
            

                    

