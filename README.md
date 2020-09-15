# my cart ecommerce app

>Steps to run the app

1. Clone the latest code
2. Create a virtualenv using ```virtualenv -p python3 <venv_name>```
3. Activate the venv using, ```source <venv_name>/bin/activate```
4. Install the requiremets using, ```pip install -r requirements.txt```
5. Install the current codebase using, ```python setup.py develop```

> App(Flow-1)
1. to run the app(customer app), navigate to ```mycart_cli_app/my_cart_app/app```
then run the ```main.py``` using, ```python main.py```
2. Once the app the app is running, the menu list will be shown.
3. Option 1 will display the all available product categories.
4. Option 2 will display the products category wise, need to enter the category id once the choice is selected.
5. Option 3 will display the product details, need to enter the product id once the choice is selected.
6. Option 4 is for, adding the product to the cart, need to enter the product id once the choice is selected.
7. Option 5 will diaplay the products list which is added in cart.
8. Option 6 is for removing the product from cart, need to enter the produc id once the choice is selected.
9. Option 7 is for generating the bill, need to enter the user's name for billing generation process once the choice is selected.

> App(Flow-2)
1. to run the app(admin app), navigate to ```mycart_cli_app/my_cart_app/admin```
then run the ```main.py``` using, ```python main.py```
2. Once the app the app is running, the menu list will be shown.
3. Option 1 is for adding the new brand product category, need to enter category name, once the choice is selected.
4. Option 2 is adding the new brand product, need to enter product name, once the choice is selected, after it will ask for 'product name', then it will ask for the product price. then it will ask for product description, here the product description is taken in dictionary(key-value format), so firstly we need to specify numbers of fields, acording it will ask for the key & value.
5. Option 3 is for displaying the user cart details.
6. Option 4 is for, displaying the bills genarated by the user.
