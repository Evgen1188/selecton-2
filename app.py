from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import csv

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
CORS(app, resources={"/*": {"origins": "*"}})


class Main(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_cue', required=True)
        data = parser.parse_args()
        # log_string = get_prediction(user_cue)
        with open("logs.csv", "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([data['user_cue'], "log_string"])
        return {'user_cue': data['user_cue'], "log_string": "log_string"}


api.add_resource(Main, '/')
