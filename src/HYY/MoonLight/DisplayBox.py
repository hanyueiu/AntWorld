"""
https://blog.csdn.net/m0_58086930/article/details/125734826?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-125734826-blog-129162577.235^v36^pc_relevant_default_base3&spm=1001.2101.3001.4242.1&utm_relevant_index=3
MenuBar 上上方菜单栏

NavBarSub上方副导航
DisplayBox中间展示框
TaskBar下方任务按钮

NavBar 左边导航按钮和logo

InfoBox 右上基本信息展示，右下状态信息展示
"""
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QPushButton, QHBoxLayout

from AppStyle.StyleLoader import Loader
import Resource.resource_qrc


class BrowserSimple(QWidget):

    def __init__(self, parent=None):
        super(BrowserSimple, self).__init__(parent)
        self.setObjectName("BrowserWidget")
        self.setStyleSheet("background:rgb(255,255,235)")
        self.initParams()
        self.initLayout()

    def initParams(self):
        Loader.boundAttach(self)

    def initLayout(self):
        self.stackedWidget = QStackedWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)
        Loader.spaceAttach(layout, 10)
        Loader.boundAttach(layout)
        self.create_page(None)


    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     width = self.width()
    #     height = self.height()
    #     self.stackedWidget.setGeometry(0, 0, width, height)

    def create_page(self, bar_dict):
        video_page = QWidget(self)
        bar_dict = {"nav_bar": ["先", "魔", "要"]}
        sub_nav = QWidget()
        for bar in bar_dict["nav_bar"]:
            layout_bar = QHBoxLayout()
            button = QPushButton(bar, sub_nav)
            layout_bar.addWidget(button)
            Loader.spaceAttach(layout_bar)
            Loader.boundAttach(layout_bar)
            sub_nav.setLayout(layout_bar)
        v = QHBoxLayout()
        v.addWidget(sub_nav)
        video_page.setLayout(v)

