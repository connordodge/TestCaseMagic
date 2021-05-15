import json
import unittest
from database import Database
from .fixtures.case_fixture import case_fixture_1, case_fixture_2, case_fixture_3
import os

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database('mock.db')
        self.db.create_table('cases', '(case_id INTEGER PRIMARY KEY, name text, steps blob)')
        self.db.create_table('suites', '(suite_id INTEGER PRIMARY KEY, name text)')
        case_suite_relations_schema = '''
            (
                case_id INTEGER,
                suite_id INTEGER,
                suite_case_order INTEGER,
                UNIQUE(case_id, suite_id),
                FOREIGN KEY(case_id) REFERENCES cases(case_id),
                FOREIGN KEY(suite_id) REFERENCES suites(suite_id)
            )
        '''
        self.db.create_table('case_suite_relations', case_suite_relations_schema)
        test_case_steps = json.dumps(case_fixture_1)
        test_case = ("login", test_case_steps)
        self.db.insert_case(test_case)
        self.db.insert_suite("regression suite")
        # self.db.add_or_update_cases_to_suite()


    def tearDown(self):
        os.remove('mock.db')

    def test_create_table(self):
        table_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="cases"'
        res = self.db.execute(table_query)[0][0]
        self.assertEqual('cases', res, "Expected the table \"cases\" to exist")

    def test_drop_table(self):
        self.db.drop_table('cases')
        table_query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="cases"'
        res = self.db.execute(table_query)
        self.assertEqual(0, len(res), f"Expected list {res} to be empty")

    def test_insert_case(self):
        # case is already inserted in set up
        test_case_query = '''
            SELECT *
            FROM cases
            WHERE case_id = 1
        '''
        res = self.db.execute(test_case_query)
        self.assertEqual('login',res[0][1], f"Expected {res[0][1]} to equal 'login'")

    def test_update_case(self):
        self.db.update_case(1, "sign in", json.dumps(case_fixture_2))
        test_case_query = '''
            SELECT *
            FROM cases
            WHERE case_id = 1
        '''
        res = self.db.execute(test_case_query)
        self.assertEqual('sign in', res[0][1], f"Expected {res[0][1]} to equal 'sign in'")
        self.assertEqual("navigate to /signin", json.loads(res[0][2])[0]["description"], f"Expected {res[0][1]} to equal 'sign in'")

    def test_delete_case(self):
        self.db.delete_case(1)
        test_case_query = '''
            SELECT *
            FROM cases
            WHERE case_id = 1
        '''
        res = self.db.execute(test_case_query)
        self.assertEqual(0, len(res), f"Expected {res} to have length 0")

    def test_insert_suite(self):
        # case is already inserted in set up
        test_suite_query = '''
            SELECT *
            FROM suites
            WHERE suite_id = 1
        '''
        res = self.db.execute(test_suite_query)
        self.assertEqual('regression suite',res[0][1], f"Expected {res[0][1]} to equal 'regression suite'")

    def test_update_suite(self):
        self.db.update_suite(1, "regression plan")
        test_suite_query = '''
            SELECT *
            FROM suites
            WHERE suite_id = 1
        '''
        res = self.db.execute(test_suite_query)
        self.assertEqual('regression plan', res[0][1], f"Expected {res[0][1]} to equal 'sign in'")

    def test_delete_suite(self):
        self.db.delete_suite(1)
        test_suite_query = '''
            SELECT *
            FROM suites
            WHERE suite_id = 1
        '''
        res = self.db.execute(test_suite_query)
        self.assertEqual(0, len(res), f"Expected {res} to have length 0")
        relations_query = '''
                SELECT *
                FROM case_suite_relations
                WHERE suite_id = 1
            '''
        res = self.db.execute(relations_query)
        self.assertEqual(0, len(res), f"Expected {res} to have length 0")

    def test_add_case_to_suite(self):
        test_case_steps = json.dumps(case_fixture_2)
        test_case = ("sign in", test_case_steps)
        self.db.insert_case(test_case)
        self.db.add_or_update_cases_to_suite([1,2],1)
        relations_query = '''
                            SELECT *
                            FROM case_suite_relations
                            WHERE suite_id = 1
                        '''
        res = self.db.execute(relations_query)
        self.assertEqual(2, len(res), f"Expected {res} to have length 2")

    def test_update_cases_in_suite(self):
        test_case_steps = json.dumps(case_fixture_2)
        test_case = ("sign in", test_case_steps)
        self.db.insert_case(test_case)
        test_case_steps_2 = json.dumps(case_fixture_2)
        test_case_2 = ("auth", test_case_steps_2)
        self.db.insert_case(test_case_2)
        self.db.add_or_update_cases_to_suite([1, 2], 1)
        relations_query = '''
                            SELECT *
                            FROM case_suite_relations
                            WHERE suite_id = 1
                        '''
        res = self.db.execute(relations_query)
        self.assertEqual(2, len(res), f"Expected {res} to have length 2")
        self.db.add_or_update_cases_to_suite([1, 3, 2], 1)
        res = self.db.execute(relations_query)
        self.assertEqual(3, len(res), f"Expected {res} to have length 3")
        self.assertEqual(2, res[2][2], f"Expected case_id 3 to have step order 2")

