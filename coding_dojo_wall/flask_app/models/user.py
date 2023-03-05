from flask_app.config.mysqlconnection import connectToMySQL
db = 'tables_schema'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = '''
        INSERT INTO tables(first_name,last_name,email,password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        '''
        return connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = '''
        SELECT *
        FROM tables;'''
        results = connectToMySQL(db).query_db(query)
        output = []
        for row in results:
            output.append(cls(row))
        return output
    
    @classmethod
    def get_by_id(cls,data):
        query = '''
        SELECT *
        FROM tables
        WHERE id = %(id)s;'''
        results = connectToMySQL(db).query_db(query,data)
        return cls(results)
    
    @classmethod
    def edit(cls,data):
        query = '''
        UPDATE tables
        SET column=new_Value
        WHERE id = %(id)s;'''
        connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = '''
        DELETE FROM tables
        WHERE id = %(id)s;'''
        connectToMySQL(db).query_db(query,data)