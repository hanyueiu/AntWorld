import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScrollMessageBox(QMessageBox):
    def __init__(self, l, *args, **kwargs):
        QMessageBox.__init__(self, *args, **kwargs)
        scroll = QScrollArea(self)
        print(self.size())
        scroll.setWidgetResizable(True)
        print(self.size())
        self.content = QWidget()
        scroll.setWidget(self.content)
        lay = QVBoxLayout(self.content)
        for item in l:
            q = QLabel(item, self)
            q.setStyleSheet("background:grey")
            lay.addWidget(q)
        self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
        self.setStyleSheet("QScrollArea{min-width:300 px; min-height: 400px}")


class W(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Show Message', self)
        self.btn.setGeometry(10, 10, 100, 100)
        self.btn.clicked.connect(self.buttonClicked)
        self.lst = [str(i) for i in range(500)]
        a = """We have encountered an error.
The following information may be useful in troubleshooting:
1
2
3
4
5
6
7
8
9
10
Here is the bottom.
"""
        self.lst.insert(0, a)
        self.show()

    def buttonClicked(self):
        result = ScrollMessageBox(self.lst, None)
        result.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = W()
    sys.exit(app.exec_())
