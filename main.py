# coding=utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from controller import Controller
from PyQt5.QtCore import pyqtSignal
from model import Model
from PIL import Image


class ActionRe(QWidget):
    # 初始化成功的信号
    initOkSignal = pyqtSignal(str, str)

    def __init__(self, model):
        super(QWidget, self).__init__()

        self.__model = model
        self.__model.dataChangedSignal.connect(self.getData)

        self.lb = QLabel(self)
        self.initUI()

    def initUI(self):
        self.resize(1120, 630)
        self.lb.setLineWidth(0)
        self.lb.setGeometry(0, 0, 960, 540)
        self.lb.setStyleSheet("border: 0px")
        self.lb.setScaledContents(True)

    def getData(self):
        '''响应model数据更新信号，更新界面

        :return: 无
        '''
        data = self.__model.getData()

        self.updataUI(data)

    def updataUI(self, data):
        ''' 更新界面中的内容

        :param data:{
                    'img': ndarray(画上姿态的图片),
                    'boundingBox': [ndarray(未画上姿态的框内图片)],
                    'nameAndAction': [['葛某', '走']]
                }
        :return: 无
        '''
        img = data['img']

        pix = Image.fromarray(img).toqpixmap()
        self.lb.setPixmap(pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = Model()
    view = ActionRe(model)
    controller = Controller(model)

    # 视图更新完成，通知controller
    view.initOkSignal.connect(controller.route)
    view.initOkSignal.emit("startTimer", None)

    view.show()
    sys.exit(app.exec_())
