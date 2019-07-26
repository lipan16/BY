from network.cnn import cnn_models
from src.rec import get_pictures
from src.util import check_weight
import os

LOG_PATH = "log/"
CNN_WEIGHT_PATH = "../weight/cnn.h5"
batch_size = 5
epochs = 7


def train(Is_continue=True):
    batch_x, batch_y = get_pictures()
    model = cnn_models()
    if Is_continue:
        if os.path.exists(CNN_WEIGHT_PATH):
            model.load_weights(CNN_WEIGHT_PATH)
    else:
        print("begin training!")
        # callback回调函数会在训练适当时机被调用  validation_split=0.1在训练集中随机选取10%做验证集（可以理解为测试集）
        model.fit(x=batch_x, y=batch_y, batch_size=batch_size, epochs=epochs, verbose=2, validation_split=0.1)
        model.save_weights(CNN_WEIGHT_PATH, True)  # 保存模型的权重
        print("train finish\n")


def test():
    print("begin testing")
    check_weight(CNN_WEIGHT_PATH)
    model = cnn_models()
    model.load_weights(CNN_WEIGHT_PATH)
    test_x, test_y = get_pictures(Is_Train=False)
    out = model.test_on_batch(test_x, test_y)
    print("loss = {:.4f}, accuracy = {:.4f}".format(out[0], out[1]))
    print("test finish\n")

train()

