from flask_restful import Resource,reqparse
import piglow


class LightsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for color, number in piglow.colours.iteritems():
            self.reqparse.add_argument(color, type=int, default=0, location='json')

        super(LightsAPI,self).__init__()

    def _get_leds(self):
        led_values = piglow.get()
        return_values = {}
        for i in range(len(led_values)):
            led_value = led_values[i]
            for color, number in piglow.colours.iteritems():
                if number == ((i % 6) - 1):
                    return_values[color] = led_value

        return return_values

    def get(self):
        return _get_leds()

    def post(self):
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            piglow.colour(k,v)

        piglow.show()
        return _get_leds(self)
        


