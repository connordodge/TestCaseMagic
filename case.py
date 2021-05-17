from flask import jsonify
from flask_restful import Resource, reqparse
from helpers import id_is_valid
from database import Database
import json

class Case(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="The test case needs a name"
                        )
    parser.add_argument('steps',
                        action='append',
                        location='json'
                        )

    def get(self, id):
        if not id_is_valid(id):
            return {"message": "bad request"}, 400
        db = Database("test_case_magic.db")
        case = db.get_case(id)
        if len(case) > 0:

            return_case = {
                "case_id": case[0][0],
                "name": case[0][1],
                "steps": json.loads(case[0][2])
            }
            return jsonify(return_case)
        else:
            return {"message": "Item not found"}, 404

    def post(self):
        data = Case.parser.parse_args()
        print(data['steps'])
        dictionary_steps = self.parse_steps(data['steps'])
        db = Database("test_case_magic.db")
        id = db.insert_case(data['name'], json.dumps(dictionary_steps))
        return_obj = {'case_id': id, 'name': data['name'], 'steps': dictionary_steps}
        return_obj = jsonify(return_obj)
        return return_obj

    def put(self, id):
        if not id_is_valid(id):
            return {"message": "bad request"}, 400
        # TODO: Connect to DD
        # TODO: query for id
        # TODO: If id exists, update test case steps in database
        # TODO: if id does not exist, return 404 not found
        return NotImplementedError

    def delete(self, id):
        # TODO: Validate id format
        # TODO: Connect to DB
        # TODO: query for id
        # TODO: If id exists, remove from existing test suites
        # TODO: if id exists, delete test case from DB
        # TODO: if not exists, return error
        return NotImplementedError

    def parse_steps(self, steps):
        dictionary_steps = []
        for step in steps:
            step = step.replace("'", "\"")
            step = json.loads(step)
            dictionary_steps.append(step)
        return dictionary_steps
