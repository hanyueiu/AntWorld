import math
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QLineF, QRect, QPointF
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen, QPolygon, QMouseEvent

from AppStyle.StyleQss import StyleQss
from Dandelion import PushButton, Widget, VBoxLayout
from MoonLight.LogoWidget import LogoWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFrame
from Resource import resource_qrc


class IcoButton(Widget):
    def __init__(self, parent=None, draw=None):
        super(IcoButton, self).__init__(parent)
        self.type = {"mini": self.mini_ico, "close": self.close_ico, "setting": self.setting_ico}
        self.draw = self.type.get(draw, None) if draw else None
        width, height = self.width(), self.height()
        self.setFixedSize(50, 50)

    def mini_ico(self, painter: QPainter):
        #  颜色， 笔宽， 实线， 平顶， 平滑连接
        pen = QPen(Qt.gray, 3, Qt.SolidLine, Qt.FlatCap, Qt.RoundJoin)
        painter.setPen(pen)
        line = QLineF(self.width() * 0.1, self.height() / 2, self.width() * 0.8, self.height() / 2)
        painter.drawLine(line)
    def close_ico(self, painter: QPainter):
        pass

    def setting_ico(self, painter: QPainter):
        points = []
        rx, ry = self.width() / 2, self.height() / 2
        for i, d in enumerate(range(0, 360, 30)):
            if i % 2 == 1:
                r = self.height() / 2
            else:
                r = self.height() / 2.5

            point = QPointF(rx + r * math.cos(2 * math.pi / 360 * d), ry + r * math.sin(2 * math.pi / 360 * d))
            points.append(point)
        #  颜色， 笔宽， 实线， 圆顶， 平滑连接
        pen = QPen(Qt.gray, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawPolygon(*points)
        # polygon = QPolygon()
        # polygon.setPoints(1,1,2,2,3,3)
        # painter.drawPolygon(polygon)

        pen = QPen(Qt.gray, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(pen)
        area_m = LogoWidget.get_scale(QRect(0, 0, self.width(), self.height()), 0.1)
        print(area_m, rx, ry)
        painter.drawArc(area_m, 360 * 16, 360 * 16)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(IcoButton, self).paintEvent(a0)
        painter = QPainter()
        # 设置反锯齿
        painter.setRenderHint(painter.Antialiasing)
        brush = QBrush()
        painter.begin(self)
        self.draw(painter)
        painter.end()


class TitleWidget(QWidget):
    def __init__(self, parent=None):
        super(TitleWidget, self).__init__(parent)
        self.offset_d = 10
        self.frame = parent
        self.layout_widget()


    def layout_widget(self):
        self.title_widget = Widget(self)
        self.title_widget.setObjectName("title_widget")

        self.title_label = QLabel(self.title_widget)
        self.title_label.setObjectName("title_text")
        self.title_label.setText("这是一个title!")

        self.mini_button = QPushButton(self.title_widget)
        self.mini_button.setObjectName("minimize_btn")
        self.mini_button.mouseMoveEvent = lambda a0: None
        self.mini_button.clicked.connect(lambda x: self.parent().showMinimized())

        self.close_button = QPushButton(self.title_widget)
        self.close_button.setObjectName("close_btn")
        self.close_button.mouseMoveEvent = lambda a0: None
        self.close_button.clicked.connect(lambda x: self.parent().close())

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        width, height = self.width(), self.height()

        self.title_widget.setGeometry(0,  0, width, height)
        self.title_label.setGeometry(height, 0, width*0.2, height)
        self.close_button.setGeometry(width - height - self.offset_d, 0, height, height)
        self.mini_button.setGeometry(width - height * 2 - self.offset_d, 0, height, height)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QWidget, QApplication

    app = QApplication(sys.argv)
    frame = TitleWidget(None)
    frame.show()
    sys.exit(app.exec())
