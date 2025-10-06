
from muffin import Muffin
from drink import Drink

class Bakery: # this our bakery class representing a bakery that sells muffins and drinks 
    def __init__(self, display_case=None, muffin_menu=None, drink_menu=None, money=0.0, sales=None):
        # initializing our parameters
        self.display_case = [] # empty list for items in display case
        self.muffin_menu = {}  # empty dictionary for muffin menu  flavor, price
        self.drink_menu = {}  # empty dictionary for drink menu  type, price
        self.money = 0.0      # starting money       
        self.sales = []       # list of today sales      

    def stock_bakery(self, items): # this is our method to stock our bakery with muffins and drinks
        for item in items: # items is our list of muffin/drink objects, and looping through each item
            
            self.display_case.append(item) # adding each item to display case

            if isinstance(item, Muffin): 
                # if object is muffin, add to muffin menu
                self.muffin_menu[item.flavor] = item.price
            elif isinstance(item, Drink):
                # if object is  drink, add to drink menu
                self.drink_menu[item.type] = item.price

    def fill_order(self, order_item): # method for filling an order
        for item in self.display_case: # looping thorugh each item of my display case
            if str(item) == order_item: # converting item to string and seeing if its the same as order
                print(f"Order filled: {order_item}. Price: ${item.price:.2f}")
                self.money += item.price # add to money earned
                self.sales.append(order_item) # add to sales list
                self.display_case.remove(item) # remove from display case
                return
        print(f"Sorry, {order_item} is out of stock.") # if not in display cse

    def display_menu(self):
        print("Muffin Menu:") # display muffin menu
        for flavor, price in self.muffin_menu.items(): # looping through muffin menu dictionary
            print(f"{flavor}: ${price:.2f}")
        
        print("\nDrink Menu:")
        for size, price in self.drink_menu.items():# looping through drink menu dictionary
            print(f"{size}: ${price:.2f}")
        
        print()

    def daily_summary(self): # method for summary of da
        print(f"Total sales today: ${self.money:.2f}")
        print("Items sold:")
        for item in self.sales:
            print(item)


def run_bakery():

    # new instance of bakery
    bakery = Bakery()

    # stocking bakery!
    muffins = [
        Muffin("blueberry", 2.50),
        Muffin("chocolate", 3.00),
    ]

    drinks = [
        Drink("medium", "coffee", 1.75),
        Drink("large", "tea", 2.00),
    ]
    
    # add items to bakery
    bakery.stock_bakery(muffins + drinks)
    
    # display menu
    bakery.display_menu()

    # filling example order
    bakery.fill_order("blueberry")
    bakery.fill_order("coffee")
    
    # displaying menu and daily summary
    bakery.display_menu()
    bakery.daily_summary()

# run bakery program
if __name__ == "__main__":
    run_bakery()