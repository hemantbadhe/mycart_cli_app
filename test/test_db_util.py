from my_cart_app import *
import mysql.connector

from my_cart_app.db_model import CATEGORY_TABLE


def create_db(db_name):
    db_connection = mysql.connector.connect(
        host=TEST_MYSQL_HOST,
        user=TEST_MYSQL_USER,
        password=TEST_MYSQL_PASSWORD
    )

    mycursor = db_connection.cursor()

    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    return db_connection


def connection():
    config = {
        "user": TEST_MYSQL_USER,
        "password": TEST_MYSQL_PASSWORD,
        "host": TEST_MYSQL_HOST,
        "port": TEST_MYSQL_PORT,
        "database": TEST_MYSQL_DB_NAME
    }
    try:
        c = mysql.connector.connect(**config)
        return c
    except:
        print("connection error")
        exit(1)


def create_db_schema(db_connection, table):
    mycursor = db_connection.cursor()
    mycursor.execute(table)


def drop_db(db_connection, db_name):
    mycursor = db_connection.cursor()
    mycursor.execute(f"DROP DATABASE IF EXISTS {db_name};")


if __name__ == "__main__":
    create_db(TEST_MYSQL_DB_NAME)
