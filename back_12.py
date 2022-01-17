# read data with pandas
import pandas as pd

data = pd.read_csv("/home/youssef/Desktop/machine/diabetics.csv")
X = data.drop('outcome', axis=1)
y = data['outcome']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# fit with mlp
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(12, 12, 12), activation='logistic', solver='sgd')
mlp.fit(X_train, y_train)
pre_mlp = mlp.predict(X_test)

# calc accuracy
from sklearn.metrics import accuracy_score
print("The accuracy is: ", accuracy_score(y_test, pre_mlp))


h = []

h.append("mk")
print(h)