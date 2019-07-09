from scipy.io import arff
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

file = open('/home/kejsi/PythonBda/3authors.arff', encoding="utf8")
data = arff.loadarff(file)
df = pd.DataFrame(data[0])

#df = df.drop("instanceID", axis=1)

target = pd.factorize(df['authorName_original'])[0]
#df = df.drop("authorName", axis=1)

# X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.25, random_state=0)
clf = RandomForestClassifier(n_jobs = -1, random_state=5, n_estimators = 100)
# clf.fit(X_train, y_train)
# predict = clf.predict(X_test)
# print(predict)
# cm = confusion_matrix(y_test, predict)
# print(cm)
# ac = accuracy_score(y_test, predict)
# print(ac)
scores = cross_val_score(clf, df, target, cv =5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
y_pred = cross_val_predict(clf, df, target, cv=5)
conf_mat = confusion_matrix(target, y_pred)
print(conf_mat)
