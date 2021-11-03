# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
store_items
# We count the number of NaN values in store_items
x =  store_items.isnull().sum().sum()

# We print x
print('Number of NaN values in our DataFrame:', x)


store_items.isnull()

store_items.isnull().sum()


# We print the number of non-NaN values in our DataFrame
print()
print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())

# We drop any rows with NaN values
store_items.dropna(axis = 0)

# We drop any columns with NaN values
store_items.dropna(axis = 1)

# We replace all NaN values with 0
store_items.fillna(0)


# We replace NaN values with the previous value in the column
store_items.fillna(method = 'ffill', axis = 0)

# We replace NaN values with the previous value in the row
store_items.fillna(method = 'ffill', axis = 1)
# We replace NaN values with the next value in the column
store_items.fillna(method = 'backfill', axis = 0)

# We replace NaN values with the next value in the row
store_items.fillna(method = 'backfill', axis = 1)

# We replace NaN values by using linear interpolation using column values
store_items.interpolate(method = 'linear', axis = 0)

# We replace NaN values by using linear interpolation using row values
store_items.interpolate(method = 'linear', axis = 1)


