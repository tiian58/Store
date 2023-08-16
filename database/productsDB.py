import sqlite3

class ProductsDB:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect('database/database.db')
        conn.row_factory = sqlite3.Row
        return conn
    
    def get_products():
        conn = ProductsDB.get_db_connection()
        data = conn.execute('SELECT * FROM products').fetchall()
        conn.close()
        return data
    
    def insert_product(product):
        conn = ProductsDB.get_db_connection()
        data = conn.execute('INSERT INTO products (name, price) VALUES (?, ?)',(product.name, product.price)).fetchall()
        conn.commit()
        conn.close()
        return data
