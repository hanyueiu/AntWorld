from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QEvent, QObject
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget

from AppStyle.StyleLoader import Loader
from Dandelion import PushButton, VBoxLayout, Widget, ScrollArea
from AppStyle.StyleQss import QSS, StyleQss


class NavWidget(QWidget):

    def __init__(self, parent=None):
        super(NavWidget, self).__init__(parent)
        self.topfiller = Widget()
        self.scroll = ScrollArea()
        self.scroll.setObjectName("nav_bar")
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.topfiller)
        self.items_layout = VBoxLayout()
        self.topfiller.setLayout(self.items_layout)
        self.normal_layout = VBoxLayout()
        self.normal_layout.addWidget(self.scroll)
        self.setLayout(self.normal_layout)
        self.init_bound()
        self.layout_scroll()
        self.setStyleSheet(QSS)

    def init_bound(self):
        # Nav背景窗口
        # Loader.attrAttach(self.scroll)
        Loader.attrAttach(self.topfiller)
        Loader.boundAttach(self.topfiller)
        Loader.boundAttach(self.scroll)
        Loader.boundAttach(self.normal_layout)
        Loader.boundAttach(self.items_layout)
        Loader.spaceAttach(self.items_layout)

    def layout_scroll(self):

        item_list = ["视频", "音频", "YYH"] * 1
        self.item_height = 42
        self.item_border = 0
        self.color = QColor(121, 44, 121, 255)

        for filename in item_list:
            button = PushButton(self.topfiller)
            button.setObjectName("NavPushButton")
            # 使用父窗口的eventFilter函数进行处理
            button.installEventFilter(self.parent())
            button.setText(str(filename))
            button.setCheckable(True)
            button.clicked.connect(self.button_click)
            self.items_layout.addWidget(button)

    def button_click(self, e: QtCore.QEvent):
        source = self.sender()
        print(source.text())
        return
        for item_index in range(self.items_layout.count()):
            item = self.items_layout.itemAt(item_index).widget()
            if source.text() == item.text():
                item.setStyleSheet(StyleQss.get_qss(nav_color=StyleQss.white))
            else:
                item.setStyleSheet(StyleQss.get_qss(nav_color=StyleQss.nav_color))

    def resizeEvent(self, a0) -> None:
        super(NavWidget, self).resizeEvent(a0)

        # 对滚动条区域进行尺寸修正
        self.topfiller.setFixedWidth(self.width())
        self.topfiller.setFixedHeight(self.items_layout.count() * self.item_height)
        # 对按钮进行尺寸修正
        for item_index in range(self.items_layout.count()):
            self.items_layout.itemAt(item_index).widget().setFixedSize(self.topfiller.width(), self.item_height)

