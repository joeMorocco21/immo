import pytest
import pandas as pd
import numpy as np
import pickle
import os
from model.model import X 
def test_check():
    entree = X[102:105,:]
    rfc = pickle.load(open(os.path.join(os.path.dirname(__file__),'../app/Pricing_prediction.pkl'), 'rb'))
    sortie = rfc.predict(entree)
    assert sortie.shape[0] == entree.shape[0]