import pprint

from my_cart_app.app.billing import BillingManager
from my_cart_app.app.cart import CartManager
from my_cart_app.app.categories import CategoryManager
from my_cart_app.app.product import ProductManager


def my_cart(choice):
    switcher = {
        1: lambda: CategoryManager().get_product_categories(),
        2: lambda: ProductManager().get_product_category_id_and_return_product_details(),
        3: lambda: ProductManager().get_product_id_and_return_product_detail(),
        4: lambda: CartManager().add_product_into_cart(),
        5: lambda: CartManager().get_product_from_cart(),
        6: lambda: CartManager().remove_product_from_cart(),
        7: lambda: BillingManager().create_bill(),
    }
    return switcher.get(choice, lambda: 'Invalid')()


if __name__ == '__main__':
    while True:
        print('\n---------------MyCart E-commerce app---------------')
        print('\n1. List of categories')
        print('2. View product category wise')
        print('3. View product details')
        print('4. Add products to cart')
        print('5. Display added product in cart')
        print('6. Remove Product from cart')
        print('7. Buy product from cart(billing)')
        print('---------------------------------------------------')

        choice = int(input('Enter your choice: '))
        data = my_cart(choice)
        print('\n')
        pprint.pprint(data)

