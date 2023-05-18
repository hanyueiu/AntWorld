import math
import sys
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import os
import sys
"""
api doc: https://www.riverbankcomputing.com/static/Docs/PyQt5/
api QPainter: https://blog.csdn.net/m0_38106923/article/details/120915162
api QPainter: https://blog.csdn.net/seniorwizard/article/details/111199575
"""
try:
    from HWidgets.Components.MoveComponent import DragWindow
except Exception as err:
    pa_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    sys.path.append(pa_path)
    if "HWidgets" in os.listdir(pa_path):
        from HWidgets.Components.MoveComponent import DragWindow


class HMainFrame(QWidget, DragWindow):

    rightClicked = pyqtSignal([QPoint, object], [QPoint])

    def __init__(self):
        super(HMainFrame, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.rightClicked[QPoint].connect(self.showInfoPos)
        self.rightClicked[QPoint, object].connect(self.showInfoPosConst)
        self._setSize()

    def _setSize(self, size=None):
        if not size:
            desktop = QApplication.desktop()
            self.setFixedSize(int(desktop.width() * 0.6), int(desktop.height() * 0.6))
        else:
            self.setFixedSize(size)

    def showInfoPos(self, pos):
        print("信号检测：鼠标坐标相对于应用窗口的鼠标坐标, 桌面左上角定点的鼠标坐标", pos, QCursor.pos())

    def showInfoPosConst(self, pos, const):
        """信号的定义， 信号绑定到函数， 信号的发射委托（一般由内置触发事件处理函数进行发射）"""
        print("信号重载检测：发射已到达接收区！", const)
        self.showInfoPos(pos)
        print("信号重载检测：接收已完成！", const)

    def mousePressEvent(self, evt):
        super(HMainFrame, self).mousePressEvent(evt)
        DragWindow.mousePressEvent(self, evt)
        if evt.button() == Qt.RightButton:
            self.rightClicked[QPoint].emit(evt.pos())
            self.rightClicked[QPoint, object].emit(evt.pos(), "Yes")

    def paintEvent(self, a0: QPaintEvent) -> None:
        super(HMainFrame, self).paintEvent(a0)

        title_top = QRect(1,
                          1,
                          self.floor(self.width() - 3),
                          self.floor(self.height() * 0.1) - 2)
        left = QRect(1,
                     self.floor(self.height() * 0.1 + 1),
                     self.floor(self.width() * 0.3 - 1),
                     self.floor(self.height() * 0.9 - 2)
                     )
        right_mid = QRect(self.floor(self.width() * 0.3) + 3,
                          self.floor(self.height() * 0.1 + 1),
                          self.floor(self.width() * 0.7 - 4),
                          self.floor(self.height() * 0.05)
                          )
        right_bottom = QRect(self.floor(self.width() * 0.3) + 3,
                             self.floor(self.height() * 0.15 + 2),
                             self.floor(self.width() * 0.7 - 4),
                             self.floor(self.height() * 0.85 - 3)
                             )
        # 画笔刷demo到最后
        painter = QPainter()
        painter.begin(self)
        self.drawArea(painter, title_top)
        self.drawLine(painter)
        self.drawArea(painter, left)
        self.drawArea(painter, right_mid)
        self.drawArea(painter, right_bottom)
        self.drawText(painter, title_top, "布局Demo")
        painter.end()

    def drawArea(self, painter, rect: QRect):
        brush = QBrush()
        brush.setColor(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(rect)

        # 恢复默认笔刷
        painter.setBrush(QBrush())

    def drawLine(self, painter):
        pen = QPen()
        pen.setColor(QColor(0, 255, 0))
        pen.setWidth(1)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.FlatCap)
        # pen.setJoinStyle(Qt.BevelJoin)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawPolyline(QPoint(0, 0),
                             QPoint(0, self.floor(self.height() * 0.1)),
                             QPoint(self.width(), self.floor(self.height() * 0.1)),
                             QPoint(self.width() - 1, self.height() - 1)
                             )

        # 恢复默认画笔
        painter.setPen(QColor())

    def drawText(self, painter: QPainter, rect: QRect, text="TEXT"):
        painter.setPen(QColor(200, 20, 20))
        painter.setFont(QFont('SimSun', 20))
        painter.drawText(rect, Qt.AlignCenter, text)

    def floor(self, val: float):
        """向下取整"""
        import math
        return int(math.floor(val))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    frame = HMainFrame()
    frame.show()
    sys.exit(app.exec())
