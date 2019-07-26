# 检测人脸
import face_recognition
import cv2

from PIL import Image

# 读取图片并识别人脸
img = face_recognition.load_image_file("face1.jpg")
face_locations = face_recognition.face_locations(img)
print(face_locations)

# 调用opencv函数显示图片
img = cv2.imread("face1.jpg")
cv2.namedWindow("原图")
cv2.imshow("原图", img)

'''# 遍历每个人脸，并标注
faceNum = len(face_locations)
for i in range(0, faceNum):
    top =  face_locations[i][0]
    right =  face_locations[i][1]
    bottom = face_locations[i][2]
    left = face_locations[i][3]

    start = (left, top)
    end = (right, bottom)

    color = (55,255,155)
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)

# 显示识别结果
cv2.namedWindow("识别")
cv2.imshow("识别", img)'''
i = 1
for face_location in face_locations:

        # 打印每张脸的位置信息
        i = i + 1
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right)) 
# 指定人脸的位置信息，然后显示人脸图片
        face_image = img[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        #pil_image.show() 
        cv2.imwrite('No.{}.jpg'.format(i), pil_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

