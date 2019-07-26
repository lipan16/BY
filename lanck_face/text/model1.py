import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)
i = 0
encodings = []

while True:  # 读取每一帧
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.75, fy=0.75)
    rgb_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)  # 找到了当前帧中所有面部的编码

    j = 0
    for face_encoding in face_encodings:  # 遍历当前帧中的每一个面部编码
        j += 1  # 代表当前帧中的第几个面部
        top, right, bottom, left = face_locations[j - 1]
        face_image = rgb_frame[top:bottom, left:right]

        if i == 0:
            # cv2.imwrite("./face/0.jpg", face_image)
            encodings.append(face_encoding)  # 必须是二维数组
            i += 1
        else:
            match = face_recognition.compare_faces(encodings, face_encoding, tolerance=0.35)
            o = False
            for a in match:
                o = o or a
            if o:
                pass
                # print("We have this people already")
            else:
                # cv2.imwrite("./face/{}.jpg".format(i), face_image)
                encodings.append(face_encoding)
                # print("We have add a people")
                i += 1
                continue

    cv2.imshow('Video', small_frame)

    print("We have {} faces!".format(i))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows
