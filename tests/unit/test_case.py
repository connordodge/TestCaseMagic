from json.decoder import JSONDecodeError
from case import Case
import unittest


class TestParseSteps(unittest.TestCase):

    def test_valid_steps(self):
        case = Case()
        steps = ["{'type': 'ACTION', 'description': 'navigate to /auth'}",
                 "{'type': 'ASSERTION', 'description': 'username and password fields exist'}",
                 "{'type': 'ACTION', 'description': 'type correct username into username field and correct password into password field'}",
                 "{'type': 'ACTION', 'description': 'Press Login button'}",
                 "{'type': 'ASSERTION', 'description': 'should be successfully logged in'}"]
        steps_dict = case.parse_steps(steps)
        self.assertIsInstance(steps_dict[0], dict, f"Expected {type(steps_dict[0])} to be type dict")

    def test_invalid_steps(self):
        case = Case()
        invalid_steps = ["{'type':: 'ACTION', 'description': 'navigate to /auth'}",
                 "{'type': 'ASSERTION', 'description': 'username and password fields exist'}",
                 "{'type': 'ACTION', 'description': 'type correct username into username field and correct password into password field'}",
                 "{'type': 'ACTION', 'description': 'Press Login button'}",
                 "{'type': 'ASSERTION', 'description': 'should be successfully logged in'}"]
        self.assertRaises(JSONDecodeError, case.parse_steps, invalid_steps)