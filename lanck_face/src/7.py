import csv
from PIL import Image
import numpy as np

with open("../data/iris_training.csv", 'r') as myFile:
    lines = csv.reader(myFile)
    for line in list(lines)[0:1]:
        im = Image.open(line[0])
        img = np.array(im)  # image类 转 numpy
        print(img)

