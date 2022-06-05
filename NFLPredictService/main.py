from flask import Flask, jsonify
from flask_restful import Api, Resource
import datetime as DT
from flask_cors import CORS
from TrainModel import predict

app = Flask(__name__)

CORS(app, supports_credentials=True)
# Instantiate an Api object to create and manage RESTful apis
api = Api(app)

RESULT = ""


@app.route("/result", methods=["POST"])
def result():
    global RESULT
    data = "no data"
    if RESULT.strip() != "":
        data_list = RESULT.split("\n")
        data_2w_list = [i.strip().split(" ") for i in data_list]
        data_2w_list_copy = []
        for i in data_2w_list:
            temp = []
            for j in i:
                if j.strip() != "":
                    temp.append(j.strip())
                #if len(temp) > 0:
                #    if not (temp[-1] == "" and j.strip() == "" ) :
               #        temp.append(j.strip())
                #else:
                #    temp.append(j.strip())
            if len(temp):
                data_2w_list_copy.append(temp)
        print(data_2w_list_copy)
        data = """
            <table border="0" style="color: white !important;">
                <tr><th></th><th>{}</th><th>{}</th><th>{}</th><th>{}</th></tr>
                <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>
                <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>
                <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>
                <br>
                <tr><td>{}</td><td></td><td></td><td>{}</td><td>{}</td></tr>
                <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>
                <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>
            </table>
        """.format(*data_2w_list_copy[0], *data_2w_list_copy[1], *data_2w_list_copy[2],
                   *data_2w_list_copy[3], *data_2w_list_copy[4], data_2w_list_copy[5][0] + " " + data_2w_list_copy[5][1], *data_2w_list_copy[5][2:],
                   data_2w_list_copy[6][0] + " " + data_2w_list_copy[6][1], *data_2w_list_copy[6][2:])
    return jsonify(data=data)


class NFLPredict(Resource):
    def options(self):
        return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                     'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                     'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
                                     }

    def get(self, team, quarter, yardline, qtrseconds, down, goalsel, yardtogo, margin):
        global RESULT
        RESULT = ""
        result1, RESULT = predict(
            team, quarter, yardline, qtrseconds, down, goalsel, yardtogo, margin)
        return {'msg': 'success', 'data': result1}


api.add_resource(NFLPredict, '/predict/<string:team>/<int:quarter>/<int:yardline>/<int:qtrseconds>/<int:down>/<int:goalsel>/<int:yardtogo>/<int:margin>')

if __name__ == '__main__':
    app.run(debug=False)