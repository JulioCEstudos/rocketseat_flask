from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
db.init_app(app)


@app.route("/hello-world", methods=["GET"])
def hello_world():