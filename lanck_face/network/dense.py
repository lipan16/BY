import keras
from keras.layers import Dense, Activation,Dropout
from keras.utils import plot_model

def dense_models():
    dense_model = keras.models.Sequential()
    dense_model.add(Dense(500, kernel_initializer='glorot_uniform', input_shape=(128,)))#均匀分布初始化
    dense_model.add(Activation('tanh'))
    dense_model.add(Dropout(0.5))

    dense_model.add(Dense(500, kernel_initializer='glorot_uniform', ))
    dense_model.add(Activation('tanh'))
    dense_model.add(Dropout(0.5))

    # 输出结果是40个类别，所以维度是40
    dense_model.add(Dense(40, kernel_initializer='glorot_uniform', ))
    # 最后一层用softmax
    dense_model.add(Activation('softmax'))

    keras.optimizers.Adam(lr=0.01)
    dense_model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return  dense_model

def get_picture(save_path="picture/dense_network.png"):
    plot_model(dense_models(), to_file=save_path, show_shapes=True)
