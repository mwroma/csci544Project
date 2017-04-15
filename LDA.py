# -*- coding: utf-8 -*-
import numpy as np
import pickle
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.decomposition import LatentDirichletAllocation
with open('train_data.bat', 'rb') as fp:
    data = pickle.load(fp)
X = data['X']
X_train, X_test = train_test_split(X, test_size=0.23, random_state=592)
lda = LatentDirichletAllocation(n_topics = 4, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
XTrain = lda.fit_transform(X_train)
XTest = lda.transform(X_test)
print(XTest[0])
