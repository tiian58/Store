from flask_restful import Resource
import json


class Product():
    def __init__(self,id,name,amount):
        self.id = id
        self.name = name
        self.amount = amount
    
    def __repr__(self):
        return "<Product(name={name='%s', amount='%s'})>" % (self.name, self.amount)
    
    def get(self,id):
        return products[id]
    
    def all(self):
        return products
    
    def toJSON(self):
        return json.dumps({'id': self.id(), 'name': self.name()})

# products = []
# products.append(Product(1,"Coca-Cola",2))
# products.append(Product(2,"Cookies",1))
# products.append(Product(2,"Ice-Cream",3))

