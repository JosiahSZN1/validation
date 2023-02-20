from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'cookie_orders'
# order.py
class Order:
    def __init__(self,data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = '''
        INSERT INTO cookie_orders(customer_name,cookie_type,num_boxes)
        VALUES (%(name)s,%(cookie_type)s,%(num_boxes)s);
        '''
        connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = '''
        SELECT *
        FROM cookie_orders
        '''
        output = []
        results = connectToMySQL(mydb).query_db(query)
        print(results)
        for row in results:
            output.append(cls(row))
        print(output)
        return output
    
    @classmethod
    def get_one(cls,data):
        query = '''
        SELECT *
        FROM cookie_orders
        WHERE id = %(id)s;
        '''
        results = connectToMySQL(mydb).query_db(query,data)[0]
        print(results)
        output = cls(results)
        print(output)
        return output
    
    @classmethod
    def update(cls,data):
        query = '''
        UPDATE cookie_orders
        SET customer_name = %(name)s, cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s
        WHERE id = %(id)s;
        '''
        connectToMySQL(mydb).query_db(query,data)
    
    @staticmethod
    def validate_order(order):
        is_valid = True # we assume this is true
        if len(order['name']) < 2:
            flash("Customer name must be at least 2 characters.")
            is_valid = False
        if len(order['cookie_type']) < 2:
            flash("Cookie type must be at least 2 characters.")
            is_valid = False
        if int(order['num_boxes']) < 1:
            flash("You must order at least 1 box of cookies.")
            is_valid = False
        return is_valid