from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5 import QtGui
from AppStyle.StyleLoader import Loader
from AppStyle.StyleQss import StyleQss


class NavSubWidget(QWidget):

    def __init__(self, parent=None):
        super(NavSubWidget, self).__init__(parent)
        self.setNavBar("Debug")
        self.setStyleSheet(StyleQss.get_qss())
        Loader.attrAttach(self)

    def setNavBar(self, nav_bar: dict):
        nav_bar = dict().fromkeys(list(range(3)))
        self.layout_bar = QHBoxLayout()
        for name, info_func in nav_bar.items():
            info_func = lambda x: print(x)
            print(name, info_func)
            button = QPushButton(str(name)+"收沙", self)
            button.setObjectName("NavSubPushButton")
            button.setCheckable(True)
            button.clicked.connect(info_func)
            Loader.spaceAttach(self.layout_bar)
            Loader.boundAttach(self.layout_bar)
            self.layout_bar.addWidget(button)
            self.setLayout(self.layout_bar)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        # 对按钮进行尺寸修正
        for item_index in range(self.layout_bar.count()):
            self.layout_bar.itemAt(item_index).widget().setFixedSize(100, height)


if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
    from PyQt5.QtWidgets import QWidget, QApplication
    app = QApplication(sys.argv)
    frame = NavSubWidget(None)
    frame.show()
    sys.exit(app.exec())