from sklearn import datasets,model_selection
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
algl=LinearRegression()
import pandas as pd
import matplotlib.pyplot as plt
boston=datasets.load_boston()
x=boston.data
y=boston.target
df=(pd.DataFrame(x))
df.columns=boston.feature_names
#print(df.describe())
#print(boston.feature_names)
#type(data)
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y)
print(np.shape(x_train))
algl.fit(x_train,y_train)
y_pred=algl.predict(x_test)
plt.scatter(y_test,y_pred)
#plt.axis([0,40,0,40])
plt.show()
