import unittest

from my_cart_app.app.product import ProductDBManager


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.db_manager = ProductDBManager()

    def test_sum(self):
        self.assertEqual(2 + 3, 5)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
