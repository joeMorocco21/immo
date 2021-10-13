from flask import Flask, render_template, request, Response
from flask import jsonify
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os