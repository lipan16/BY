import face_recognition
import cv2
from src.util import check_weight
from network.dense import dense_models
from network.cnn import cnn_models
from src.train_Dense import DENSE_WEIGHT_PATH
from src.train_CNN import CNN_WEIGHT_PATH
import numpy as np
weight = 64
height = 64
import time

def Predict_Dense():
    # 从摄像头中读取视频流
    video_capture = cv2.VideoCapture(0)
    check_weight(DENSE_WEIGHT_PATH)
    model = dense_models()
    # 加载权重
    model.load_weights(DENSE_WEIGHT_PATH)

    while True:  # 读取每一帧
        ret, frame = video_capture.read()  # 0.01s
        small_frame = cv2.resize(frame, (0, 0), fx=0.75, fy=0.75)
        rgb_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)  # 0.17s
        if face_locations == []:
            continue
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)  # 找到了当前帧中所有面部的编码 #0.51s
        for face_location in face_locations:    # 画矩形时间：不足0.001s
            top, right, bottom, left = face_location
            cv2.rectangle(small_frame, (left, top), (right, bottom), (0, 0, 255), 2)

        out = model.predict(np.array(face_encodings))  # 神经网络预测时间：0.001s
        for o in out:
            print("Welcome people：{}".format(o.argmax()+1))
        cv2.imshow('Video', small_frame)  # 展示一帧时间：不足0.001s
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows


def Predict_CNN():
    # 从摄像头中读取视频流

    video_capture = cv2.VideoCapture(0)
    check_weight(CNN_WEIGHT_PATH)
    model = cnn_models()
    # 加载权重
    model.load_weights(CNN_WEIGHT_PATH)

    while True:  # 读取每一帧
        face_image = []
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_locations = face_recognition.face_locations(gray)  # 0.18s 其余所有时间为0.012s
        if face_locations == []:
            continue
        for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            face = gray[top:bottom, left:right]
            face_image.append(cv2.resize(face,(weight, height)))

        data = np.array(face_image).astype(np.float32).reshape(-1, 64, 64, 1) / 255
        out = model.predict(data)  # 神经网络预测时间：0.001s
        for o in out:
            print("Welcome people：{}".format(o.argmax()+1))
        cv2.imshow('Video', frame)  # 展示一帧时间：不足0.001s
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows