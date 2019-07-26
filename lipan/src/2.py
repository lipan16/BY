# 正方形
# n = int(input("please input a number:"))
# n = 3
# print('*' * n)
# for i in range(n - 2):
#     print('*', ' ' * (n - 2), '*')
# print('*' * n)

# 乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(i, j, i * j), end='')
    print()

# 打印菱形
# n=int(input())
# if not n%2:
#     n+=1;
# e=-(n//2)
# for i in range(e,e+n):
#     print(' '*abs(i)+'*'*(n-2*abs(i)))

# count =0
# for i in range(2, 100000):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#         else:
#             count+=1
# print(count)

# sum=0
# for i in range(1,100,2):
#     sum+=i
# print(sum)

# n=int(input())
# if (n%4==0 and n%100!=0)or n%400==0:
#     print(n)

# str = 'Runoob'
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + '你好')  # 连接字符串

# tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# tinytuple = (123, 'runoob')
#
# print(type(tuple))
# print(tuple)  # 输出完整元组
# print(tuple[0])  # 输出元组的第一个元素
# print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
# print(tuple[2:])  # 输出从第三个元素开始的所有元素
# print(tinytuple * 2)  # 输出两次元组
# print(tuple + tinytuple)  # 连接元组

# list = ['abcd', 786, 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']
#
# print(type(list))
# print(list)  # 输出完整列表
# print(list[0])  # 输出列表第一个元素
# print(list[1:3])  # 从第二个开始输出到第三个元素
# print(list[2:])  # 输出从第三个元素开始的所有元素
# print(tinylist * 2)  # 输出两次列表
# print(list + tinylist)  # 连接列表

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
#
# print(student)  # 输出集合，重复的元素被自动去掉
#
# if ('Rose' in student):
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
# print(a - b)  # a和b的差集
# print(a | b)  # a和b的并集
# print(a & b)  # a和b的交集
# print(a ^ b)  # a和b中不同时存在的元素

# l=[]
#
# while True:
#     n = input()
#     l.append(n)
#     if str(n)=='q':
#         break
# print(l)
# print(l.sort())

# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
#
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
#
# print(dict['one'])  # 输出键为 'one' 的值
# print(dict[2])  # 输出键为 2 的值
# print(tinydict)  # 输出完整的字典
# print(tinydict.keys())  # 输出所有键
# print(tinydict.values())  # 输出所有值

# def func(*a):
#     print(a)
#
# if __name__=='__main__':
#     func(4,9)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(str(self.name)+' '+str(self.age))
#
# class student(person):
#     def display(self):
#         print('self')
#
# if __name__=='__main__':
#     p=person('xiao',34)
#     s=student("x",45)
#     p.display()
#     s.display()

# l=[x*x for x in range(10)]
# print(l)

# def func(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# if __name__ == '__main__':
#     print(list(func(5)))
#     for i in func(5):
#         print(i)

# #qt
# #sk - learn
# import reprlib
# import math
# from cc import p, q  # 从cc.py里引入函数p,q
#
# if __name__ == '__main__':
#     print(pow(2, 4))
#     p()
#     q()

# 多线程
# import threading, zipfile
#
# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile
#
#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)
#
# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')
#
# background.join()  # Wait for the background task to finish
# print('Main program waited until background was done.')
