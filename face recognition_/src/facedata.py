import cv2
import csv
from src.lab import get_label
import tensorflow as tf

size = 64
imgs = []
labs = []#定义两个数组用来存放图片和标签

def getPaddingSize(img):
    img = cv2.imread(img, 0)
    h, w = img.shape[:2]
    longest = max(h, w)

    if w < longest:
        tmp = longest - w
        a = 0
        b = w
        c = tmp // 2
        d = h - c
        img = img[a:b,c:d]

    elif h < longest:
        tmp = longest - h
        a = tmp // 2
        b = w - a
        c = 0
        d = h
        img = img[a:b,c:d]

    else:
        pass
    return img

def readData(path, h=size, w=size):
    with open(path) as data:
        rows = csv.reader(data)
        for row in rows:
            if row == []:
                continue
            # print(row[0])
            img = getPaddingSize(row[0])

            # 将图片放大，扩充图片边缘部分

            img = cv2.resize(img, (h, w))
            img = tf.reshape(img, [-1, 64, 64, 1])

            imgs.append(img)
            labs.append(get_label(row[1]))  # 将对应的图片和标签存进数组里面

    return imgs, labs

readData('../CSV/iris_test.csv')