import sys
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QSplitter, QVBoxLayout, QPushButton, QTextEdit

from HWidgets.navFrame import NavWidget

try:
    from Components.MoveComponent import DragWindow
except ImportError as err:
    from .Components.MoveComponent import DragWindow


class HMainFrame(QWidget, DragWindow):
    rightClicked = pyqtSignal([QPoint, object], [QPoint])

    def __init__(self):
        super(HMainFrame, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.rightClicked[QPoint].connect(self.showInfoPos)
        self.rightClicked[QPoint, object].connect(self.showInfoPosConst)
        self._setSize()
        self.layoutCustom()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(255, 255, 255, 100)")
        # self.setStyleSheet("background:rgb(66, 66, 66)")

    def _setSize(self, size=None):
        if not size:
            desktop = QApplication.desktop()
            self.setFixedSize(int(desktop.width() * 0.6), int(desktop.height() * 0.6))
        else:
            self.setFixedSize(*size)

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

    def floor(self, val: float):
        """向下取整"""
        import math
        return int(math.floor(val))

    def layoutCustom(self):

        vbox = QVBoxLayout(self)
        cell_height = self.floor(self.height() * 0.05)
        cell_width = self.floor(self.width() * 0.05)
        toolBar = QFrame()
        toolBar.setFrameShape(QFrame.StyledPanel)  # 显示边框
        toolBar.setMaximumHeight(cell_height * 2)
        toolBar.setMinimumHeight(cell_height)

        navBar = NavWidget()
        # navBar.setFrameShape(QFrame.StyledPanel)
        navBar.setMinimumWidth(cell_width * 4)
        navBar.setMaximumWidth(cell_width * 4)
        print(navBar.size())

        header = QFrame()
        header.setFrameShape(QFrame.StyledPanel)
        header.setMinimumHeight(cell_height)
        header.setMaximumHeight(cell_height * 3)

        body = QFrame()
        body.setFrameShape(QFrame.StyledPanel)
        body.setMinimumHeight(cell_height)

        # 创建分割窗口
        splitter = QSplitter(Qt.Vertical, self)
        # 设置子控件不折叠, 需要设置Mini长度
        splitter.setChildrenCollapsible(False)
        # 设置分隔条宽度
        splitter.setHandleWidth(5)
        # 添加子控件
        splitter.addWidget(toolBar)

        splitter_bottom = QSplitter(Qt.Horizontal, splitter)
        # 也可以按照索引insertWidget
        splitter_bottom.addWidget(navBar)
        splitter_bottom.setChildrenCollapsible(False)
        splitter_right = QSplitter(Qt.Vertical, splitter_bottom)
        splitter_right.addWidget(header)
        splitter_right.addWidget(body)
        # 按照索引设置子控件不折叠
        splitter_right.setCollapsible(0, False)
        splitter_right.setCollapsible(1, False)

        vbox.addWidget(splitter)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = HMainFrame()
    frame.show()
    sys.exit(app.exec())
