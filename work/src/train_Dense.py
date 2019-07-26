from network.dense import dense_models
from src.rec import get_encodings
from keras.callbacks import TensorBoard
import os
import numpy as np

LOG_PATH = "../log"
WEIGHT_PATH = "../weight/dense.h5"
batch_size = 5
num_steps = 60
epochs = 60

def train():

    batch_x, batch_y = get_encodings()
    model =dense_models()
    if os.path.exists(WEIGHT_PATH):
        model.load_weights(WEIGHT_PATH)

    tb = TensorBoard(log_dir=LOG_PATH, write_images=1)
    call_list = [tb]
    model.fit(x=batch_x, y=batch_y, batch_size=batch_size, epochs = epochs, verbose=2,callbacks=call_list)  # callback回调函数会在训练适当时机被调用
    model.save_weights(WEIGHT_PATH, True)


def test():
    check_weight()
    model = dense_models()
    model.load_weights(WEIGHT_PATH)
    data = []
    test_x, test_y = get_encodings(False)
    data.append(test_x)
    data = np.array(data).astype(np.float32).reshape(-1,128)
    out = model.test_on_batch(data,test_y)
    print("loss = {}, accuracy = {}".format(out[0],out[1]))

def check_weight():
    if not os.path.exists(WEIGHT_PATH):
        print("不存在权重！")
        return


