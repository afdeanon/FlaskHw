from flask import Flask

myobj = Flask(__name__)
myobj.config['SECRET_KEY'] = 'secret'
from app import routes
