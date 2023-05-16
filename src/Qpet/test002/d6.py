import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject, QBasicTimer
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient, \
    QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QSplitter, QVBoxLayout, QHBoxLayout, \
    QPushButton, QTextEdit, QStyleOption, QStyle, QLabel
from PIL import Image, ImageDraw
from HWidgets.Components.MoveComponent import DragWindow

from test002.qss import Qss
import test002.test_qrc


class FirstTimer(QWidget):
    def __init__(self):
        super(FirstTimer, self).__init__()
        self.setObjectName("mainframe")
        self.setStyleSheet(Qss)
        self.setFixedSize(400, 300)
        self.timer = QBasicTimer()
        self.timer.start(100, self)
        self.val = 0
        print(self.timer.isActive())
        from test002.d3 import TMainFrame
        self.h_progress = TMainFrame(self)
        self.h_progress.setValue(0)
        print(self.h_progress.size())
        self.h_progress.move(0, 0)

        self.h_layout = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText("%d %%" % self.val)
        self.h_layout.addWidget(self.h_progress)
        self.h_layout.addWidget(self.label, 0, Qt.AlignLeft | Qt.AlignCenter)
        self.setLayout(self.h_layout)

    def timerEvent(self, e):
        if self.val == 100:
            self.timer.stop()
        else:
            self.val += 1
            self.h_progress.setValue(self.val)
            self.h_progress.update()

            self.label.setText("%d %%" % self.val)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = FirstTimer()
    frame.show()
    sys.exit(app.exec())
