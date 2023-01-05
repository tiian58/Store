from flask import Flask, request, jsonify

from models.product import Product

app = Flask(__name__)

#products = {
#     1:{"id":1, "Name": "Coca-Cola", "Amount": 5},
#     2:{"id":2, "Name": "Cookie", "Amount": 1}
#}
products = [
     {"Id":1, "Name": "Coca-Cola", "Amount": 5},
     {"Id":2, "Name": "Cookie", "Amount": 1}
]

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({'response':'welcome'}), 200

@app.route("/products", methods=["GET"])
def get_products():
    data = products
    if data:
        return jsonify(data), 200
    elif data == False:
        return jsonify({'message': 'Error'}), 500
    else:
        return jsonify({'products': {}})

@app.route("/products", methods=["POST"])
def insert_products():
    products.append(request.get_json())
    if products:
        return jsonify(products), 201
    elif products == False:
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