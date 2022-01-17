# read data with pandas
import pandas as pd

data = pd.read_csv("diabetics.csv")
X = data.drop('outcome', axis=1)
y = data['outcome']

###################################
# split with train test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

###################################
# fit with svm
from sklearn import svm
sv = svm.SVC()
sv.fit(X_train, y_train)
pre_sv = sv.predict(X_test)

###################################
# fit with random forest
from sklearn.ensemble import RandomForestClassifier
rm = RandomForestClassifier(n_estimators=10)
rm.fit(X_train, y_train)
pre_rm = rm.predict(X_test)

###################################
# fit with mlp
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(12, 12, 12), activation='logistic', solver='sgd')
mlp.fit(X_train, y_train)
pre_mlp = mlp.predict(X_test)

###################################
# fit with decision tree
from sklearn.tree import DecisionTreeClassifier
des = DecisionTreeClassifier(random_state=0)
des.fit(X_train, y_train)
pre_des = des.predict(X_test)

###################################
# calc confusion matrix
from sklearn.metrics import confusion_matrix
conf = confusion_matrix(y_test, pre_sv)
print("conf_ metrics is : ", conf)

##################################
# calc accuracy
from sklearn.metrics import accuracy_score
print("The accuracy is: ", accuracy_score(y_test, pre_sv))

###################################
# calc score
print("The score is : ", sv.score(X_test, y_test))

###################################
# calc The precision is the ratio tp / (tp + fp)
from sklearn.metrics import precision_score
precision = precision_score(y_test, pre_sv)
print("precision is:", precision)

###################################
# calc The recall is the ratio tp / (tp + fn)
from sklearn.metrics import recall_score
recall = recall_score(y_test, pre_sv)
print("recall  is :", recall)

##################################
# calc f1_score F1 = 2 * (precision * recall) / (precision + recall)
from sklearn.metrics import f1_score
f1 = f1_score(y_test, pre_sv)
print("f1-measure is : ", f1)

##################################
#  back
m = len(mlp.coefs_)
print(m)
lis = [coef.shape for coef in mlp.coefs_]
print(lis)
#print(mlp.coefs_)

####################

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,y_train)
pre_knn= knn.predict(X_test)

###################################
# split with kfold
from sklearn.model_selection import KFold
k = 5
kfold = KFold(n_splits=k)
accuracy = []
for train_index, test_index in kfold.split(X):
    X_train, X_test = X.iloc[train_index, :], X.iloc[test_index, :]
    y_train, y_test = y[train_index], y[test_index]
    sv.fit(X_train, y_train)
    prediction = sv.predict(X_test)
    acc = accuracy_score(y_test, prediction)
    accuracy.append(acc)

acc = sum(accuracy) / k
print("The accuracy of  Cross validation is  : ", acc)
