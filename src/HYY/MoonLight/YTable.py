import sys

from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QTableWidget, QVBoxLayout, QHeaderView, QTableWidgetItem, \
    QApplication, QMenu
from PyQt5 import QtGui
from AppStyle.StyleLoader import Loader
from AppStyle.StyleQss import StyleQss


class YTableWidget(QWidget):
    table_data = pyqtSignal(object)

    def __init__(self, parent=None):
        super(YTableWidget, self).__init__(parent)
        self.initLayout()

    def initLayout(self):
        self.vLayout = QVBoxLayout()
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setObjectName("TaskTableWidget")
        self.vLayout.addWidget(self.tableWidget)
        Loader.spaceAttach(self.vLayout)
        Loader.boundAttach(self.vLayout)
        self.setLayout(self.vLayout)

        # 允许右键产生菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

    def generateMenu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
            print(row_num)
        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction("右键点中了一行")

            action = menu.exec(self.tableWidget.mapToGlobal(pos))
            if action == item1:
                print('第一项', self.tableWidget.item(row_num, 0).text(), self.tableWidget.item(row_num, 1).text(),
                      self.tableWidget.item(row_num, 2).text())

    def update_data(self, data):
        print(data)
        import random
        # count = random.choice(list(range(30)))
        # data = [[(i, j) for j in range(3)] for i in range(count)]
        rows, cols = len(data), 3
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)
        self.tableWidget.setHorizontalHeaderLabels(['bane', 'user', 'code'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()

        for row in range(rows):
            for col in range(cols):
                new_item = QTableWidgetItem(str(data[row][col]))
                new_item.setFlags(Qt.ItemIsEnabled)
                self.tableWidget.setItem(row, col, new_item)
        self.tableWidget.viewport().update()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        super(YTableWidget, self).mousePressEvent(a0)
        print(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = YTableWidget()
    win.show()
    sys.exit(app.exec_())
