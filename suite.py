from flask_restful import Resource


class Suite(Resource):

    def get(self):
        return NotImplementedError

    def post(self):
        return NotImplementedError

    def put(self):
        return NotImplementedError

    def delete(self):
        return NotImplementedError
