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


#API Routes
api.add_resource(LightsAPI, '/lights', endpoint = 'lights')


if __name__ == '__main__':
    app.run(debug=True)