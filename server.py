#!/usr/bin/env python

from flask import Flask, request, jsonify
app = Flask(__name__)
from validation import validate

@app.route('/', methods=['POST'])
def index():
    return jsonify(validate(request.get_json()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
