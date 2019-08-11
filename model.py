# coding=utf-8
from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):
    # 数据更新的信号
    dataChangedSignal = pyqtSignal()

    def __init__(self):
        super(Model, self).__init__()
        self.__data = None

    def setData(self, data):
        self.__data = data

        # 数据更新完成，通知view
        self.run()

    def getData(self):
        return self.__data

    def run(self):
        '''发出数据更新的信号

        :return: 无
        '''

        self.dataChangedSignal.emit()


if __name__ == '__main__':
    pass
