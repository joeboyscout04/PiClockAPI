from flask_restful import Resource,reqparse
import piglow


class LightsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('white', type=int, default=0, location='json')
        self.reqparse.add_argument('red', type=int, default=0, location='json')
        self.reqparse.add_argument('yellow', type=int, default=0, location='json')
        self.reqparse.add_argument('orange', type=int, default=0, location='json')
        self.reqparse.add_argument('blue', type=int, default=0, location='json')
        self.reqparse.add_argument('green', type=int, default=0, location='json')
        super(LightsAPI,self).__init__()

    def get(self):
        vals = piglow.get()
        #make json from this

        pass

    def post(self):
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            piglow.colour(k,v)

        piglow.show()
        return
        


