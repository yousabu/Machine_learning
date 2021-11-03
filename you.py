import pandas as pd
data = pd.read_csv('diabetics.csv')
print(data.shape)
print(data.head)
x=data.drop("outcome",axis=1)
y=data['outcome']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
print(data['outcome'].describe())
print("#" * 50)

print(x_train)
print("#" * 50)
print(y_train)

print("#" * 50)
print("#" * 50)

print(x_test)
print("#" * 50)
print(y_test)