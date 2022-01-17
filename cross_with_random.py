# read data with pandas
import pandas as pd
from sklearn.metrics import accuracy_score

data = pd.read_csv("/home/youssef/Desktop/machine/diabetics.csv")
X = data.drop('outcome', axis=1)
y = data['outcome']

# fit with random forest
from sklearn.ensemble import RandomForestClassifier
rm = RandomForestClassifier(n_estimators=10)

from sklearn.model_selection import KFold
k = 5
kfold = KFold(n_splits=k)
accuracy = []
for train_index, test_index in kfold.split(X):
    X_train, X_test = X.iloc[train_index, :], X.iloc[test_index, :]
    y_train, y_test = y[train_index], y[test_index]
    rm.fit(X_train, y_train)
    prediction = rm.predict(X_test)
    acc = accuracy_score(y_test, prediction)
    accuracy.append(acc)

acc = sum(accuracy) / k
print("The accuracy of  Cross validation is  : ", acc)