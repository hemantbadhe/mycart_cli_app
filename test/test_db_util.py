from my_cart_app import *
import mysql.connector


def create_db(db_name):
    db_connection = mysql.connector.connect(
        host=TEST_MYSQL_HOST,
        user=TEST_MYSQL_USER,
        password=TEST_MYSQL_PASSWORD
    )

    mycursor = db_connection.cursor()

    mycursor.execute(f"CREATE DATABASE {db_name};")
    return mycursor


def create_db_schema(db_connection):
    query = '''
              CREATE TABLE categories(
             id INT AUTO_INCREMENT PRIMARY KEY,
             categoryName VARCHAR(100) NOT NULL);
            '''
    obj = db_connection.execute(query)


if __name__ == "__main__":
    create_db(TEST_MYSQL_DB_NAME)
