import csv
import numpy as np
import cv2
from PIL import Image

# with open('t.csv', 'w', newline='') as myFile:
#     myWriter = csv.writer(myFile)
#
#     myWriter.writerow([7, 'g'])
#     myWriter.writerow([8, 'h'])
#
#     myList = [[1, 2], [4, 6]]
#     myWriter.writerows(myList)
#
#     datas = [{'name': "lp", 'age': 23},
#              {'Bob': "lm", "age": 14},
#              {'Tom': "ds", "ahe": 23},
#              {'Jerry': "sd", "skd": '18'}]
#     myWriter.writerows(datas)



with open("../data/iris_training.csv", 'r') as myFile:
    lines = csv.reader(myFile)
    for line in list(lines)[0:1]:
        im = Image.open(line[0])
        img = np.array(im)  # image类 转 numpy

        print(img.shape)
        #img=cv2.imread(line[0],1)
        #print(img)
        #im.show()
        #break;

# im = Image.open("../att_faces/s1/1.pgm")
# im.show()
# img = np.array(im)  # image类 转 numpy
# #img = img[:, :, 0]  # 第1通道
# im = Image.fromarray(img)  # numpy 转 image类
# print(img.shape)
# im.show()
