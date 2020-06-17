class AlcoholType():
    """Initialises the inventory's alcohol type stock settings"""
    
    def __init__(self):
        self.beer_stock_types =  {
            'Single bottle': 0, 'Single (can)': 0, '4-Pack (bottle)': 0, 
            '4-Pack (can)': 0, '6-Pack (bottle)': 0, '6-Pack (can)': 0,
            '16-Pack (can)': 0, '24-Pack (bottle)': 0, 
            '24-Pack (can)': 0, '30-Pack (can)': 0
            }
        self.wine_stock_types = {'Single bottle': 0, 'Case (6)': 0, 'Case (12)': 0, 'Cask 4L': 0}
        self.spirit_stock_types = {'Single bottle': 0, 'Case (6)': 0, 'Case (12)': 0}

        
        
class SaveFilePath():
    """File save locations for inventory"""

    def __init__(self):
        self.file_save_path = "C:\\Users\Chris\Documents\VS_CODE_LEARNING\InventoryApp\inventory.json"
        self.base_file_save_path = "C:\\Users\Chris\Documents\VS_CODE_LEARNING\InventoryApp\\"
        