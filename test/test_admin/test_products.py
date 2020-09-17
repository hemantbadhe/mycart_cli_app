import unittest

from my_cart_app import TEST_MYSQL_DB_NAME

from my_cart_app.app.categories import CategoryDBManager
from my_cart_app.app.product import ProductDBManager
from my_cart_app.db_model import PRODUCT_TABLE
from test.test_db_util import create_db, create_db_schema, connection, drop_db


class TestProduct(unittest.TestCase):
    def setUp(self):
        create_db(TEST_MYSQL_DB_NAME)
        self.db_connection = connection()
        create_db_schema(self.db_connection, PRODUCT_TABLE)
        self.db_manager = ProductDBManager(self.db_connection)

    # def test_create_new_category_success(self):
    #     self.db_manager.add_product_category('Product-category-1')
    #
    #     product_categories = self.db_manager.get_product_categories()
    #     self.assertEqual(len(product_categories), 1)
    #
    # def test_create_existing_category(self):
    #     self.db_manager.add_product_category('Product-category-1')
    #     self.db_manager.add_product_category('Product-category-1')
    #
    #     product_categories = self.db_manager.get_product_categories()
    #     self.assertNotEqual(len(product_categories), 2)
    #
    # def test_get_categories(self):
    #     self.db_manager.add_product_category('Product-category-1')
    #     self.db_manager.add_product_category('Product-category-2')
    #
    #     product_categories = self.db_manager.get_product_categories()
    #     self.assertEqual(len(product_categories), 2)
    #
    # def test_get_category_by_id_success(self):
    #     self.db_manager.add_product_category('Product-category-1')
    #     obj = self.db_manager.get_product_category_by_id(1)
    #     self.assertEqual(obj[0].get('id'), 1)
    #
    # def test_get_category_by_id_fail(self):
    #     self.db_manager.add_product_category('Product-category-1')
    #     # sending wrong category id
    #     obj = self.db_manager.get_product_category_by_id(5)
    #     self.assertNotEqual(obj, 5)

    def test_get_product_by_category(self):
        pass

    def tearDown(self):
        # drop_db(self.db_connection, TEST_MYSQL_DB_NAME)
        pass

if __name__ == '__main__':
    unittest.main()
