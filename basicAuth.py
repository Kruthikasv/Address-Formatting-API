from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from appBasicAuth import *

app = Flask(__name__)
api = Api(app, prefix="/api")
auth = HTTPBasicAuth()
app.config['JSON_SORT_KEYS'] = False

USER_DATA = {
    "admin": "password"
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


class Resource(Resource):
    @auth.login_required
    def get(self):
        return testpost()


api.add_resource(Resource, '/post')

if __name__ == "__main__":
    app.run(debug=True)
