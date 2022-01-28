import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler




data=pd.read_csv('ex1data2.txt')
st=StandardScaler()

X=data.iloc[:,0:2].values
y=data.iloc[:,2].values

X_scale=st.fit_transform(X)



X_train,X_test,y_train,y_test=train_test_split(X_scale,y,test_size=0.08,random_state=0)

model=LinearRegression()

N=model.fit(X_train,y_train)

predict=model.predict(X_test)
c=model.intercept_
m1=model.coef_
