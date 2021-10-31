from flask import Flask, request, jsonify
from appApiKey import *

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/post")
def index():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == 'aAbB-cCdD-eEfF-gGhH':
        return testpost()
        # return jsonify({"message": "Successful"})
    else:
        return jsonify({"message": "Error: Unauthorized access"})


if __name__ == '__main__':
    app.run()
