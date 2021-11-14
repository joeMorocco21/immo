from flask import Flask, render_template, jsonify, Response
import pandas as pd
from flask import request
import os
from .apps import Apps
app = Flask(__name__, template_folder='templates')

class View(Apps):
    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/particulier')
    def particulier():
        return render_template('particular.html')
    @app.route('/professionel')
    def professionel():
        return render_template('professionel.html')
    @app.route('/predict/<tpbs>/<srb>/<np>/<st>/<nd>/<app>/<loc>/<mai>/<ter>')
    def predict(tpbs,srb,np,st,nd,app,loc,mai,ter):
        print(tpbs,srb,nd,st,np,app,loc,mai,ter)
        return Apps.predicted(tpbs,srb,np,st,nd,app,loc,mai,ter)