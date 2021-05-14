import sqlite3
from flask_restful import Resource

class Database(Resource):
    def __init__(self):
        raise NotImplementedError

    def connect_to_db(self):
        raise NotImplementedError

    def create_table(self, table_name, schema_tuple):
        raise NotImplementedError

    def drop_table(self, table_name):
        raise NotImplementedError

    def insert_entry(self, insert_query, data):
        raise NotImplementedError

    def update_entry(self, update_query, data):
        raise NotImplementedError

    def delete_entry(self, delete_query):
        raise NotImplementedError
