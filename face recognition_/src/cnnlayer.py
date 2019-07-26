# -*- coding: UTF-8 -*-

import numpy as np
import tensorflow as tf
from src.facedata import readData

def cnnlayer():
    # 下载并载入 MNIST 手写数字库（55000 * 28 * 28）55000 张训练图像
    imgs_test = []
    labs_test = []

    imgs_test, labs_test=readData('../CSV/iris_test.csv')

    imgs_train = []
    labs_train = []
    imgs_train, labs_train = readData('../CSV/iris_training.csv')

    #将图片数组与标签转换成数组，并给图片做上标签
    imgs_train= np.array(imgs_train)
    labs_train = np.array(labs_train)

    imgs_test = np.array(imgs_test)
    labs_test = np.array(labs_test)

    # one_hot 独热码的编码（encoding）形式
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 的十位数字
    # 0 : 1000000000
    # 1 : 0100000000
    # 2 : 0010000000
    # 3 : 0001000000
    # 4 : 0000100000
    # 5 : 0000010000
    # 6 : 0000001000
    # 7 : 0000000100
    # 8 : 0000000010
    # 9 : 0000000001

    # None 表示张量（Tensor）的第一个维度可以是任何长度
    # 除以 255 是为了做 归一化（Normalization），把灰度值从 [0, 255] 变成 [0, 1] 区间
    # 归一话可以让之后的优化器（optimizer）更快更好地找到误差最小值

    input_x = tf.placeholder(tf.float32, [None, 64 * 64]) / 255.  # 输入

    output_y = tf.placeholder(tf.int32, [None, 40])  # 输出：40个数字的标签

    # -1 表示自动推导维度大小。让计算机根据其他维度的值
    # 和总的元素大小来推导出 -1 的地方的维度应该是多少
    input_x_images = tf.reshape(input_x, [-1, 64, 64, 1])  # 改变形状之后的输入

    # 从 Test（测试）数据集里选取 200 个手写数字的图片和对应标签
    test_x = imgs_test[:200]  # 图片
    test_y = labs_test[:200]  # 标签


    # 构建我们的卷积神经网络：
    # 第 1 层卷积
    conv1 = tf.layers.conv2d(
        inputs=input_x_images,  # 形状 [64, 64, 1]
        filters=32,             # 32 个过滤器，输出的深度（depth）是32
        kernel_size=[10, 10],     # 过滤器在二维的大小是 (10 * 10)
        strides=1,              # 步长是 1
        padding='same',         # same 表示输出的大小不变，因此需要在外围补零 2 圈
        activation=tf.nn.relu   # 激活函数是 Relu
    )  # 形状 [64, 64, 32]


    # 第 1 层池化（亚采样）
    pool1 = tf.layers.max_pooling2d(
        inputs=conv1,      # 形状 [64, 64, 32]
        pool_size=[4, 4],  # 过滤器在二维的大小是（4 * 4）
        strides=4          # 步长是 4
    )  # 形状 [16, 16, 32]


    # 第 2 层卷积
    conv2 = tf.layers.conv2d(
        inputs=pool1,          # 形状 [16, 16, 32]
        filters=64,            # 64 个过滤器，输出的深度（depth）是64
        kernel_size=[5, 5],    # 过滤器在二维的大小是 (5 * 5)
        strides=1,             # 步长是 1
        padding='same',        # same 表示输出的大小不变，因此需要在外围补零 2 圈
        activation=tf.nn.relu  # 激活函数是 Relu
    )  # 形状 [16, 16, 64]


    # 第 2 层池化（亚采样）
    pool2 = tf.layers.max_pooling2d(
        inputs=conv2,      # 形状 [16, 16, 64]
        pool_size=[2, 2],  # 过滤器在二维的大小是（2 * 2）
        strides=2          # 步长是 2
    )  # 形状 [8, 8, 64]

    # 平坦化（flat）。降维
    flat = tf.reshape(pool2, [-1, 8 * 8 * 64])  # 形状 [7 * 7 * 64, ]

    # 1024 个神经元的全连接层
    dense = tf.layers.dense(inputs=flat, units=1024, activation=tf.nn.relu)

    # Dropout : 丢弃 50%（rate=0.5）
    dropout = tf.layers.dropout(inputs=dense, rate=0.5)


    # 10 个神经元的全连接层，这里不用激活函数来做非线性化了
    logits = tf.layers.dense(inputs=dropout, units=40)  # 输出。形状 [1, 1, 10]

    return logits, test_x, test_y, input_x, output_y, imgs_test, imgs_train, labs_test, labs_train, input_x_images
