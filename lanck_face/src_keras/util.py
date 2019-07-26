import os

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
