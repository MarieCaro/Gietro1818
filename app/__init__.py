from flask import Flask
from config import CONFIG
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
static = os.path.join(chemin_actuel, "static")


app = Flask(__name__, template_folder=templates, static_folder=static)
app.config.from_object(CONFIG)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['DEBUG'] = True



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../gietro.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)


from app import routes, models