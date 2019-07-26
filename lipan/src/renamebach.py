import os

path_name = 'D:\Python\work1\data'  # 表示你需要批量改的文件夹
i = 100
for item in os.listdir(path_name):  # 进入到文件夹内，对每个文件进行循环遍历
    print(os.path.join(path_name, item))  # 源文件名

    print(os.path.join(path_name, 's'+str(i)))  # 目的文件名

    # os.rename(os.path.join(path_name, item), os.path.join(path_name, 's'+str(i)))
    # os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
    i += 1
