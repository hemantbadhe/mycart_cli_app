CATEGORY_TABLE = f"CREATE TABLE IF NOT EXISTS categories(id INT AUTO_INCREMENT PRIMARY KEY, categoryName " \
                 f"VARCHAR(100) NOT NULL);"

PRODUCT_TABLE = """
                    CREATE TABLE IF NOT EXISTS products(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    productName varchar(100) not null,
                    price FLOAT NOT NULL,
                    description JSON NULL,
                    category INT,
                    CONSTRAINT fk_category
                    FOREIGN KEY (category) 
                        REFERENCES categories(id),
                );
                """
