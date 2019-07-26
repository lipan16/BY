import tkinter as tk
from src.train_CNN import train, test
from src.predict_CNN import Predict_CNN

# window = tk.Tk()
# window.title('my window') # 窗口标签
# window.geometry('400x200') #窗口大小
#
#
# var1 = tk.StringVar()  # 文字变量储存器
# var2 = tk.StringVar()  # 文字变量储存器
# var3 = tk.StringVar()  # 文字变量储存器
# var1.set('train')
# var2.set('test')
# var3.set('predict')


# on_hit = False  # 默认初始状态为 False
# def hit_train():
#     global on_hit
#     if on_hit == False:
#         var1.set('begin training')   # 设置标签的文字为 'begin training'
#         train(Is_continue=False)
#         on_hit = True
#     else:
#         on_hit = False
#         var1.set('end train')
#
def hit_train():
    print('training')

# but1 = tk.Button(window,
#     textvariable=var1,      # 显示在按钮上的文字
#     width=15, height=2,
#     command=hit_train)     # 点击按钮式执行的命令
# but1.pack()    # 按钮位置
#
# but2 = tk.Button(window,
#     textvariable=var2,
#     width=15, height=2,
#     command=hit_train)
# but2.pack()
#
# but3 = tk.Button(window,
#     textvariable=var3,
#     width=15, height=2,
#     command=hit_train)
# but3.pack()

# b1 = tk.Button(window,text="insert point",width=15,height=2,command=hit_train())
# b1.pack()
#
# b2 = tk.Button(window,text="insert end",command=hit_train())
# b2.pack()
#
# window.mainloop()


from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="QUIT", fg="red",width=15,height=2,
                         command=quit)
    self.button.pack(side=LEFT)

    self.slogan1 = Button(frame,
                         text="train",width=15,height=2,
                         command=self.begin_train)
    self.slogan1.pack(side=LEFT)
    self.slogan2 = Button(frame,
                         text="test",width=15,height=2,
                         command=self.begin_test)
    self.slogan2.pack(side=LEFT)
    self.slogan3 = Button(frame,
                         text="predict",width=15,height=2,
                         command=self.begin_predict)
    self.slogan3.pack(side=LEFT)

  def begin_train(self):
    train(Is_continue=False)
  def begin_test(self):
    test()
  def begin_predict(self):
      Predict_CNN()

root = Tk()
app = App(root)
root.mainloop()