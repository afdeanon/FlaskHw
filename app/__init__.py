from flask import Flask
myobj.config
myobj = Flask(__name__)
myobj.config(
	SECRET_KEY='It is a secret'
)
from app import routes
