import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPaintEvent, QPainter
from PyQt5.QtWidgets import QProgressBar, QApplication, QWidget, QStyleOption, QStyle
from test002.qss import Qss


class TextProgressBar(QProgressBar):

    def __init__(self, *args, **kwargs):
        super(TextProgressBar, self).__init__(*args, **kwargs)
        self.setObjectName("text_widget")
        self.setFixedSize(200, 30)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(':/images/bg.png'))
        self.setStyleSheet(Qss)

    def paintEvent(self, a0: QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mytask = TextProgressBar()
    mytask.show()
    sys.exit(app.exec_())
