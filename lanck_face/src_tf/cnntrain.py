import tensorflow as tf
from src_tf.cnnlayer import cnnlayer

def cnntrain():
    logits, test_x, test_y, input_x, output_y, imgs_test, imgs_train, labs_test, labs_train,_ = cnnlayer()
    # logits = next(cnnlayer())

    # 交叉熵损失函数
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=output_y))
    # 将训练优化方法改成GradientDescentOptimizer发现并没有加快收敛所以又改回AdamOptimizer
    # train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    train_op = tf.train.AdamOptimizer(0.01).minimize(loss)
    # 比较标签是否相等，再求的所有数的平均值，tf.cast(强制转换类型)
    accuracy = tf.metrics.accuracy(
        labels=tf.argmax(output_y, axis=1),
        predictions=tf.argmax(logits, axis=1), )[1]
    # 将loss与accuracy保存以供tensorboard使用
    tf.summary.scalar('loss', loss)
    tf.summary.scalar('accuracy', accuracy)
    # 合并所有的Op为一个Op


    # 数据保存器的初始化
    saver = tf.train.Saver()
    return train_op, saver, accuracy, loss
