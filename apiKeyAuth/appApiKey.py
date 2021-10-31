from flask import Flask, request, jsonify
import difflib
import re

import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def hello_world():
    return 'This is my first API call!'


@app.route('/post', methods=["GET"])
def testpost():
    input_json = request.get_json(force=True)
    dictToReturn = dict(building=input_json["building"], street=input_json["street"], landmark=input_json["landmark"],
                        locality=input_json["locality"], vtc=input_json["vtc"], pincode=input_json["pincode"], district=input_json["district"],
                        state=input_json["state"])
    res = dict()
    temp = []
    name = []
    for key, val in dictToReturn.items():
        newval = re.sub(r'[@!$%^&*()<>?/|}{~:]', '', str(val))
        if newval is not None:
            lval = newval.lower()

            if key == "vtc" or key == "district" or key == "state":
                x = lval.replace(" ", "")
                y = open("./cities.txt", "r")
                name = difflib.get_close_matches(x, y)
                name1 = name[0].replace("\n", "")
                try:
                    if name1 not in temp:
                        temp.append(name1)
                        res[key] = lval.title()
                    else:
                        res[key] = None
                except IndexError:
                    print("Error")
            else:
                if lval.strip() not in temp:
                    temp.append(lval)
                    res[key] = newval.title()
                else:
                    res[key] = None
        else:
            res[key] = None
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
