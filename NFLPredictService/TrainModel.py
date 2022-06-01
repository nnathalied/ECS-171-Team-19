#import sys
#!{sys.executable} -m pip install cvxpy
import cvxpy as cp
import pandas as pd
import numpy as np
from numpy import array
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def predict(team, quarter, yardline, qtrseconds, down, goalsel, yardtogo, margin):

#import data set
 nfl1 = pd.read_csv("NFL_data_super_cleaned.csv")

 nfl1.dropna(inplace=True)
 print(nfl1.isnull().values.any(), nfl1.isnull().sum().sum())

 #Our 350,000 samples seem like a little too much, so sample about 10,000 rows
 sample = nfl1.sample(n=150000, random_state=21, axis=0)
 print(sample.isnull().values.any(), sample.isnull().sum().sum())
 #one-hot encode the categorical variables
 #posteam_type, defteam, side_of_field, game_date (drop), time (convert?), yrdline (convert?)

 cat_columns = ["posteam" , "qtr"]
 #one-hot encode categorical variables
 encoder = preprocessing.OneHotEncoder()
 cat_array = encoder.fit_transform(sample[cat_columns]).toarray()
 cat_labels = encoder.get_feature_names_out(cat_columns)
 cat_onehot_encoded = pd.DataFrame(cat_array, columns=cat_labels)

 #Add back the continuous variables
 cat_onehot_encoded["yardline_100"] = sample["yardline_100"]
 cat_onehot_encoded["quarter_seconds_remaining"] = sample["quarter_seconds_remaining"]
 cat_onehot_encoded["down"] = sample["down"]
 cat_onehot_encoded["goal_to_go"] = sample["goal_to_go"]
 cat_onehot_encoded["ydstogo"] = sample["ydstogo"]
 cat_onehot_encoded["score_margin"] = sample["score_margin"]


 cat_onehot_encoded["play_type"] = sample["play_type"]
 cat_onehot_encoded.dropna(inplace=True)


 print(cat_onehot_encoded.isnull().values.any(), cat_onehot_encoded.isnull().sum().sum())
 #print(onehot_encoded.isnull().values.any())
 #split data into training and testing sets
 #seed: 21, train/test ratio: 0.2 test, 0.8 train



 x, y = cat_onehot_encoded.drop(["play_type"], axis=1).to_numpy(), cat_onehot_encoded["play_type"].to_numpy()
 #Split data into training and testing sets
 X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 21)

 #compares each play_type to the other possible play_type

 scaler = preprocessing.StandardScaler()
 scaler.fit(X_train)


 find = np.where(cat_labels == team)
 clf_ovo = SVC(kernel='linear', decision_function_shape='ovo') # The other is ovr

 clf_ovo.fit(scaler.transform(X_train), np.asarray(y_train))

 insideX = np.array([0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, yardline+0.00, qtrseconds+0.00, down+0.00, goalsel+0.00, yardtogo+0.00, margin+0.00])
 if quarter == 1:
  insideX[32] = 1.00
 elif quarter == 2:
  insideX[33] = 1.00
 elif quarter == 3:
  insideX[34] = 1.00
 elif quarter == 4:
  insideX[35] = 1.00
 else:
  insideX[36] = 1.00

 insideX[find[0]] = 1.00
 inputX = np.array([insideX])

 result = clf_ovo.predict(scaler.transform(inputX))
 print(result)
 print(classification_report(y_test, clf_ovo.predict(scaler.transform(X_test))))

 np.set_printoptions(precision=2)

 return result[0]

