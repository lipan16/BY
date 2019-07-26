import keras
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten, Activation

FIRST_CONV_INPUT = (64, 64, 1)#输入图片的特征
NUMBER_OUTPUT = 40

def cnn_models():
    cnn_model = keras.models.Sequential()
    cnn_model.add(Conv2D(input_shape=FIRST_CONV_INPUT,
                     filters=32,
                     kernel_size=(5, 5),
                     padding='same',
                     activation='relu'))
    cnn_model.add(MaxPooling2D(strides=2))
    cnn_model.add(Conv2D(filters=64,
                     kernel_size=(5, 5)
                     , padding='same',
                     activation='relu'))
    cnn_model.add(MaxPooling2D(strides=2))
    cnn_model.add(Flatten())
    cnn_model.add(Dense(1024, activation='relu'))
    cnn_model.add(Dropout(0.5))
    cnn_model.add(Dense(NUMBER_OUTPUT))
    cnn_model.add(Activation('softmax'))
    keras.optimizers.Adam(lr=0.01)
    cnn_model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return cnn_model
