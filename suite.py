import json

from flask import jsonify
from flask_restful import Resource, reqparse
from helpers import id_is_valid
from database import Database

MAGIC_DB = "test_case_magic.db"


class Suite(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="The suite needs a string name"
                        )
    parser.add_argument('case_ids',
                        action='append',
                        # type=list,
                        location='json'
                        )

    def get(self, suite_id):
        print("here")
        if not id_is_valid(suite_id):
            return {"message": "bad request"}, 400
        db = Database(MAGIC_DB)
        suite = db.get_suite(suite_id)
        if len(suite) > 0:
            return_suite = {
                "suite_id": suite[0][0],
                "name": suite[0][1],
                "cases": suite[0][2]
            }
            return jsonify(return_suite)
        else:
            return {"message": "Item not found"}, 404

    def post(self):
        data = Suite.parser.parse_args()
        db = Database(MAGIC_DB)
        suite_id = db.insert_suite(data['name'])
        case_ids = self.parse_case_ids(data['case_ids'])
        db.add_or_update_cases_to_suite(case_ids, suite_id)
        return_obj = self.create_return_object(case_ids, data, suite_id)
        return return_obj

    def create_return_object(self, case_ids, data, suite_id):
        return_obj = {'suite_id': suite_id, 'name': data['name'], 'cases': case_ids}
        return_obj = jsonify(return_obj)
        return return_obj

    def put(self, suite_id):
        data = Suite.parser.parse_args()
        db = Database(MAGIC_DB)
        case_ids = self.parse_case_ids(data['case_ids'])
        db.add_or_update_cases_to_suite(case_ids, suite_id)
        return_obj = self.create_return_object(case_ids, data, suite_id)
        return return_obj

    def delete(self):
        # TODO: Validate id format
        # TODO: Connect to DB
        # TODO: query for id
        # TODO: if id exists, delete test case from DB
        # TODO: if not exists, return error
        return NotImplementedError

    def parse_case_ids(self, case_ids):
        int_ids = []
        for case_id in case_ids:
            case_id = int(case_id)
            int_ids.append(case_id)
        return int_ids