from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#initilize the flask app
app = Flask(__name__)
#get rid of the cors error
CORS(app)

#specifying the local sqlite database storing on our machine
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
#not track all the modifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#creating the instance of the database
db = SQLAlchemy(app)