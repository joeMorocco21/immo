import pandas as pd
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os
from sklearn.preprocessing import StandardScaler
df = pd.read_csv(os.path.join(os.path.dirname(__file__),"../app/data/df_final.csv"))
df.drop(['id', 'tot_lot', 'typ_lot', 'prix_m2'], axis=1, inplace=True)
df.drop(df[df.local == 'mix'].index, inplace=True)
df.reset_index(drop=True)

for c in df.columns:
    if df[c].dtype == 'object': 
        df[c] = df[c].astype('category')
clean=df.copy()
clean_cat = clean.select_dtypes(include=['category'])
clean_num = clean.select_dtypes(exclude=['category'])
dummied_cat = pd.get_dummies(data=clean_cat, prefix=["local"])
dc = dummied_cat.reset_index(drop=True)
price=clean_num.iloc[:,-4]
num_feat=clean_num.loc[:,['Appartement', 'Dépendance', 'Local industriel. commercial ou assimilé', 'Maison', 'Terrain','nbr_piece', 'surf_bati', 'surf terr']]
nf = num_feat.reset_index(drop=True)
scalX = StandardScaler()
scaly = StandardScaler()
scalX.fit(num_feat.values)
scaly.fit(price.values.reshape(-1, 1))
df_features=pd.DataFrame(scalX.transform(num_feat.values))
target=pd.DataFrame(scaly.transform(price.values.reshape(-1, 1)))
data_input = pd.concat([dc, df_features], axis=1)

X = data_input.values
y = target.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
Price_prediction_model = LinearRegression(fit_intercept=True)
Price_prediction_model.fit(X_train, y_train)

with open('Pricing_prediction.pkl', 'wb') as file:
    pickle.dump(Price_prediction_model, file)
    
with open('ScalX.pkl', 'wb') as file:
    pickle.dump(scalX, file)

with open('Scaly.pkl', 'wb') as file:
    pickle.dump(scaly, file)