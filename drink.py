class Drink: # class representing drink --> size, type, price
    
    def __init__(self, size, drink_type, price): # initializing our drink
        self.size = size
        self.type = drink_type
        self.price = price
    
    def __str__(self): # string representation of drink!
        return self.type