from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QPushButton, QScrollArea


class NavWidget(QFrame):

    def __init__(self, parent=None):
        super(NavWidget, self).__init__(parent)
        self.topfiller = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.topfiller)
        self.items_button = QVBoxLayout()
        self.topfiller.setLayout(self.items_button)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.setLayout(self.vbox)
        self.layout_scroll()

        self.topfiller.setAttribute(Qt.WA_TranslucentBackground)
        self.scroll.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("""QScrollArea{
                border-radius: 1px;
                border: 1px solid ;
                border-color: rgba(200,200,200,100)
            }""")

    def layout_scroll(self):
        num = 10
        for filename in range(num):
            button = QPushButton(self.topfiller)
            button.mouseMoveEvent = lambda a0: None
            button.setText(str(filename))
            button.setStyleSheet("""QPushButton{background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(198, 172, 190, 100), stop:0.5 rgba(239, 221, 234,100), stop:1 rgba(164, 178, 201, 100));border-radius:0px;color:white;}""")
            self.layout_item(button)

    def resizeEvent(self, a0) -> None:
        super(NavWidget, self).resizeEvent(a0)
        # 对滚动条区域进行尺寸修正
        self.topfiller.setFixedWidth(self.width() - 30)
        self.topfiller.setFixedHeight(self.items_button.count() * 60)
        # 对按钮进行尺寸修正
        list(map(lambda index: self.items_button.itemAt(index).widget().setFixedSize(self.topfiller.width(), 52), range(self.items_button.count())))

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(NavWidget, self).paintEvent(a0)

    def layout_item(self, item):
        self.items_button.addWidget(item)

