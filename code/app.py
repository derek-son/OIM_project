# Defines basic structure of Flask app and calls the main routes

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home()
def index():
    return render_template('index.html')

