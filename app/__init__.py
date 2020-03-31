from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='./view/static', template_folder='./view/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
