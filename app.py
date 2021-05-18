from flask import Flask
from flask_restful import Api
from case import Case
from suite import Suite

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

api.add_resource(Case, '/case', '/case/<int:case_id>')
api.add_resource(Suite, '/suite', '/suite/<int:suite_id>')

if __name__ == '__main__':
    app.run()
