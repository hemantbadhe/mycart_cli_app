from my_cart_app import db_connection


class CategoryManager:
    def __init__(self):
        self.db_manager = CategoryDBManager()

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
    def __init__(self):
        self.__cursor = db_connection.cursor()
        self.__util = CategoryUtil

    def get_product_categories(self):
        query = f"SELECT * FROM categories;"
        self.__cursor.execute(query)
        categories = self.__util.get_product_categories_from_cursor(self.__cursor)
        db_connection.commit()
        if categories:
            return categories
        return None

    def get_product_category_by_id(self, category_id):
        query = f"SELECT id FROM categories where id={category_id};"
        self.__cursor.execute(query)
        categories = self.__util.get_product_categories_from_cursor(self.__cursor)
        if categories:
            return categories
        return None

    def add_product_category(self, category_name):
        insert_query = f"INSERT INTO categories (categoryName)SELECT * FROM (SELECT '{category_name}') AS tmp " \
                       f"WHERE NOT EXISTS (SELECT categoryName FROM categories WHERE categoryName = '{category_name}')" \
                       f" LIMIT 1;"
        self.__cursor.execute(insert_query)
        db_connection.commit()

        if self.__cursor.rowcount == 0:
            return "Product categories already exists."

        return "Product categories added successfully."

