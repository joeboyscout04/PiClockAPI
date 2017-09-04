#!piglow-env/bin/python
from flask import Flask,make_response,jsonify
from flask_restful import Api
from lightsapi import LightsAPI

#Plan out the API endpoints

#/lights

#Save favorite settings

#Control by color

#Control by arm?


app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    return "Hello, World!"

#API Routes
api.add_resource(LightsAPI, '/lights', endpoint = 'lights')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)