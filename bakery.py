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
    self.display_case.append(items)

def fill_order(self, order_item):
    pass

def display_menu(self):
    pass

def daily_summary(self):
    pass


def run_bakery():
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
    
    bakery.stock_bakery(muffins + drinks)
    # Display the menu
    bakery.display_menu()
    # Fill some example orders
    bakery.fill_order("blueberry")
    bakery.fill_order("coffee")
    # Show the updated menu and daily summary
    bakery.display_menu()
    bakery.daily_summary()

# Example usage
if __name__ == "__main__":
    run_bakery()