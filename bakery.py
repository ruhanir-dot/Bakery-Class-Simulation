from muffin import Muffin
from drink import Drink

class Bakery:
    def __init__(self, display_case=None, muffin_menu=None, drink_menu=None, money=0.0, sales=None):
        self.display_case = []
        self.muffin_menu = {} # Dictionary for muffins
        self.drink_menu = {} # Dictionary for drinks
        self.money = 0.0
        self.sales = []


def stock_bakery(self, items):
    for item in items: # iterating through items to stock bakery
        self.display_case.append(item)

        # Updating Menus
        if isinstance(item,Muffin): # checking if item is a muffin 
            self.muffin_menu[item] #if it is we are adding the flavor and price to muffin menu
        elif isinstance(item,Drink): #checking if item is a drink
            self.drink_menu[item.size] = item.price #adding size and price

def fill_order(self, order_item):
    for item in self.display_case:
    #Convert item to string and check if it matches the order
        if str(item) == order_item:
            # Found it! Process the sale
            print(f"Order filled: {order_item}. Price: ${item.price:.2f}")
                
            # Add the price to total money
            self.money += item.price
                
            # Record the sale
            self.sales.append(order_item)
                
            # Remove the item from display case (it's been sold!)
            self.display_case.remove(item)
                
            # Exit the method - order complete
            return
    print(f"Sorry, {order_item} is not available.")
   
def display_menu(self):
    print("Muffin Menu:")
    for flavor, price in self.muffin_menu.items():
        print(f"{flavor}: ${price:.2f}")
    print("\nDrink Menu:")
    for size, price in self.drink_menu.items():
        print(f"{size} drink: ${price:.2f}")

def daily_summary(self):
    print(f"Total sales today: ${self.money:.2f}")
    print("Items sold:")
    for item in self.sales:
        print(item)


def run_bakery():
    """
    Main function to run the bakery simulation.
    """
    # Create a new bakery
    bakery = Bakery()
    
    # Stock the bakery with some muffins and drinks
    muffins = [
        Muffin("blueberry", 2.50),
        Muffin("chocolate", 3.00),
    ]
    
    drinks = [
        Drink("medium", "coffee", 1.75),
        Drink("large", "tea", 2.00),
    ]
    
    # Add all items to the bakery
    bakery.stock_bakery(muffins + drinks)
    
    # Display the menu
    bakery.display_menu()
    
    # Fill some example orders
    bakery.fill_order("blueberry")
    bakery.fill_order("coffee")
    
    # Show the updated menu and daily summary
    bakery.display_menu()
    bakery.daily_summary()


# This runs the simulation when you execute the file
if __name__ == "__main__":
    run_bakery()