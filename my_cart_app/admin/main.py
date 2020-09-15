import pprint

from my_cart_app.app.billing import BillingManager
from my_cart_app.app.cart import CartManager
from my_cart_app.app.categories import CategoryManager
from my_cart_app.app.product import ProductManager


def my_cart(choice):
    switcher = {
        1: lambda: CategoryManager().add_product_category(),
        2: lambda: ProductManager().add_new_product(),
        3: lambda: CartManager().get_product_from_cart(),
        4: lambda: BillingManager().get_all_bills(),
    }
    return switcher.get(choice, lambda: 'Invalid')()


if __name__ == '__main__':
    while True:
        print('\n---------------MyCart E-commerce app---------------')
        print('\n1. Add product category')
        print('2. Add product')
        print("3. Display user cart details")
        print('4. Display all bills generated by user')
        print('---------------------------------------------------')

        choice = int(input('Enter your choice: '))
        data = my_cart(choice)
        print('\n')
        pprint.pprint(data)
