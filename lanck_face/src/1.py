import cv2

img = cv2.imread("../att_face/s1/1.jpg")
cv2.imshow("src", img)

r = 64.0 / img.shape[1]
dim = (64, int(img.shape[0] * r))

# 执行图片缩放，并显示
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
