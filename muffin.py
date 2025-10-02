class Muffin: # class for muffin flavor, price, and cooking doneness 
    
    def __init__(self,flavor, price, cook_levels):
        
        #initializing a muffin object
        self.flavor = flavor 
        self.price = price 

        # Cooking levels of Muffin 
        self.cook_levels = ["underdone", "well done", "overdone"]
        current_level = 0 # we are starting at under done which is position 0 of the list! 

    def bake_muffin(self): # updates the cooking level of the muffin each time called 
        if self.current_level < len(self.cook_levels): # checking if muffin is not overdone or underdone
            self.current_level += 1       
    
    def get_description(self): 
        muffin_doneness = self.cook_levels[self.current_level]
        return  self.current_level + self.flavor + "muffin " + ": $" + self.price # string with muffin cooking level, flavor and price
    
    def __str__(self): # a string representation of the muffin object
        return self.get_description()
    


        
    

