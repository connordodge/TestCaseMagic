import json

from flask import jsonify
from flask_restful import Resource
from helpers import id_is_valid
from database import Database

MAGIC_DB = "test_case_magic.db"


class Suite(Resource):

    def get(self, suite_id):
        if not id_is_valid(suite_id):
            return {"message": "bad request"}, 400
        db = Database(MAGIC_DB)
        suite = db.get_suite(suite_id)
        if len(suite) > 0:
            return_suite = {
                "suite_id": suite[0][0],
                "name": suite[0][1],
                "steps": json.loads(suite[0][2])
            }
            return jsonify(return_suite)
        else:
            return {"message": "Item not found"}, 404

    def post(self):
        # TODO: parse arguments
        # TODO: validate arguments - case list should have valid ids, or can be empty
        # TODO: Add test suite to database
        # TODO: Add test cases to relations table
        # TODO: return 200 and test case id
        return NotImplementedError

    def put(self):
        # TODO: validate id format
        # TODO: Connect to DD
        # TODO: query for id
        # TODO: If id exists, update test cases in relations table
        # TODO: if id does not exist, return 404 not found
        return NotImplementedError

    def delete(self):
        # TODO: Validate id format
        # TODO: Connect to DB
        # TODO: query for id
        # TODO: if id exists, delete test case from DB
        # TODO: if not exists, return error
        return NotImplementedError
