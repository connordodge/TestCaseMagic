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

    def get_case(self, case_id):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        get_case_query = '''
            SELECT *
            from cases
            WHERE case_id = ?
        '''
        rows = cursor.execute(get_case_query, (case_id,)).fetchall()
        connection.commit()
        connection.close()
        return rows

    def insert_case(self, name, steps):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        query = "INSERT INTO cases(name, steps) VALUES (?, ?)"
        cursor.execute(query, (name, steps))
        count = cursor.lastrowid
        connection.commit()
        connection.close()
        return count

    def update_case(self, case_id, name, steps):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        query = '''
            UPDATE cases
            SET name = ?, steps = ?
            WHERE case_id = ?
        '''
        cursor.execute(query, (name, steps, case_id))
        connection.commit()
        connection.close()

    def delete_case(self, case_id):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        delete_query = '''
            DELETE from cases
            WHERE case_id = ?
        '''
        cursor.execute(delete_query, (case_id,))
        connection.commit()
        connection.close()

    def insert_suite(self, suite_name):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        query = "INSERT INTO suites (name) VALUES (?)"
        cursor.execute(query, (suite_name,))
        connection.commit()
        connection.close()

    def update_suite(self, suite_id, suite_name):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        query = '''
            UPDATE suites
            SET name = ?
            WHERE suite_id = ?
        '''
        cursor.execute(query, (suite_name, suite_id))
        connection.commit()
        connection.close()

    def delete_suite(self, suite_id):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        delete_query = '''
            DELETE from suites
            WHERE suite_id = ?
        '''
        cursor.execute(delete_query, (suite_id,))
        delete_from_relations_table_query = '''
            DELETE from case_suite_relations
            WHERE suite_id = ?
        '''
        cursor.execute(delete_from_relations_table_query, (suite_id,))
        connection.commit()
        connection.close()

    def add_or_update_cases_to_suite(self, case_ids, suite_id):
        add_query = '''
            INSERT INTO case_suite_relations (suite_case_order, case_id, suite_id) VALUES (?, ?, ?)
        '''

        update_query = '''
            UPDATE case_suite_relations
            SET suite_case_order = ?
            WHERE case_id = ? and suite_id = ?
        '''
        connection = self.connect_to_db()
        cursor = connection.cursor()

        for index, case_id in enumerate(case_ids):
            try:
                cursor.execute(add_query, (index+1, case_id, suite_id)) #index +1 is to account for 0 indexed
            except Exception as e:
                cursor.execute(update_query, (index+1, case_id, suite_id)) #index +1 is to account for zero indexed
        connection.commit()
        connection.close()
