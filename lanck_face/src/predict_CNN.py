import cv2
from src.util import check_weight
from network.cnn import cnn_models, WIDTH, HEIGHT
from src.train_CNN import CNN_WEIGHT_PATH
import numpy as np


def Predict_CNN():
    video_capture = cv2.VideoCapture(0)  # 从摄像头中读取视频流
    check_weight(CNN_WEIGHT_PATH)  #核查是否存在权重
    model = cnn_models()  #模型
    model.load_weights(CNN_WEIGHT_PATH)  # 加载权重
    face_cascade = cv2.CascadeClassifier('D:\Program files\python36\Lib\site-packages\cv2\data'
                                         '/haarcascade_frontalface_default.xml')
    i = 0  # 每20帧输出一次，i作循环变量
    who = {}  # 记录每个人出现的概率
    numbers = {}  # 记录每个人出现的次数
    number = 0  # 总人数

    while True:  # 读取每一帧
        face_locations = []

        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰度化
        face_locations = face_cascade.detectMultiScale(gray, 1.2, 5)  #  第二个参数是每次检测放大的百分比，
        # face_locations = face_recognition.face_locations(gray)  # 0.18s 其余所有时间为0.012s
        if len(face_locations) != 0:  # 检测到视频帧中有人脸
            number += len(face_locations)  # 每帧中人脸的总数
            for face_location in face_locations:
                # top, right, bottom, left = face_location   # face_recognition的边框
                # cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                # face = gray[top:bottom, left:right]
                face_image = []
                x, y, h, w = face_location  # cv2 的边框，矩形的表示方法却不同
                cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 0, 255), 2)
                face = gray[y:y + h, x:x + w]


                try:
                    face_image.append(cv2.resize(face, (WIDTH, HEIGHT)))
                    data = np.array(face_image).astype(np.float32).reshape(-1, WIDTH, HEIGHT, 1) / 255
                    results = model.predict(data)  # 神经网络预测时间：0.001s


                    if who == {}:
                        for m in range(len(face_locations)):
                            temp = results[m].argmax()
                            who[temp] = results[m].take(temp)
                            numbers[temp] = 1

                    else:
                        for m in range(len(face_locations)):
                            temp = results[m].argmax()
                            if temp in who.keys():
                                who[temp] += results[m].take(temp)
                                numbers[temp] += 1
                            else:
                                who[temp] = results[m].take(temp)
                                numbers[temp] = 1

                    i += 1
                    if i % 20 == 0:
                        print(str(who))
                        print(number)
                        for m in range(len(who)):
                            print("Welcome people:{}".format(list(who.keys())[m]),end='\t')
                            print(who[list(who.keys())[m]] / numbers[list(numbers.keys())[m]],end='\t')
                            print(numbers[list(numbers.keys())[m]], '\n')

                        # a = int(numbers[list(numbers.key())[m]])
                        # b = int(number // 3)
                        # c = who[list(who.keys())[m]] / numbers[list(numbers.keys())[m]]
                        # if a >= b:
                        #     if c >= 0.6:
                        #         print("Welcome :{}".format(list(who.keys())[m]))

                        who.clear()
                        numbers.clear()
                        i = 0
                        number = 0

                except:
                    continue  # 这里有一定几率产生一个奇怪的错误。。。暂时只能continue


        cv2.imshow("Video", frame)  # 展示一帧时间：不足0.001s
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 1ms一帧 q：退出
            break

    video_capture.release()  # 释放资源
    cv2.destroyAllWindows

Predict_CNN()

