import tensorflow as tf
from src.cnntrain import cnntrain
from src.cnnlayer import cnnlayer
import sys
import numpy as np

train_op, saver, accuracy, loss = cnntrain()
logits, test_x, test_y, input_x, output_y, imgs_test, imgs_train, labs_test, labs_train, input_x_images = cnnlayer()

with tf.Session() as sess:
    sess = tf.Session()
    # 初始化变量：全局和局部
    init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    sess.run(init)

    # 训练 5000 步。这个步数可以调节
    for i in range(5000):
        for n in range(20):
            batch_x = imgs_train[(n) * 10: (n + 1) * 10]
            batch_y = labs_train[(n) * 10: (n + 1) * 10]
            train_loss, train_op_ = sess.run([loss, train_op], {input_x_images: batch_x, output_y: batch_y})
            if i % 100 == 0:
                test_accuracy = sess.run(accuracy, {input_x: test_x, output_y: test_y})
                print("第 {} 步的 训练损失={:.4f}, 测试精度={:.2f}.......".format(i, train_loss, test_accuracy))
                # if test_accuracy > 0.98 and n > 2:
                #     saver.save(sess, './train_faces.model', global_step=n * 20 + i)
                #     sys.exit(0)
                # print('accuracy less 0.98, exited!')

# 测试：打印 20 个预测值 和 真实值
# test_output = sess.run(logits, {input_x: test_x[:20]})
# inferred_y = np.argmax(test_output, 1)
# print(inferred_y, '推测的数字')  # 推测的数字
# print(np.argmax(test_y[:20], 1), '真实的数字')  # 真实的数字
