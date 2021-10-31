from flask import Flask
from flask_restful import Resource, Api
from app import *

app = Flask(__name__)
api = Api(app, prefix="/apiAuth")


class PrivateResource(Resource):
    def get(self):
        return testpost()


api.add_resource(PrivateResource, '/post')

if __name__ == '__main__':
    app.run(debug=True)
