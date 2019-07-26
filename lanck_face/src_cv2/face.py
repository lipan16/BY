import face_recognition
import cv2
video_capture = cv2.VideoCapture(0)

i = 0
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (500, 500))
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)#找到了当前帧中所有面部的编码

    for face_location in face_locations:
        i += 1
        top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]
        rgb_frame = face_image[:, :, ::-1]
        # cv2.imshow('no.{}.jpg'.format(i),face_image)
        cv2.imwrite('../data/face/{}.jpg'.format(i), rgb_frame)
        if i == 0:
            cv2.imwrite("../data/face/{}.jpg".format(i), face_image)
            i += 1
        else:
            for face_encoding in face_encodings:
                for m in range(0, i):
                    match = face_recognition.compare_faces("../data/face/{}.jpg".format(m), face_encoding, tolerance=0.49)
                    if not match[0]:
                        cv2.imwrite("../data/face/i.jpg")
                        i += 1

    cv2.imshow('Video', small_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows
