import os
import numpy as np


def getPaddingSize(img, h, w):
    longest = max(h, w)
    if w < longest:  # h>w
        tmp = longest - w
        top = tmp
        bottom = h
        left = 0
        right = w
        img = img[top:bottom, left:right]

    elif h < longest:
        tmp = longest - h
        top = 0
        bottom = h
        left = tmp // 2
        right = w - left
        img = img[top:bottom, left:right]

    else:
        pass

    return img


def check_weight(WEIGHT_PATH):
    if not os.path.exists(WEIGHT_PATH):
        print("不存在权重！")
        return


def write(f, dir_path, csv_file_path, i=1):  # i是起始编号
    for name in os.listdir(dir_path):  # 列出path目录下包含的所有文件夹和文件，返回列表
        temp_dir = os.path.join(dir_path, name)  # 将path和name组合成一个新目录

        if os.path.isdir(temp_dir):  # 这是个文件夹
            i = write(f, temp_dir, csv_file_path, i)
        else:  # 这是个文件
            f.write(str(temp_dir))  # 将文件名写入csv
            f.write(','+str(i))  # 将编号i转化为字符形式写入csv
            # f.write(",{}".format(str(get_label())))  # 将标签写入csv
            f.write("\n")
            i += 1
    return i


def list_dir_and_write_csv(dir_path, csv_file_path):
    with open(csv_file_path, "w") as f:  # 以写的形式打开文件
        write(f, dir_path, csv_file_path)


# list_dir_and_write_csv("data","csv/text.csv")