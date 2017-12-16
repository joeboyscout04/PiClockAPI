# project/__init__.py

import os
from flask import Flask
from flask_restful import Api,Resource
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


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world!'}


class Development(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }
    

#API Routes
api.add_resource(HelloWorld, '/')
api.add_resource(Development, '/ping', endpoint='ping')
api.add_resource(LightsAPI, '/lights', endpoint='lights')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)