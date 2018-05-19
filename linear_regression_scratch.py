import numpy as np
data =np.loadtxt('data.csv',delimiter=',')
x= data[:,0]
y=data[:,1]

from sklearn import model_selection
#70:30 splitting
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(x,y,test_size=0.3)


def fit(x_train,y_train):
    num=(x_train*y_train).mean()-x_train.mean()*y_train.mean()#numpy array so no need of for loop for multiplication
    den=(x_train**2).mean()-x_train.mean()**2
    m=num/den
    c=y_train.mean()-m*x_train.mean()
    return m,c

def predict(x,m,c):
    return m*x+c
    

def score(y_test,ypred):
    u=((y_test-y_pred)**2).sum()
    v=((y_test-y_truth.mean())**2).sum()



def cost(x,y,m,c):
    return ((y-m*x-c)**2).sum()
    


m,c=fit(X_train,Y_train)
y_pred=predict(X_test,m,c)
score(Y_test,Y_pred)

