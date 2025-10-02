class Drink:
    def __init__(self, size, type, price): # initializing our drink
        self.size = size
        self.type = type 
        self.price = price 

    def __str__(self): 
        return self.type