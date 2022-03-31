from app import myonj
from flask import Flask, flash, render_template
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myobj.route("/")
def home():
	cities = city_names
	return render_template('home.html', name = "Lisa", city_names = cities)

