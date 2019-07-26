import numpy as np

def get_label(num):
    label = np.zeros(40) #laber = [0,0,0]
    label[int(num) - 1] = 1 #让编号为num-4的值为1
    return label
