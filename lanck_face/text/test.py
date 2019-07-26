import face_recognition
import cv2
#video_capture = cv2.VideoCapture(0)
i = 0
encodings = []
while True:#读取每一帧
    #ret, frame = video_capture.read()
    frame = cv2.imread('1.jpg')
    small_frame = cv2.resize(frame, (0, 0),fx = 0.65 ,fy = 0.65)
    rgb_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)#找到了当前帧中所有面部的编码

    for face_location in face_locations:#遍历当前帧中的每一个面部
        top, right, bottom, left = face_location
        face_image = rgb_frame[top:bottom, left:right]

        if i == 0:
            cv2.imwrite("./face/0.jpg", face_image)
            encodings.append(face_encodings[0])#必须是二维数组
            i += 1
        else:
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces(encodings, face_encoding)
                o = False
                for a in match:
                    o = o or a
                if o:
                    print("We have this people already")
                else:
                    cv2.imwrite("./face/{}.jpg".format(i), face_image)
                    i += 1
                    encodings.append(face_recognition.face_encodings(small_frame, [face_location])[0])
                    print("We have add a people")
                    break

    cv2.imshow('Video', small_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows
