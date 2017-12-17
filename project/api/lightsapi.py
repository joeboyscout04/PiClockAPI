from flask_restful import Resource,reqparse
import piglow


class LightsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for color in piglow.colours:
            self.reqparse.add_argument(color, type=int, default=0, location='json')

        super(LightsAPI,self).__init__()

    def _get_leds(self):
        # assume all colors have same value, just take first set of LEDs
        led_values = piglow.get()[:5]
        return_values = {}
        for i in range(len(led_values)):
            led_value = led_values[i]
            for color in piglow.colours:
                number = piglow.colours[color]
                if number == i:
                    return_values[color] = led_value

        return return_values

    def get(self):
        return self._get_leds()

    def post(self):
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            piglow.colour(k,v)

        piglow.show()
        return self._get_leds()
        


