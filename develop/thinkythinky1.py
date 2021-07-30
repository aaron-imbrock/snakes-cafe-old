

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

appetizers = ['Appetizers','----------','Wings', 'Cookies', 'Spring Rolls']
entrees = ['Entrees','-------','Salmon','Steak','Meat Tornado','A Literal Garden']
desserts = ['Desserts','--------','Ice Cream','Cake','Pie']
drinks = ['Drinks', '------', 'Coffee', 'Tea','Unicorn Tears']

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
    

