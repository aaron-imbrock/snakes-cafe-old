
from sys import exit
from textwrap import dedent

class Menu(object):
    def __init__(self):
        self.appetizers = ['Appetizers','----------','Wings', 'Cookies', 'Spring Rolls']
        self.entrees = ['Entrees','-------','Salmon','Steak','Meat Tornado','A Literal Garden']
        self.desserts = ['Desserts','--------','Ice Cream','Cake','Pie']
        self.drinks = ['Drinks', '------', 'Coffee', 'Tea','Unicorn Tears']

    def is_on_menu(self, item):
        if item in [*self.appetizers, *self.entrees, *self.desserts, *self.drinks]:
            return True
        return False

    def _print_list(self, _list):
        for item in _list:
            print(item)
        print()
    
    def print_menu(self):
        intro = f'''
        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **                                  **
        ** To quit at any time, type "quit" **
        **************************************
        '''
        print(dedent(intro))
        self._print_list(self.appetizers)
        self._print_list(self.entrees)
        self._print_list(self.desserts)
        self._print_list(self.drinks)

class Order():
    def __init__(self):
        self.menu = Menu()
        self.prompt = '> '
        self.order_prompt = f'''
        ***********************************
        ** What would you like to order? **
        ***********************************
        {self.prompt}'''

        self.order = {}

    def print_intro(self):
        print(dedent(self.order_prompt))

    def take_order(self, item):
        if menu.is_on_menu(item):
            # Add item and item count to order{}
            # dict default(1) if key not already present otherwise increment count +1
            # if item_count != 1, print({item_count} orders of {item} added to order.
            # else print({item_count} orders of {item} added to order.

            ## while loop w/ input(self.prompt)
            ## handle "quit", Ctrl-D, exit()

            print("Yes")
            return
        print("No")

if __name__ == "__main__":

    menu = Menu()
    order = Order()
    menu.print_menu()
    order.print_intro()
    order.take_order('Salmon')

