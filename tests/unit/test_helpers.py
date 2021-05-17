import unittest
import helpers
from case import Case


class TestIdIsValidHelper(unittest.TestCase):

    def test_id_is_valid_int(self):
        is_valid = helpers.id_is_valid(1)
        self.assertEqual(True, is_valid, "Expected id_is_valid(1) to be True")

    def test_id_is_valid_negative(self):
        is_valid = helpers.id_is_valid(-1)
        self.assertEqual(False, is_valid, "Expected id_is_valid(-1) to be False")

    def test_id_is_valid_string(self):
        is_valid = helpers.id_is_valid("1")
        self.assertEqual(False, is_valid, "Expected id_is_valid(\"1\") to be False")

    def test_id_is_valid_zero(self):
        is_valid = helpers.id_is_valid(0)
        self.assertEqual(False, is_valid, "Expected id_is_valid(0) to be False")

    def test_id_is_valid_float(self):
        is_valid = helpers.id_is_valid(1.0)
        self.assertEqual(False, is_valid, "Expected id_is_valid(1.0) to be False")

class TestParseSteps(unittest.TestCase):

    def test_valid_steps(self):
        case = Case()
        steps = ["{'type': 'ACTION', 'description': 'navigate to /auth'}", "{'type': 'ASSERTION', 'description': 'username and password fields exist'}", "{'type': 'ACTION', 'description': 'type correct username into username field and correct password into password field'}", "{'type': 'ACTION', 'description': 'Press Login button'}", "{'type': 'ASSERTION', 'description': 'should be successfully logged in'}"]
        steps_dict = case.parse_steps(steps)
        self.assertIsInstance(steps_dict[0], dict, f"Expected {type(steps_dict[0])} to be type dict")