from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
"""
https://blog.csdn.net/weixin_48668114/article/details/126805047?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-126805047-blog-105907762.235%5Ev34%5Epc_relevant_increate_t0_download_v2_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-126805047-blog-105907762.235%5Ev34%5Epc_relevant_increate_t0_download_v2_base&utm_relevant_index=2
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resize(1000, 30)

    def init_ui(self):
        button = [0, 0, 0]
        for i in range(3):
            button[i] = QPushButton(str(i), self)
        horizontal_Layout = QHBoxLayout()
        horizontal_Layout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.VLine)
        h_line.setFrameShadow(QFrame.Sunken)
        h_line.setObjectName("line")
        horizontal_Layout.addWidget(button[0])
        horizontal_Layout.addItem(spacerItem)
        horizontal_Layout.addWidget(button[1])
        horizontal_Layout.addWidget(h_line)
        horizontal_Layout.addWidget(button[2])
        self.setLayout(horizontal_Layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
