import keras
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten, Activation

WIDTH = 64
HEIGHT = 64
FIRST_CONV_INPUT = (HEIGHT, WIDTH, 1)  # 输入图片的特征
NUMBER_OUTPUT = 41


def cnn_models():
	cnn_model = keras.models.Sequential()		#Kerase序贯模型
	cnn_model.add(Conv2D(input_shape=FIRST_CONV_INPUT,
						 filters=32,  			# 卷积核个数
						 kernel_size=(5, 5),	#卷积核大小
						 padding='same',  		# same 表示输出的大小不变，使得输入和输出的形状一致
						 activation='relu'))  	#激活函数 # 卷积层
	cnn_model.add(MaxPooling2D(strides=2))  	# 池化层 最大值池化 步长2

	cnn_model.add(Conv2D(filters=32,
						 kernel_size=(5, 5),
						 padding='same',
						 activation='relu'))  	# 卷积层

	cnn_model.add(Conv2D(filters=64,
						 kernel_size=(5, 5),
						 padding='same',
						 activation='relu'))  	# 卷积层

	cnn_model.add(MaxPooling2D(strides=2))  	# 池化层

	cnn_model.add(Flatten())  # 展平层，多维输入，一维输出
	cnn_model.add(Dense(1024, activation='relu'))  # 全连接，激励函数relu
	cnn_model.add(Dropout(0.5))  # 防止过拟合
	cnn_model.add(Dense(NUMBER_OUTPUT))
	cnn_model.add(Activation('softmax'))  # 损失函数
	keras.optimizers.Adam(lr=0.01)  # 学习率，相当于回传参数的权重
	cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	return cnn_model
