
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QSplitter, QVBoxLayout, QPushButton, QTextEdit, \
    QScrollArea, QLabel, QGridLayout
"""
https://blog.csdn.net/weixin_48668114/article/details/126805047?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-126805047-blog-105907762.235%5Ev34%5Epc_relevant_increate_t0_download_v2_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-126805047-blog-105907762.235%5Ev34%5Epc_relevant_increate_t0_download_v2_base&utm_relevant_index=2
"""


class NavWidget(QFrame):

    def __init__(self, parent=None):
        super(NavWidget, self).__init__(parent)
        self.layout_scroll_demo()

    def layout_scroll_demo(self):
        self.topfiller = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topfiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.setLayout(self.vbox)
        print(self.size(), self.sizeHint())
        num = 1000
        width, height = self.size().width()/4, 100
        for filename in range(num):
            mapbutton = QPushButton(self.topfiller)

            mapbutton.setText(str(filename))
            mapbutton.move(0, filename * 40)
            mapbutton.setFixedSize(width, height)
            mapbutton.setStyleSheet("background:grey")

        self.topfiller.setMinimumSize(width, num * height)


    def demo_scroll(self):
        self.topfiller = QWidget()
        self.topfiller.setMinimumSize(250, 2000)  #######设置滚动条的尺寸
        ##创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topfiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.setLayout(self.vbox)
        for filename in range(50):
            self.mapbutton = QPushButton(self.topfiller)
            self.mapbutton.setText(str(filename))
            self.mapbutton.move(10, filename * 40)

    def resizeEvent(self, a0) -> None:
        super(NavWidget, self).resizeEvent(a0)
        print(self.size())
