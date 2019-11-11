import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.multiclass import unique_labels
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', type=str, default="", help='File to be Processed')
parser.add_argument('--cross', '-c', type=int, default=10, help='Number of cross validation folds')
args = parser.parse_args()

ast = 0
cpp = 0
api = 0
word = 0
unacounted = 0
cross = args.cross
label_list = []
drop_list = []

#print("Loading File...")
df_data = pd.read_csv("CSV/" + args.file, encoding="'latin-1'")
#target = pd.factorize(df_data['AuthorName'])[0]
#print (list(df_data.columns.values))
#df_data['instanceID_original'] = df_data['instanceID_original'].astype(str)
#df_data['instanceID_original'] = pd.factorize(df_data['instanceID_original'])[0]
target = pd.factorize(df_data["'authorName_original'"])[0]
df_data = df_data.drop("'authorName_original'", axis=1)

#To remove features add lines here
#df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='Bjoern')))]

#df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='AST', axis=1)))]
#df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='cpp', axis=1)))]
df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='Bigrams', axis=1)))]
df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='Trigrams', axis=1)))]


df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='TF', axis=1)))]

#df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='Instruction', axis=1)))]

#df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='AST', axis=1)))]
df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='CFG', axis=1)))]

df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='Bjoern', axis=1)))]
df_data = df_data[df_data.columns.drop(list(df_data.filter(regex='cpp', axis=1)))]
print (list(df_data.columns.values))
clf = RandomForestClassifier(n_estimators=600, random_state=0, n_jobs=-1)
#print("Performing Cross Validation...")
#predict = cross_val_predict(clf, df_data, target, cv = cross)
scores = cross_val_score(clf, df_data, target, cv = cross)
print (df_data.shape)
#print("Accuracy via cross validation:" + str(scores.mean()))
print(str(scores.mean()*100) + ", ")
#print(ast + cpp + api + word + unacounted)
#conf_mat = confusion_matrix(target, predict)
#print(conf_mat)
