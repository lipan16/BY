from network.cnn import cnn_models
from src.rec import get_pictures
from keras.callbacks import TensorBoard
import os


LOG_PATH = "log/"
WEIGHT_PATH = "../weight/cnn.h5"
batch_size = 10

epochs = 16

def train():
    batch_x, batch_y = get_pictures()
    model =cnn_models()
    if os.path.exists(WEIGHT_PATH):
        model.load_weights(WEIGHT_PATH)
    #tb = TensorBoard(log_dir=LOG_PATH, write_images=1)
    #call_list = [tb]
    print("begin training!")
    model.fit(x=batch_x, y=batch_y, batch_size=batch_size, epochs = epochs, verbose=2)  # callback回调函数会在训练适当时机被调用
    model.save_weights(WEIGHT_PATH, True)


def test():
    check_weight()
    model = cnn_models()
    model.load_weights(WEIGHT_PATH)
    test_x, test_y = get_pictures(False)
    out = model.predict_on_batch(test_x)
    print("loss = {}, accuracy = {}".format(out[0], out[1]))



def check_weight():
    if not os.path.exists(WEIGHT_PATH):
        print("不存在权重！")
        return
