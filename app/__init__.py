from flask import Flask
from config import Config
myobj = Flask(__name__)
myobj.config(
	SECRET_KEY='It is a secret'
)
from app import routes
