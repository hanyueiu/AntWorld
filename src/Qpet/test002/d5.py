

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject, QEvent, QBasicTimer
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient, \
    QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QSplitter, QVBoxLayout, QPushButton, QTextEdit, \
    QStyleOption, QStyle, QProgressBar
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QFont
# from PyQt5.QtGui import QLinearGradient
from test002.qss import Qss
import test002.test_qrc
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar



class HProgressBar(QProgressBar):

    def __init__(self, parent):
        super(HProgressBar, self).__init__(parent)
        self.img_001 = ':/images/img001.png'
        self.setObjectName("widget_bg")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowIcon(QIcon(self.img_001))
        self.setStyleSheet(Qss)
        # print(self.testAttribute(Qt.WA_TranslucentBackground))
        self.setStyleSheet(
            """QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;

            text-align: right;
            border-image: url(:/images/img002.png) no-repeat 0px 0px;
            }
            QProgressBar::chunk {
            border-image: url(:/images/img003.png);

}""")
    #
    #
    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     opt = QStyleOption()
    #     opt.initFrom(self)
    #     painter = QPainter(self)
    #     self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = HProgressBar(self)
        self.pbar.setGeometry(10, 10, 300, 30)
        # self.pbar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 5px; padding: 0px}"
        #                         "QProgressBar::chunk {background-color: #CD96CD; width: 10px;}")
        self.pbar.setAlignment(Qt.AlignCenter)
        self.pbar.setFormat('%p%')
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(100)
        self.pbar.setValue(50)
        print(self.pbar.value())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())