# coding=utf-8
import sys
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QWidget, QFrame, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import time


class ObjectInfoView(QFrame):

    __views_count__ = 0

    def __new__(cls, *args, **kwargs):
        cls.__views_count__ += 1
        return super().__new__(cls)

    def __init__(self, parent, img: QPixmap = None, person: str = '', action: str = ''):
        super().__init__(parent=parent)
        self.setObjectName(str(ObjectInfoView.__views_count__) + str(time.time()))
        self.view_img = QLabel(self)
        self.view_tag_per = QLabel(self)
        self.view_tag_ac = QLabel(self)
        self.set_image(img)
        self.set_person(person)
        self.set_action(action)
        self.initUI()

    def initUI(self):
        self.view_img.setGeometry(20, 15, 60, 60)
        self.view_tag_per.setGeometry(90, 20, 50, 20)
        self.view_tag_ac.setGeometry(90, 50, 50, 20)

    def set_image(self, img: QPixmap = None):
        if img is None:
            self.view_img.clear()
            return
        w = img.size().width()
        h = img.size().height()
        if w > h:
            pix = img.scaledToWidth(60)
        else:
            pix = img.scaledToHeight(60)
        self.view_img.setPixmap(pix)

    def set_person(self, per: str = ''):
        self.view_tag_per.setText(per)

    def set_action(self, ac: str = ''):
        self.view_tag_ac.setText(ac)

    def set_default_geometry(self):
        y = (ObjectInfoView.__views_count__ - 1) * 90
        self.setGeometry(960, y, 160, 90)

    def set_remove(self):
        ObjectInfoView.__views_count__ -= 1
        self.setParent(None)
        self.deleteLater()


class ActionReUI(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.lb = QLabel(self)
        self.timer = QBasicTimer()
        self.initUI()

    def initUI(self):
        self.resize(1120, 630)

        self.lb.setLineWidth(0)
        self.lb.setGeometry(0, 0, 960, 540)
        self.lb.setStyleSheet("border: 0px")
        self.lb.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ActionReUI()
    ex.show()
    sys.exit(app.exec_())
