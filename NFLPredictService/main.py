from flask import Flask
from flask_restful import Api, Resource
import datetime as DT
from flask_cors import CORS
from TrainModel import predict

app = Flask(__name__)

CORS(app, supports_credentials=True)
# Instantiate an Api object to create and manage RESTful apis
api = Api(app)


class NFLPredict(Resource):
    def options(self):
        return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                     'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                     'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
                                     }

    def get(self, team, quarter, yardline, qtrseconds, down, goalsel, yardtogo, margin):
        result = predict(team, quarter, yardline, qtrseconds, down, goalsel, yardtogo, margin)
        return {'msg':'success', 'data': result}


api.add_resource(NFLPredict, '/predict/<string:team>/<int:quarter>/<int:yardline>/<int:qtrseconds>/<int:down>/<int:goalsel>/<int:yardtogo>/<int:margin>')

if __name__ == '__main__':
    app.run(debug=False)