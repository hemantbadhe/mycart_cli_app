from my_cart_app import db_connection


class CategoryManager:
    def __init__(self):
        self.cursor = db_connection.cursor()
        self.db_manager = CategoryDBManager(self.cursor)

    def get_product_categories(self):
        return self.db_manager.get_product_categories()

    def get_product_category_by_id(self, category_id=None):
        if not category_id:
            category_id = int(input('Enter category_id'))
        return self.db_manager.get_product_category_by_id(category_id)

    def add_product_category(self):
        category_name = str(input('Enter category name: '))
        return self.db_manager.add_product_category(category_name)


class CategoryUtil:
    @staticmethod
    def get_product_categories_from_cursor(db_cursor):
        columns = [col[0] for col in db_cursor.description]
        return [dict(zip(columns, row)) for row in db_cursor.fetchall()]


class CategoryDBManager:
    def __init__(self, connection):
        self.connection = connection
        self._util = CategoryUtil

    def get_product_categories(self):
        query = f"SELECT * FROM categories;"
        cursor = self.connection.cursor()
        cursor.execute(query)
        categories = self._util.get_product_categories_from_cursor(cursor)
        db_connection.commit()
        if categories:
            return categories
        return None

    def get_product_category_by_id(self, category_id):
        query = f"SELECT id FROM categories where id={category_id};"
        cursor = self.connection.cursor()
        cursor.execute(query)
        categories = self._util.get_product_categories_from_cursor(cursor)
        if categories:
            return categories
        return None

    def add_product_category(self, category_name):
        insert_query = f"INSERT INTO categories (categoryName)SELECT * FROM (SELECT '{category_name}') AS tmp " \
                       f"WHERE NOT EXISTS (SELECT categoryName FROM categories WHERE categoryName = '{category_name}')" \
                       f" LIMIT 1;"
        cursor = self.connection.cursor()
        cursor.execute(insert_query)
        db_connection.commit()

        if cursor.rowcount == 0:
            return "Product categories already exists."

        return "Product categories added successfully."

