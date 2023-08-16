from flask_restful import Resource
import json


class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return "<Product(name={name='%s', amount='%s'})>" % (self.name, self.amount)
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def toJSON(self):
        return json.dumps({'id': self.id(), 'name': self.name()})


