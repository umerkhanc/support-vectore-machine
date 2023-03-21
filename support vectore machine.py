import numpy as np
from sklearn import svm

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = [0, 0, 1, 1]

clf = svm.SVC(kernel='linear', C=1, random_state=0)
clf.fit(X, y)
print(clf.score(X, y
