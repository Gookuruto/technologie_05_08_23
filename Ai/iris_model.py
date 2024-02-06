from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

iris = pd.read_csv(r'IRIS.csv')

print(iris)

X = iris.iloc[:, :-1]
y = iris.iloc[:, -1]

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=6)

knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
dt = DecisionTreeClassifier()
lr = LogisticRegression(solver='liblinear')
acc = {}

knn.fit(X_train, y_train)
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

a, b, c = dt.score(X_test, y_test), lr.score(X_test, y_test), knn.score(X_test, y_test)
acc = pd.DataFrame({'models': ['DecisionTree', 'LogisticRegression', 'KNN'], 'accuracy': [a, b, c]})
print(acc)
