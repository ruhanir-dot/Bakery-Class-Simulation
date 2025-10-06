class Muffin: # muffin class --> flavor, price, cook level
    def __init__(self, flavor, price): # initilizing muffin
        self.flavor = flavor
        self.price = price
        self.cook_levels = ["underdone", "well done", "overdone"] # cooking levels
        self.current_level = 0 # since they start underdone current level is index 0
    
    def bake_muffin(self):# baking da muffin
        if self.current_level < len(self.cook_levels) - 1: # want to only go one uo if we are underdone, don't want to overdone
            self.current_level += 1
    
    def get_description(self): # description of muffin
        cooking_status = self.cook_levels[self.current_level]
        return f"{cooking_status} {self.flavor} muffin priced at ${self.price:.2f}"
    
    def __str__(self): # string representation of muffin!
        return self.flavor
    


        
    

