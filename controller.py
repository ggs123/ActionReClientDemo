# coding=utf-8
from PyQt5.QtCore import QBasicTimer
import utils
import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal


class Controller(QObject):
    def __init__(self, model):
        super(Controller, self).__init__()
        self.__model = model
        self.__timer = QBasicTimer()

    def route(self, msg1, msg2):
        print(222)
        {"startTimer": self.startTimer}[msg1](msg2)

    def startTimer(self, msg):
        print(333)
        self.__timer.start(1000, self)

    def onSetImage(self):
        # data = utils.get_data()

        image = np.zeros((1080, 1920, 3), np.uint8)
        self.__model.setImage(image)

    def timerEvent(self, a0):
        self.onSetImage()


if __name__ == '__main__':
    pass