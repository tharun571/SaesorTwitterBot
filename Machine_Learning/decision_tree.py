import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

def train_model():
    dataset = pd.read_csv('data_main.csv')
    X = dataset.iloc[:, 1:].values
    y = dataset.iloc[:, 0].values

    from sklearn.tree import DecisionTreeRegressor
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X, y)
    pickle.dump(regressor,open("twitter_bot.sav","wb"))

def predict_result(followers):
    regressor = pickle.load(open("twitter_bot.sav", 'rb'))
    print(regressor.predict([[3000,followers]]))

train_model()
predict_result(2868)


'''
y = y.reshape(len(y),1)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

print(sc_y.inverse_transform(regressor.predict(sc_X.transform([[3000,52]]))))
'''
