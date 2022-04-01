from flask import Flask

myobj = Flask(__name__)
myobj.config['SECRET_KEY'] = 'ThisIsATest'
from app import routes
