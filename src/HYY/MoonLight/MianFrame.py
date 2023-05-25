import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt, QRectF, QRect
from PyQt5.QtWidgets import QWidget, QApplication

from AppAlg.Move import DragAlg
from AppStyle.StyleLoader import Loader
from AppStyle.StyleQss import StyleQss
from Dandelion import Icon, Pixmap

from MoonLight.LogoWidget import LogoWidget, LogoBWidget
from MoonLight.NavWidget import NavWidget
import Resource.resource_qrc


class MainFrame(QWidget, DragAlg):

    def __init__(self):
        super(MainFrame, self).__init__()
        self.setObjectName("MainFrame")
        # 设置标题栏的icon
        self.setWindowIcon(Icon(Pixmap(":/images/moon.png")))
        self.setWindowTitle("一月寒")
        self.setStyleSheet(StyleQss.get_qss())
        self.setSize()
        # Loader.attrAttach(self)
        Loader.boundAttach(self)
        Loader.flagDetach(self)
        self.addWidget()

    def setSize(self, size=None):
        if not size:
            desktop = QApplication.desktop()
            # PyQt5.QtCore.QSize(1920, 1080)
            width, height = int(desktop.width() * 0.6), int(desktop.height() * 0.6)
            print(width, height)
            self.setFixedSize(QSize(width, height))
        else:
            self.setSize(*size)

    def addWidget(self):
        self.logo = LogoWidget(self)
        self.nav = NavWidget(self)
        self.logo_b = LogoBWidget(self)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width = self.width()
        height = self.height()

        self.logo.setGeometry(QRect(0, 0, self.setInt(width, 0.15), self.setInt(width, 0.15) - 1))
        self.nav.setGeometry(QRect(0, self.setInt(width, 0.15), self.setInt(width, 0.15), height - self.setInt(width, 0.3)))
        self.logo_b.setGeometry(QRect(0, height - self.setInt(width, 0.15), self.setInt(width, 0.15), self.setInt(width,  0.15)))

    def setInt(self, length, ratio):
        return int(length * ratio)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainFrame()
    frame.show()
    sys.exit(app.exec())
