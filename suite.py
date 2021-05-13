from flask_restful import Resource


class Suite(Resource):

    def get(self):
        # TODO: Validate id format
        # TODO: connect to DB
        # TODO: query for id
        # TODO: either return id if found or return 404 if not found
        # TODO: return object should include case name, description, and a list of case ids
        return NotImplementedError

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
