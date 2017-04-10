#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 01:42:29 2017

@author: luoma
"""

# -*- coding: utf-8 -*-
import numpy as np
import pickle
import tflearn
from sklearn.model_selection import train_test_split
def one_hot_code(Y):
    result = []
    for y in Y:
        ty = [0,0,0,0]
        ty[y] = 1
        result.append(ty)
    return result

with open('train_data.bat', 'rb') as fp:
    data = pickle.load(fp)
X = data['X']
y = data['Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.23, random_state=592)

y_train = one_hot_code(y_train)
y_test = one_hot_code(y_test)


xl = len(X_train[0])
net = tflearn.input_data([None, xl])
net = tflearn.fully_connected(net, 8000, activation='sigmoid')
net = tflearn.fully_connected(net, 100, activation='relu')
net = tflearn.fully_connected(net, 4, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
                         loss='categorical_crossentropy')
model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(X_train, y_train, validation_set=(X_test, y_test), show_metric=True,
          batch_size=32)
model.save('my_model.tflearn')