import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split

def get_scoure(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    print( model.score(X_test, y_test))

data = pd.read_csv('diabetics.csv')
X = data.drop('outcome', axis=1)
y = data['outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# sm = svm.SVC()

rm = RandomForestClassifier(n_estimators=10)
rm.fit(X_train, y_train)

print(rm.score(X_test, y_test))

from sklearn.model_selection import KFold

kf = KFold(n_splits=3)
print(kf)

for train_index, test_index in kf.split([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(train_index, test_index)





print("@#@" * 50)

for train_index, test_index in kf.split(data):
    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    get_scoure(svm.SVC(), X_train, X_test, y_train, y_test)
    get_scoure(RandomForestClassifier(), X_train, X_test, y_train, y_test)
