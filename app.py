from flask import Flask, render_template, url_for
from markupsafe import escape
import requests, json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", demo = requests.get("https://api.nasa.gov/insight_weather/?api_key=000rQfOy4HYGv3gw6eHvqop1awibodWWHrizpAaw&feedtype=json&ver=1.0").json())