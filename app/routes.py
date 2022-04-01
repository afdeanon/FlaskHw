from app import myobj
from flask import Flask, flash, render_template
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myobj.route("/")
def home():
	cities = city_names
	return render_template('home.html', name = name, city_names = cities)
	
