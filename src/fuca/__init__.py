from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#TODO: Generate real random key
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from fuca import routes