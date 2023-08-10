import sqlite3, sys
from sqlite3 import Error

def create():
    try:
        connection = sqlite3.connect('database.db')

        with open('sql/tables.sql') as f:
            print(f.read())
            connection.executescript(f.read())
            
        cur = connection.cursor()
        cur.execute("INSERT INTO products (name, price) VALUES (?, ?)",('Cookies', 5))
        print("OK")
        connection.commit()
        connection.close()
    except Error as e:
        print("Error db: " + str(e))

if __name__== "__main__":
        create()