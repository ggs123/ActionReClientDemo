# coding=utf-8
from PyQt5.QtCore import QBasicTimer
import utils
from PyQt5.QtCore import QObject
import Visualization
import cv2


class Controller(QObject):
    def __init__(self, model):
        super(Controller, self).__init__()
        self.__model = model
        self.__timer = QBasicTimer()

    def route(self, msg1, msg2):
        ''' 接收view的请求，并通过查找表调用对应的处理方法

        :param msg1: 响应view请求的方法名称
        :param msg2: 请求对应的参数(暂时没有用到)
        :return: 无
        '''
        {"startTimer": self.startTimer}[msg1](msg2)

    def startTimer(self, msg):
        ''' 开启定时器

        :param msg: 暂时用不到
        :return: 无
        '''
        self.__timer.start(25, self)

    def onSetData(self):
        ''' 获取数据，并更新model的数据

        :return: 无
        '''
        data = utils.get_data()

        processedData = self.processData(data)
        self.__model.setData(processedData)

    def processData(self, data):
        ''' 对获取到的数据做进一步的处理

        :param data:{
                    'img_b': 二进制图片,
                    'pose': ndarray,
                    'boundingBox': [[39, 917, 336, 886], [39, 917, 336, 886]],
                    'nameAndAction': [['葛某', '走'], ['葛某', '走']]
                    }
        :return:{
                'img': ndarray(画上姿态的图片),
                'boundingBox': [ndarray(未画上姿态的框内图片), ndarray(未画上姿态的框内图片)],
                'nameAndAction': [['葛某', '走'], ['葛某', '走']]
                }
        '''

        img_b = data['img_b']
        img_np = Visualization.np.frombuffer(img_b, Visualization.np.uint8)
        img_cv = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

        result = {
            'img': img_cv,
            'boundingBox': None,
            'nameAndAction': [['葛某', '走']]
        }

        return result

    def timerEvent(self, a0):
        self.onSetData()


if __name__ == '__main__':
    pass