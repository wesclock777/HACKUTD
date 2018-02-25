import csv
import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import glob

allFiles = glob.glob("finaldata/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=0,encoding='latin-1')
    df = df.drop('text', 1)
    df = df.drop('date', 1)
    list_.append(df)
frame = pd.concat(list_)
frame.dropna(axis=1,how='any',inplace=True)
print(frame)

dfinputs = frame.drop('difference',1)

X= np.array(dfinputs)
Y= np.array(frame['difference'].values)

def predict_prices(X, Y, n):
    #dates = np.reshape(dates,(len(dates),1))
    svr_lin = SVR(kernel = 'linear' , C='le3')
    svr_poly = SVR(kernel= 'poly' , C='le3', degree=2)
    svr_rbf = SVR(kernel='rbf' , C='le3', gamma = 0.1)
    svr_lin.fit(X, Y)
    svr_poly.fit(X, Y)
    svr_rbf.fit(X, Y)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(X[0], svr_rbf.predict(X), color='red', label='RBF model')
    plt.plot(X[0], svr_lin.predict(X), color='green', label='Linear model')
    plt.plot(X[0], svr_poly.predict(X), color='blue', label='Polynomial model')
    ply.xlabel('Combined value')
    plt.ylabel('Change in stock value')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

predicted_price = predict_prices(X,Y,29)

print(predicted_price)
