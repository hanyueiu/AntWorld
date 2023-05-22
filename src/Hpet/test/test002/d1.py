import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient, \
    QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QSplitter, QVBoxLayout, QPushButton, QTextEdit

from HWidgets.Components.MoveComponent import DragWindow


class TMainFrame(QWidget, DragWindow):

    def __init__(self):
        super(TMainFrame, self).__init__()
        # YYHKey: 使用相对位置的图片展示于窗口， 任务栏
        self.img_001 = './Images/img001.png'
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(self.img_001))
        # self.setFixedSize(300, 30)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap(self.img_001)
        self.setFixedSize(pixmap.size())
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = TMainFrame()
    frame.show()
    sys.exit(app.exec())
