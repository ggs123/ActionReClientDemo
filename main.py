# coding=utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QFrame, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import utils
import cv2
from wind import ObjectInfoView
from controller import Controller
from PyQt5.QtCore import QObject, pyqtSignal
from model import Model
from PIL import Image


class ActionRe(QWidget):
    # 初始化成功的信号
    initOkSignal = pyqtSignal(str, str)

    def __init__(self, model):
        super(QWidget, self).__init__()

        self.__model = model
        self.__model.imageChangedSignal.connect(self.getImage)

        self.lb = QLabel(self)
        self.initUI()

    def initUI(self):
        self.resize(1120, 630)
        self.lb.setLineWidth(0)
        self.lb.setGeometry(0, 0, 960, 540)
        self.lb.setStyleSheet("border: 0px")
        self.lb.setScaledContents(True)

    def getImage(self, msg1, msg2):
        print(555)
        print("QSlot get msg => " + msg1+' '+msg2)
        image = self.__model.getImage()

        pix = Image.fromarray(image).toqpixmap()
        self.lb.setPixmap(pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = Model()
    view = ActionRe(model)
    controller = Controller(model)

    view.initOkSignal.connect(controller.route)
    view.initOkSignal.emit("startTimer", None)
    print(111)

    view.show()
    sys.exit(app.exec_())
