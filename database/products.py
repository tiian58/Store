from .connection import create_connection

def get_products():
    return 
    # conn = create_connection()
    # sql = "SELECT * FROM products"
    # try:
    #     conn.row_factory = sqlite3.Row
    #     cur = conn.cursor()
    #     cur.execute(sql)
    #     product_rows = cur.fetchall()
    #     products = [dict(row) for row in product_rows]
    #     return products
    # except Error as e:
    #     print("Error get products")
    #     return false
    # finally:
    #     if conn:
    #         cur.close()
    #         conn.close()
