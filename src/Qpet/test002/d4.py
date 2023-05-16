import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject, QEvent
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient, \
    QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QSplitter, QVBoxLayout, QPushButton, QTextEdit, \
    QStyleOption, QStyle

from HWidgets.Components.MoveComponent import DragWindow
from test002.d3 import TMainFrame
from test002.qss import Qss
import test002.test_qrc


class WButton(QPushButton):
    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        return None


class WFrame(QWidget, DragWindow):

    def __init__(self):
        super(WFrame, self).__init__()
        self.setFixedSize(600, 400)
        # YYHKey 在父窗口展示使用打包成源码的图片显示的子窗口
        tm = TMainFrame(self)
        self.setObjectName("widget_main")
        self.setStyleSheet(Qss)

        # YYHKey 在父窗口展示按钮的hover,pressed以及自然状态下的颜色
        b = WButton(self)
        b.setGeometry(100, 100, 60, 30)
        b.setStyleSheet("""QPushButton{background:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, 
        stop:0 blue, stop:0.5 green, stop:1 blue);border-radius:5px;color:white;}
        QPushButton:hover:!pressed {border:1px solid #f8878f;}
        QPushButton:pressed {padding-left:6px;padding-top:6px;border:1px solid blue;}""")

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = WFrame()
    frame.show()
    sys.exit(app.exec())
