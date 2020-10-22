import numpy as np
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense

#importing the dataset
dataset = pd.read_csv('data_main.csv')
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values 

#Splitting the data into train and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)


#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_train)



#Building the ANN
ann = Sequential()
ann.add(Dense(units=8,activation='relu',input_shape=(2,)))
ann.add(Dense(units=6,activation='relu'))
ann.add(Dense(units=1,activation='sigmoid'))

ann.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Training the ANN on X_train data
ann.fit(X_train,y_train,epochs=100)
ann.save('ann.h5')

#predicting on the model
model = load_model('ann.h5')
print(model.predict(sc.transform([[seconds,followers]])))