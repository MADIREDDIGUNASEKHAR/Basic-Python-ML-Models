import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



data=pd.read_csv('ex1data1.txt')




X=np.array(data['X'])
X=X.reshape(-1,1)

print(X)
y=data['y']



X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

model=LinearRegression()

N=model.fit(X_train,y_train)

predict=model.predict(X_test)
c=model.intercept_
m1=model.coef_
nav=c+m1*X

print(r2_score(predict,y_test))












