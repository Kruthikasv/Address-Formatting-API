from flask import Flask
from flask_restful import Resource, Api
from appBasicAuth import *

app = Flask(__name__)
api = Api(app, prefix="/api")


class Resource(Resource):
    def get(self):
        return testpost()


api.add_resource(Resource, '/post')

if __name__ == '__main__':
    app.run(debug=True)
