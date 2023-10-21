from flask import Flask
from controller import *
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
api.add_resource(ConstructionDataController, '/suppliers', '/<vars>', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

