from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets


class Loader(object):
    @staticmethod
    def flagDetach(widget: QtWidgets.QWidget):
        # 去除窗口标志
        widget.setWindowFlag(Qt.FramelessWindowHint)

    @staticmethod
    def attrAttach(widget: QtWidgets.QWidget):
        # 窗口属性透明
        widget.setAttribute(Qt.WA_TranslucentBackground)

    @staticmethod
    def boundAttach(widget: (QtWidgets.QWidget, QtWidgets.QBoxLayout)):
        widget.setContentsMargins(0, 0, 0, 0)

    @staticmethod
    def spaceAttach(layout: QtWidgets.QBoxLayout):
        layout.setSpacing(0)
