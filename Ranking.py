import pandas as pd 
import numpy as np


df = pd.read_csv('Ranking.csv')
df=df.drop(['url','address','name','phone','dish_liked','reviews_list','menu_item'],axis=1)
import cleaning	
df = cleaning.cleanDF(df)	

import visualization as visualize

visualize.Plot(df)


print('Running LabelEncoder...',end='')
import preprocess
df = preprocess.label_encode_input(df)
print('Done')
x=df.drop(['rate'],axis=1)
y=df['rate']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=121)

print('Running LabelEncoder...',end='')
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
print('Done')

#Logistic regression, Decision tree , Random forest, KNN & SVM 
from sklearn.linear_model import LogisticRegression
my_model1=LogisticRegression()
result1=my_model1.fit(x_train,y_train)
pred1=my_model1.predict(x_test)
from sklearn.metrics import accuracy_score,confusion_matrix
print('Logistic: ',accuracy_score(y_test,pred1))

