# coding=utf-8

import cv2

def imreadRGB(path):
    return cv2.cvtColor(cv2.imread(str(path)), cv2.COLOR_BGR2RGB)
    

def imwriteRGB(path, image):
    cv2.imwrite(str(path), cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    


if __name__ == '__main__':
    pass