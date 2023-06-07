import numpy as np # for arrayprocessing
import pandas as pd #for dataframe
import matplotlib as plt #for pictorial representation

import seaborn as sns #for visulisation
#%matplotlib notebook
# from sklearn.ensemble import RandomForestClassifier

#for datarepresentation
import pandas as pd
from classifier import classifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# cursor = connection.cursor()

# query = "SELECT * FROM table_name"
# cursor.execute(query)
# result = cursor.fetchall()
# cursor.close()
# connection.close()
# df = pd.read_sql('SELECT * FROM diabetes.csv', con=connection)


# df = pd.read_csv("diabetes.csv")
# for x in df.columns:
#     if x in ['Pregnancies','Age','Outcome']:
#         continue
#     df[x]=df[x].replace(0,df[x].mean())
# df







df = pd.read_csv("diabetes.csv")
df
df.info()
x = df.drop(['Outcome'], axis=1)
x.head()
y=df['Outcome']
y
	#from sklearn.preprocessing import MinMaxScaler
	#scaler = MinMaxScaler()
	#x = scaler.fit_transform(x)
    #x
y
# from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 0.3, random_state = 1)
from sklearn.neighbors import KNeighborsClassifier as knn, KNeighborsClassifier

# sc = StandardScaler()
# xtrain = sc.fit_transform(xtrain)
# xtest = sc.transform(xtest)


# classifier = RandomForestClassifier()
# classifier.fit(xtrain, ytrain)


knn = KNeighborsClassifier(n_neighbors =5 )
classifier = knn.fit(xtrain, ytrain)
# ypred = knn.predict(xtest)
# ypred
# ytest
# 	#to find accuracy of model we use accuracy_score function
from sklearn.metrics import accuracy_score
ypred = knn.predict(xtest)
score= accuracy_score(ytest,ypred)
print(score)

import pickle
pickle.dump(classifier, open("model.pkl","wb"))
model = pickle.load(open("model.pkl","rb"))


