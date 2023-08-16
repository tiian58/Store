import sqlite3
from flask import Flask, request, jsonify

from database.productsDB import ProductsDB
from models.product import Product

app = Flask(__name__)

conn = sqlite3.connect('database/database.db')

def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({'response':'welcome'}), 200

@app.route("/products", methods=["GET"])
def get_products():
    products = ProductsDB.get_products()
    products = [list(row) for row in products]
    if products:
        return jsonify(products), 200
    elif products == False:
        return jsonify({'message': 'Error'}), 500
    else:
        return jsonify({'products': {}})

@app.route("/products", methods=["POST"])
def insert_products():
    body = request.get_json()
    prod = Product(body['name'], body['price'])
    if prod:
        ProductsDB.insert_product(prod)
        return jsonify(prod.name), 201
    elif prod == False:
        return jsonify({'message': 'Error'}), 500
    else:
        return jsonify({'products': {}})

@app.route("/products/<id>", methods=["GET"])
def get_products_id():
    data = id
    if data:
        return jsonify(data)
    elif data == False:
        return jsonify({'message': 'Error'})
    else:
        return jsonify({'products': {}})


if __name__== "__main__":
    app.run(port = 5001, debug=True)