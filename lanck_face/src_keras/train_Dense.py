from network.dense import dense_models
from src_keras.rec import get_encodings
from keras.callbacks import TensorBoard
import os
import numpy as np
from src_keras.util import check_weight

LOG_PATH = "log/"
DENSE_WEIGHT_PATH = "weight/dense.h5"
batch_size = 5
num_steps = 60
epochs = 60


def train():

    batch_x, batch_y = get_encodings()
    model =dense_models()
    if os.path.exists(DENSE_WEIGHT_PATH):
        model.load_weights(DENSE_WEIGHT_PATH)

    tb = TensorBoard(log_dir=LOG_PATH, write_images=1)
    call_list = [tb]
    model.fit(x=batch_x, y=batch_y, batch_size=batch_size, epochs = epochs, verbose=2,callbacks=call_list)  # callback回调函数会在训练适当时机被调用
    model.save_weights(DENSE_WEIGHT_PATH, True)# 保存模型的权重


def test():
    check_weight(DENSE_WEIGHT_PATH)
    model = dense_models()
    model.load_weights(DENSE_WEIGHT_PATH)
    data = []
    test_x, test_y = get_encodings(False)
    data.append(test_x)
    data = np.array(data).astype(np.float32).reshape(-1,128)
    out = model.test_on_batch(data,test_y)
    print("loss = {:.4f}, accuracy = {:.4f}".format(out[0],out[1]))


