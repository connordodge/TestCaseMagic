from flask import jsonify
from flask_restful import Resource, reqparse
from helpers import id_is_valid
from database import Database
import json
from json.decoder import JSONDecodeError

MAGIC_DB = "test_case_magic.db"


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

    def get(self, case_id):
        if not id_is_valid(case_id):
            return {"message": "bad request"}, 400
        db = Database(MAGIC_DB)
        case = db.get_case(case_id)
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
        dictionary_steps = self.parse_steps(data['steps'])
        print(dictionary_steps)
        db = Database(MAGIC_DB)
        id = db.insert_case(data['name'], json.dumps(dictionary_steps))
        return_obj = {'case_id': id, 'name': data['name'], 'steps': dictionary_steps}
        return_obj = jsonify(return_obj)
        return return_obj

    def put(self, case_id):
        if not id_is_valid(case_id):
            return {"message": "bad request"}, 400
        db = Database(MAGIC_DB)
        case = db.get_case(case_id)
        if len(case) > 0:
            data = Case.parser.parse_args()
            dictionary_steps = self.parse_steps(data['steps'])
            print(dictionary_steps)
            db.update_case(case_id, data['name'], json.dumps(dictionary_steps))
            return 200
        else:
            return {"message": "Item not found"}, 404

    def delete(self, case_id):
        if not id_is_valid(case_id):
            return {"message": "bad request"}, 400
        db = Database(MAGIC_DB)
        db.delete_case(case_id)
        return 200

    def parse_steps(self, steps):
        dictionary_steps = []
        for step in steps:
            step = step.replace("'", "\"")
            try:
                step = json.loads(step)
            except JSONDecodeError:
                raise
            dictionary_steps.append(step)
        return dictionary_steps


