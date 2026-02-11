import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

dataset = pd.read_csv('Churn_Modelling.csv')

x=dataset.iloc[:,3:-1].values
y=dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
encoder= LabelEncoder()
x[:,2]=encoder.fit_transform(x[:,2])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct =ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[1])], remainder='passthrough')
x= np.array(ct.fit_transform(x))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=42)

#feature scaling

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

#cff
import tensorflow as tf
train_data = tf.keras.utils.image_dataset_from_directory(
    'dataset/training_set',
    image_size=(64, 64),
    batch_size=32
)

test_data = tf.keras.utils.image_dataset_from_directory(
    'dataset/test_set',
    image_size=(64, 64),
    batch_size=32
)


cnn = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

cnn.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
cnn.fit(x=train_data,validation_data=test_data,epochs=10)


import numpy as np
from keras.utils import load_img
from keras.utils import img_to_array
test_image = load_img('dataset/dog.4027.jpg', target_size = (64, 64))
test_image = img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)

print(result)


print(train_data.class_names)