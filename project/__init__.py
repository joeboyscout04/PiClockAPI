# project/__init__.py

import os
from flask import Flask,make_response,jsonify
from flask_restful import Api
from api.lightsapi import LightsAPI

#Plan out the API endpoints

#/lights

#Save favorite settings

#Control by color

#Control by arm?

#instantiate the app
app = Flask(__name__)
api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


#API Routes
api.add_resource(LightsAPI, '/lights', endpoint = 'lights')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)