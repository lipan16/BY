from keras.layers import *
from keras.models import *
from keras.utils.vis_utils import *

WIDTH = 80
HEIGHT = 25
CHANNEL = 1
CLASS_NUM = 10


def get_model(weights_file=None):
    inputs = Input(shape=(HEIGHT, WIDTH, CHANNEL), dtype='float32')
    x = inputs
    x = Conv2D(filters=32, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = Conv2D(filters=32, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2))(x)

    x = Conv2D(filters=64, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = Conv2D(filters=64, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2))(x)

    x = Conv2D(filters=128, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = Conv2D(filters=128, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2))(x)

    x = Conv2D(filters=256, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = Conv2D(filters=256, kernel_size=3, strides=1, activation='relu', padding='same')(x)
    x = MaxPooling2D((2, 2))(x)

    x = Flatten()(x)
    x = Dropout(0.5)(x)
    x1 = Dense(CLASS_NUM, activation='softmax', name="First")(x)
    x2 = Dense(CLASS_NUM, activation='softmax', name="Second")(x)
    x3 = Dense(CLASS_NUM, activation='softmax', name="Third")(x)
    x4 = Dense(CLASS_NUM, activation='softmax', name="Fourth")(x)
    x5 = Dense(CLASS_NUM, activation='softmax', name="Fifth")(x)

    models = Model(inputs=inputs, outputs=[x1, x2, x3, x4, x5])

    models.compile(loss='categorical_crossentropy',
                   optimizer='adam',
                   metrics=['accuracy'])

    if weights_file is not None:
        models.load_weights(weights_file)

    return models


def get_picture(save_path="picture/5_number_network.png"):
    plot_model(get_model(), to_file=save_path, show_shapes=True)
