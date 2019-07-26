from src_keras.train_Dense import train, test
from src_keras.train_CNN import train, test
from src_keras.predict import Predict_CNN, Predict_Dense

if __name__ == '__main__':
    # train(Is_continue=False)
    # test()
    Predict_CNN()
pass

    # while True:
    #     print("     1.训练    ")
    #     print("     2.测试    ")
    #     print("     3.预测    ")
    #     print("     0.结束    ")
    #     try:
    #         index = int(input(">>>"))
    #     except:
    #         print("非法输入，请重新输入！")
    #         continue
    #     if index == 0:
    #         break
    #     elif index == 1:
    #         train(Is_continue=False)
    #     elif index == 2:
    #         test()
    #     elif index == 3:
    #         Predict_CNN()
    #     else:
    #         print("输入错误，请重新输入")


