from flask import Flask

myobj = Flask(__name__)
myobj.config
myobj.config(
	SECRET_KEY='It is a secret'
)
from app import routes
