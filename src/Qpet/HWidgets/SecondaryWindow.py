import sys

from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

"""
api doc: https://www.riverbankcomputing.com/static/Docs/PyQt5/
api QPainter: https://blog.csdn.net/m0_38106923/article/details/120915162
api QPainter: https://blog.csdn.net/seniorwizard/article/details/111199575
"""

try:
    from Components.MoveComponent import DragWindow
except ImportError as err:
    from .Components.MoveComponent import DragWindow


class HMainFrame(QWidget, DragWindow):
    rightClicked = pyqtSignal([QPoint])

    def __init__(self):
        super(HMainFrame, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.rightClicked[QPoint].connect(self.showInfo)
        self.rightClicked[QPoint].connect(lambda x, y=(12, 32): self.showInfo(x, y))
        desktop = QApplication.desktop()
        self.setFixedSize(int(desktop.width() * 0.6), int(desktop.height() * 0.6))

    def _setSize(self, size):
        self.setFixedSize(size)

    def showInfo(self, pos, y):
        print("相对于应用窗口的鼠标位置", pos)
        print("相对于桌面左上角的鼠标位置", QCursor.pos())
        print(y)

    def mousePressEvent(self, evt):
        super(HMainFrame, self).mousePressEvent(evt)
        DragWindow.mousePressEvent(self, evt)
        if evt.button() == Qt.RightButton:
            self.rightClicked[QPoint].emit(evt.pos())

    def paintEvent(self, a0: QPaintEvent) -> None:
        super(HMainFrame, self).paintEvent(a0)
        painter = QPainter()
        painter.begin(self)
        self.drawArea(painter, QRect(10, 10, 90, 90))
        self.drawLine(painter)
        self.drawArea(painter, QRect(100, 10, 90, 90))
        self.drawText(painter, QRect(10, 10, 90, 90))
        painter.end()

    def drawArea(self, painter, rect: QRect):
        brush = QBrush()
        brush.setColor(QColor(255, 255, 50))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(rect)

    def drawLine(self, painter):
        pen = QPen()
        pen.setColor(QColor(0, 255, 0))
        pen.setWidth(15)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.FlatCap)
        # pen.setJoinStyle(Qt.BevelJoin)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)
        # line = QLine(QPoint(100, 100), QPoint(100, 200))
        # painter.drawLine(line)
        painter.drawPolyline(QPoint(20, 30), QPoint(100, 200), QPoint(200, 200))

    def drawText(self, painter: QPainter, rect: QRect):
        painter.setPen(QColor(200, 20, 20))
        painter.setFont(QFont('SimSun', 20))
        painter.drawText(rect, Qt.AlignCenter, "TEXT")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = HMainFrame()
    frame.show()
    sys.exit(app.exec())
