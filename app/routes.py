from app import myapp_obj
from flask import Flask, flash, render_template
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myapp_obj.route("/")
def home():
	cities = city_names
	return render_template('home.html', name = "Lisa", city_names = cities)

