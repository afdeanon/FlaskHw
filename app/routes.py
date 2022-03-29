from app import myapp_obj
from flask import Flask, render_template, flash, render_template_string
@myapp_obj.route("/")

def home():
        city_names = ["Paris", "London", "Rome", "Tahiti"]
        return render_template('home.html', name = "Lisa", city_names = city_names)
