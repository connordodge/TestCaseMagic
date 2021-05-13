from flask_restful import Resource

class Case(Resource):

    def get(self):
        # TODO: validate id format
        # TODO: connect to DB
        # TODO: query for id
        # TODO: either return id if found or return 404 if not found
        return NotImplementedError

    def post(self):
        # TODO: parse arguments
        # TODO: validate arguments - Steps should be strings
        # TODO: Add test case to database
        # TODO: return 200 and test case id
        return NotImplementedError

    def put(self):
        # TODO: validate id format
        # TODO: Connect to DD
        # TODO: query for id
        # TODO: If id exists, update test case steps in database
        # TODO: if id does not exist, return 404 not found
        return NotImplementedError

    def delete(self):
        # TODO: Validate id format
        # TODO: Connect to DB
        # TODO: query for id
        # TODO: If id exists, remove from existing test suites
        # TODO: if id exists, delete test case from DB
        # TODO: if not exists, return error
        return NotImplementedError
