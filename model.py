# coding=utf-8
from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):
    # 数据更新的信号
    imageChangedSignal = pyqtSignal(str, str)

    def __init__(self):
        super(Model, self).__init__()
        self.__image = None

    def setImage(self, image):
        self.__image = image
        self.run()

    def getImage(self):
        return self.__image

    def run(self):
        self.imageChangedSignal.emit("1", "2")
        print(444)


class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()
    #槽对象中的槽函数
    # def get( self,msg ):
    #     print("QSlot get msg => " + msg)

    #todo 优化 多个参数
    def get(self, msg1, msg2):
        print("QSlot get msg => " + msg1+' '+msg2)


if __name__ == '__main__':
    send = Model()
    slot = QTypeSlot()

    print('_____-把信号绑定到槽函数上_)___')
    send.imageChangedSignal.connect(slot.get)

    send.run()

    print('_____-把信号与槽函数解绑_)___')
    send.imageChangedSignal.disconnect(slot.get)

    send.run()
