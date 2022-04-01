from flask import Flask

myobj = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
from app import routes
