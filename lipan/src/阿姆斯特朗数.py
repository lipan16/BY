# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数

lower = int(input("最小值: "))
upper = int(input("最大值: "))

for num in range(lower, upper + 1):
    sum = 0
    n = len(str(num))  # 指数

    # 检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if num == sum:
        print(num)
