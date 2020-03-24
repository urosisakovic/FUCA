from flask import Flask
app = Flask(__name__)

#TODO: Generate real random key
app.config['SECRET_KEY'] = '1234'

from fuca import routes