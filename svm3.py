# -*- coding: utf-8 -*-
import numpy as np
import pickle
from sklearn import metrics
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
with open('train_data.bat', 'rb') as fp:
    data = pickle.load(fp)
X = data['X']
y = data['Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.23, random_state=592)
clf = svm.SVC(C=100, kernel="sigmoid")
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
my_metrics = metrics.classification_report( y_test, predictions)
print(my_metrics)
