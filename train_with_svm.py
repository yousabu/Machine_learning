# read data with pandas
import pandas as pd

data = pd.read_csv("/home/youssef/Desktop/machine/diabetics.csv")
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

from sklearn.metrics import accuracy_score
print("The accuracy is: ", accuracy_score(y_test, pre_sv))