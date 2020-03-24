from flask import Flask

from fuca import routes

app = Flask(__name__)

#TODO: Generate real random key
app.config['SECRET_KEY'] = '1234'
