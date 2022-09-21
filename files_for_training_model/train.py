"""
Multiple Linear Regression uses several explanatory variables to predict the outcome of a response variable.
There are a lot of variables and multiple linear regression is designed to create a model 
based on all these variables. 

#Dataset link:
https://cdn.scribbr.com/wp-content/uploads//2020/02/heart.data_.zip?_ga=2.217642335.893016210.1598387608-409916526.1598387608

#Heart disease
The effect that the independent variables biking and smoking 
have on the dependent variable heart disease 

the percentage of people biking to work each day, the percentage of people smoking, 
and the percentage of people with heart disease in an imaginary sample of 500 towns.
"""
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# data preprocessing
df = pd.read_csv('heart_data.csv')
df = df.drop("Unnamed: 0", axis=1)
x_df = df.drop('heart.disease', axis=1)
y_df = df['heart.disease']
X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=42)

#build, train and validate performance of model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_train, y_train))  #Prints the R^2 value, a measure of how well
prediction_test = model.predict(X_test)    
print(y_test, prediction_test)
print("Mean sq. errror between y_test and predicted =", np.mean(prediction_test-y_test)**2)

# save model, and validate model weights
pickle.dump(model, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[20.1, 56.3]]))


#Model is ready. Let us check the coefficients, stored as reg.coef_.
#These are a, b, and c from our equation. 
#Intercept is stored as reg.intercept_
#print(model.coef_, model.intercept_)

#All set to predict the number of images someone would analyze at a given time
#print(model.predict([[13, 2, 23]]))
