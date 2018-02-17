import pandas as pd
iris =pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
print(type(iris))
df=iris.copy()
print(df.head())
