import sqlite3

class Product:
    def get_products(conn):
        data = conn.execute('SELECT * FROM products').fetchall()
        conn.close()
        return data
