import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix

data = pd.read_csv('diabetics.csv')
print(data.shape)
print(data.head)
X = data.drop('outcome', axis=1)
y = data['outcome']


rf = RandomForestClassifier(n_estimators=10)

from sklearn.model_selection import KFold

k = 5
kfold = KFold(n_splits=k, random_state=None, shuffle=False)

acclist = []

for train_index, test_index in kfold.split(X):
    X_train, X_test = X.iloc[train_index, :], X.iloc[test_index, :]
    y_train, y_test = y[train_index], y[test_index]
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)

    from sklearn.metrics import confusion_matrix

    matrix = confusion_matrix(y_test, predictions)
    from sklearn.metrics import accuracy_score

    acc = accuracy_score(y_test, predictions)
    acclist.append(acc)

acc = sum(acclist) / k
print(acc)
