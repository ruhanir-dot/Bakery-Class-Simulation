class Muffin: # class for muffin flavor, price, and cooking doneness 
    
    def __init__(self,flavor, price, cook_levels):
        
        #initializing a muffin object
        self.flavor = flavor 
        self.price = price 

        # Cooking levels of Muffin 
        self.cook_levels = ["underdone", "well done", "overdone"]
        current_level = 0 # we are starting at under done which is position 0 of the list! 

