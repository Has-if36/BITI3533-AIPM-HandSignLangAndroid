import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras


num_to_alpha = {
    -1: '-',
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
}

label = {
    '-': -1,
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
}


data_train = pd.read_csv(r'.\HandRecBaseV4_output\data\hand_sign_data_hasif.csv')
actual_output = data_train['Actual Output'].to_numpy()
y_train = data_train['Actual Output'].to_numpy()
y_train = np.zeros(shape=[data_train.shape[0], 26])
for i, y_each in enumerate(actual_output):
    index = label[y_each]
    y_train[i][index] = 1
data_train = data_train.drop(['Actual Output'], axis=1)
x_train = data_train.to_numpy()

data_test = pd.read_csv(r'.\HandRecBaseV4_output\data\hand_sign_data_test.csv')
actual_output = data_test['Actual Output'].to_numpy()
y_test = np.zeros(shape=[data_test.shape[0], 26])
for i, y_each in enumerate(actual_output):
    index = label[y_each]
    y_test[i][index] = 1
data_test = data_test.drop(['Actual Output'], axis=1)
x_test = data_test.to_numpy()

# x_train, x_test = 1/x_train, 1/x_test
model = tf.keras.Sequential([
    # tf.keras.layers.Flatten(input_shape=(150, 150)),  # input_shape=(150, 150)
    tf.keras.layers.Dense(130, activation='relu', input_dim=150),
    # tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(26, activation='relu'),
    tf.keras.layers.Dense(26, activation='sigmoid')
])
print(model.output_shape)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)