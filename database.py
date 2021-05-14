import sqlite3
from flask_restful import Resource

class Database(Resource):
    def __init__(self, db_name):
        self.db_name = db_name

    def execute(self, sql_string):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        rows = cursor.execute(sql_string).fetchall()
        connection.commit()
        connection.close()
        return rows

    def connect_to_db(self):
        connection = sqlite3.connect(self.db_name)
        return connection

    def create_table(self, table_name, schema_tuple):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} {schema_tuple}"
        cursor.execute(create_table_query)
        connection.commit()
        connection.close()

    def drop_table(self, table_name):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
        cursor.execute(drop_table_query)
        connection.commit()
        connection.close()

    def insert_entry(self, insert_query, data):
        raise NotImplementedError

    def update_entry(self, update_query, data):
        raise NotImplementedError

    def delete_entry(self, delete_query):
        raise NotImplementedError
