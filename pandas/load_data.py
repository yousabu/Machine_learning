import pandas as pd

Google_stock = pd.read_csv('/home/youssef/Desktop/sklearn/diabetics.csv')

print(data.describe())

# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('./GOOG.csv')

# We print some information about Google_stock
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)

Google_stock.head()
Google_stock.tail()

Google_stock.isnull().any()

# We get descriptive statistics on our stock data
Google_stock.describe()

# We get descriptive statistics on a single column of our DataFrame
Google_stock['Adj Close'].describe()

# We print information about our DataFrame
print()
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())

# We display the correlation between columns
Google_stock.corr()

# We display the total amount of money spent in salaries each year
data.groupby(['Year'])['Salary'].sum()
# We display the average salary per year
data.groupby(['Year'])['Salary'].mean()

# We display the total salary each employee received in all the years they worked for the company
data.groupby(['Name'])['Salary'].sum()

# We display the salary distribution per department per year.
data.groupby(['Year', 'Department'])['Salary'].sum()
