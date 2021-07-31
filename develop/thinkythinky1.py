
intro = f'''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
'''

prompt = '> '
order_prompt = f'''
***********************************
** What would you like to order? **
***********************************
{prompt}'''

class Menu:
    def __init__(self):
        self.appetizers = ['Appetizers','----------','Wings', 'Cookies', 'Spring Rolls']
        self.entrees = ['Entrees','-------','Salmon','Steak','Meat Tornado','A Literal Garden']
        self.desserts = ['Desserts','--------','Ice Cream','Cake','Pie']
        self.drinks = ['Drinks', '------', 'Coffee', 'Tea','Unicorn Tears']

    def is_on_menu():
        pass

class Order:
    def __init__(self):
        order = {}
    
    def add_to_order():
        pass

def menu_item_exists(item):
    if item in [*appetizers, *entrees, *desserts, *drinks]:
        return True
    return False

def update_order(item):


def extract_list(_list):
    for item in _list:
        print(item)
    print()

def print_menu(a_list, b_list, c_list, d_list):
    print(intro)
    extract_list(a_list)
    extract_list(b_list)
    extract_list(c_list)
    extract_list(d_list)

if __name__ == "__main__":
    print_menu(appetizers, entrees, desserts, drinks)
    print(intro)
    menu_item = input(prompt)
    if menu_item_exists(menu_item):
