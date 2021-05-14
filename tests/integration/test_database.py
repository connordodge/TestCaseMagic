import unittest
from database import Database
import os

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database('mock.db')

    def tearDown(self):
        os.remove('mock.db')

    def test_create_drop_table(self):
        self.db.create_table('cases', '(case_id int, name text, steps blob)')
        table_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="cases"'
        res = self.db.execute(table_query)[0][0]
        self.assertEqual('cases', res, "Expected the table \"cases\" to exist")
        self.db.drop_table('cases')
        res = self.db.execute(table_query)
        self.assertEqual(0, len(res), f"Expected list {res} to be empty")
