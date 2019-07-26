import cv2
import csv
import face_recognition
import numpy as np
from src_keras.util import getPaddingSize
from network.cnn import NUMBER_OUTPUT

CSV_TRAIN_PATH = "CSV/training.csv"
CSV_TEST_PATH = "CSV/test.csv"


def get_label(num):  #获取独热码
    label = np.zeros(NUMBER_OUTPUT)
    label[int(num) - 1] = 1   #让编号为num-1的值为1
    return label


def get_encodings(Is_Train = True):
    encodings = []  # 二维
    labels = []
    if Is_Train:
        PATH = CSV_TRAIN_PATH
    else:  # test
        PATH = CSV_TEST_PATH
    with open(PATH, "r") as csvs:
        reader = csv.reader(csvs)
        # for rows in list(reader)[(step - 1) * batch_size:step * batch_size]:  #分批获取的方法，训练时可能出现问题
        for rows in list(reader):
            file_name = rows[0]
            file_label = rows[1]
            try:
                path = file_name
                image_data = cv2.imread(path)
                # rgb_data = image_data[:, :, ::-1]
                face_encoding = face_recognition.face_encodings(image_data)
                try:
                    face_enco = [en+0.5 for en in face_encoding[0]]  # 将数据范围调整到零0到1比较好
                except:  # 可能会有未找到面部返回空数组导致越界的异常，continue就好
                    continue
                encodings.append(face_enco)  # file_label没有0
                labels.append(get_label(file_label))  # 训练时返回独热码
            except FileNotFoundError:
                print("未找到文件，文件名{name}，标签为{labels}".format(name=file_name, labels=file_label))
                continue

    return np.array(encodings), np.array(labels)


def get_pictures(height=64, weight=64, Is_Train=True):
    image_data = []
    labels = []
    if Is_Train:
        PATH = CSV_TRAIN_PATH
    else:  # test
        PATH = CSV_TEST_PATH
    with open(PATH, "r") as csvs:
        reader = csv.reader(csvs)
        for rows in list(reader):
            file_name = rows[0]
            file_label = rows[1]
            try:
                img = cv2.imread(file_name, 0)
                h, w = img.shape[:2]
            except:
                continue
            img = getPaddingSize(img, h, w)
            # 将图片缩小
            img = cv2.resize(img, (weight, height))
            # cv2.imshow("HG", img)
            # cv2.waitKey(0)
            image_data.append(img)
            labels.append(get_label(file_label))  # 将对应的图片和标签存进数组里面
    image_data = np.array(image_data).astype(np.float32).reshape(-1, 64, 64, 1) / 255
    labels = np.array(labels).astype(np.float32).reshape(-1, NUMBER_OUTPUT)
    return image_data, labels
