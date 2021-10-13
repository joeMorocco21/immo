from flask import Flask, render_template, jsonify, Response
import pandas as pd
from flask import request
import os
app = Flask(__name__, template_folder='templates')
    # To get one variable, tape app.config['MY_VARIABLE']
class View():
    @app.route('/')
    def index():
        return render_template('index.html')