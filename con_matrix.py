# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd

data = pd.read_csv('diabetics.csv')

print(data.shape)
print(data.head)

x = data.drop("outcome", axis=1)
y = data['outcome']
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)  # 70% training and 30% test

print(data['outcome'].describe())

print('ggggg', data.ndim)  # WHAT THIS

from sklearn import svm

# Create a svm Classifier
clf = svm.SVC(kernel='linear')  # Linear Kernel

# Train the model using the training sets
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# confusion matrix

from sklearn.metrics import confusion_matrix

conf = confusion_matrix(y_pred, y_test)

print('confusion matrix', conf)

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy: how often is the classifier correct?

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

print("precition:", metrics.precision_score(y_test, y_pred))

print("f1 score:", metrics.f1_score(y_test, y_pred))

print("recall:", metrics.recall_score(y_test, y_pred))
