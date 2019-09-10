import csv
import keras

from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten, Activation
from keras.utils import plot_model

CAPTCHA_WIDTH = 80
CAPTCHA_HEIGHT = 25
LEARNING_RATE = 0.01
INPUT_CHANNAL = 1
FIRST_CONV_INPUT = (CAPTCHA_HEIGHT, CAPTCHA_WIDTH, INPUT_CHANNAL)
NUMBER_OUTPUT = 3


def train_models():`
    model = keras.models.Sequential()
    model.add(Conv2D(input_shape=FIRST_CONV_INPUT,
                     filters=32,
                     kernel_size=(5, 5),
                     padding='same',
                     activation='relu'))
    model.add(MaxPooling2D(strides=2))
    model.add(Conv2D(filters=64,
                     kernel_size=(5, 5)
                     , padding='same',
                     activation='relu'))
    model.add(MaxPooling2D(strides=2))
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUMBER_OUTPUT))
    model.add(Activation('softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model


def get_picture(save_path="picture/bits_network.png"):
    plot_model(train_models(), to_file=save_path, show_shapes=True)
