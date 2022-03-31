from flask import Flask

myobj = Flask(__name__)
myobj.config(
	SECRET_KEY='It's a secret'
)
from app import routes
