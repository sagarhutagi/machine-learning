import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np


print("Hello, World!")

x = np.array([200, 17])

layer_1 = Dense(units=3, activation="sigmoid")
a1 = layer_1(x)

layer_2 = Dense(units=1, activation="sigmoid")
a2 = layer_2(a1)

if a2 >= 0.5:
    yhat = 1
else:
    yhat = 0
print(yhat)
