import unittest
import helpers


class TestIdIsValidHelper(unittest.TestCase):

    def test_id_is_valid_int(self):
        is_valid = helpers.id_is_valid(1)
        self.assertEqual(True, is_valid, "Expected id_is_valid(1) to be True")

    def test_id_is_valid_negative(self):
        is_valid = helpers.id_is_valid(-1)
        self.assertEqual(False, is_valid, "Expected id_is_valid(-1) to be False")

    def test_id_is_valid_string(self):
        is_valid = helpers.id_is_valid("1")
        self.assertEqual(True, is_valid, "Expected id_is_valid(\"1\") to be False")

    def test_id_is_valid_zero(self):
        is_valid = helpers.id_is_valid(0)
        self.assertEqual(True, is_valid, "Expected id_is_valid(0) to be False")

    def test_id_is_valid_float(self):
        is_valid = helpers.id_is_valid(1.0)
        self.assertEqual(True, is_valid, "Expected id_is_valid(1.0) to be False")