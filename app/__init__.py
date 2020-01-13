from flask import Flask, jsonify, Response, json, make_response
from config import CONFIG
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource
import os


chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
static = os.path.join(chemin_actuel, "static")


app = Flask(__name__, template_folder=templates, static_folder=static)
api = Api(app=app)
cors = CORS(app)
app.config.from_object(CONFIG)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../gietro.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class GetManifest(Resource):
    def get(self, cote):
        with open ("app/manifest/" + cote + ".json") as manifeste:
            d = json.load(manifeste)
            return make_response(jsonify(d), 200)

class GetImage(Resource):
    def get(self, cote):
        return()


api.add_resource(GetManifest, '/api/manifest/<cote>')



from app import routes, models



