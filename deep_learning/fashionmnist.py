import gzip
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


def open_image(filename):
    with gzip.open(filename, 'rb') as file:
        data = file.read()
        return np.frombuffer(data, dtype=np.uint8, offset=16).reshape(-1, 28, 28).astype(np.float32)


def open_labels(filename):
    with gzip.open(filename, 'rb') as file:
        data = file.read()
        return np.frombuffer(data, dtype=np.uint8, offset=8)


X_train = open_image("../data/train-images-idx3-ubyte.gz")
y_train = to_categorical(open_labels("../data/train-labels-idx1-ubyte.gz"))

X_test = open_image("../data/t10k-images-idx3-ubyte.gz")
y_test = to_categorical(open_labels("../data/t10k-labels-idx1-ubyte.gz"))

model = Sequential()

model.add(Dense(100, activation="sigmoid", input_shape=(784,)))  # The hidden layer
model.add(Dense(10, activation="sigmoid"))  # The output layer

model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(X_train.reshape(60000, 784), y_train, epochs=10, batch_size=1000)

# model.evaluate(X_test.reshape(-1, 784), y_test)
pred = model.predict(X_test.reshape(-1, 784))

ytrue = pd.Series(np.argmax(y_test, axis=1), name='actual')
ypred = pd.Series(np.argmax(pred, axis=1), name='pred')
print(pd.crosstab(ytrue, ypred))

# print(model.predict(X_train[1].reshape(1, 784)))

# y_train_pred = np.round(model.predict(X_train.reshape(60000, 784))).reshape(-1)
# print(np.mean(y_train_pred == y_train))