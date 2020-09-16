import unittest

from my_cart_app import TEST_MYSQL_DB_NAME

from my_cart_app.app.categories import CategoryDBManager
from test.test_db_util import create_db, create_db_schema


class TestCategory(unittest.TestCase):
    def setUp(self):
        db = create_db(TEST_MYSQL_DB_NAME)
        create_db_schema(db)
        self.db_manager = CategoryDBManager(db)

    def test_get_categories(self):
        self.db_manager.add_product_category('Product-category-1')
        self.db_manager.add_product_category('Product-category-2')

        product_categories = self.db_manager.get_product_categories()

        self.assertEqual(len(product_categories), 2)

    def test_get_category_by_id_success(self):
        pass

    def test_get_category_by_id_fail(self):
        pass

    def tearDown(self):
        # drop db
        pass


if __name__ == '__main__':
    unittest.main()
