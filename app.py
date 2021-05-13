from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

if __name__ == '__main__':
    app.run()
