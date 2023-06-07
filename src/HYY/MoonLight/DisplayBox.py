"""
https://blog.csdn.net/m0_58086930/article/details/125734826?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-125734826-blog-129162577.235^v36^pc_relevant_default_base3&spm=1001.2101.3001.4242.1&utm_relevant_index=3
MenuBar 上上方菜单栏

NavBarSub上方副导航
DisplayBox中间展示框
TaskBar下方任务按钮

NavBar 左边导航按钮和logo

InfoBox 右上基本信息展示，右下状态信息展示
"""
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QGridLayout, \
    QApplication, QLineEdit, QFrame

from AppStyle.StyleLoader import Loader
import Resource.resource_qrc
from AppStyle.StyleQss import StyleQss
from MoonLight.TaskBar import TaskWidget
from MoonLight.YTable import YTableWidget


class BrowserWidget(QWidget):

    def __init__(self, parent=None):
        super(BrowserWidget, self).__init__(parent)
        self.setObjectName("BrowserWidget")
        self.root_parent = parent
        self.initLayout()

    def initLayout(self):
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName("TaskStackedWidget")
        Loader.attrAttach(self.stackedWidget)
        # Loader.boundAttach(self.stackedWidget)
        layout = QVBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)
        Loader.spaceAttach(layout)
        Loader.boundAttach(layout)
        widgets_scale = ((0.92, 0.08), (1, 1))
        self.create_page(widgets_scale)

    def create_page(self, widgets_scale):
        stackPage = YYHWidget(widgets_scale)
        Loader.attrAttach(stackPage)
        self.stackedWidget.addWidget(stackPage)



class YYHWidget(QWidget):
    def __init__(self, widgets_scale, parent=None):
        super(YYHWidget, self).__init__(parent)
        self.root_parent = parent
        self.widgets_scale = widgets_scale
        Loader.attrAttach(self)
        self.setObjectName("YYHWidget")
        self.initLayout()

    def initLayout(self, ):
        self.showWidget = YTableWidget(self)
        self.showWidget.tableWidget.installEventFilter(self.root_parent)

        task_list = [
            {"name": "Ontology Path", "type": QLineEdit, "handle": lambda x: print(x), "width": 200, "ObjectName": "TaskLineEdit", "args": 1},
            {"name": "Append Path", "type": QLineEdit, "handle": lambda x: print(x), "width": 200, "ObjectName": "TaskLineEdit", "args": 1},
            {"name": "Salt", "type": QLineEdit, "handle": lambda x: print(x), "width": 100, "ObjectName": "TaskLineEdit", "args": 1},
            {"name": "GO", "type": QPushButton, "handle": self.showWidget.update_data, "width": 100, "ObjectName": "TaskPushButton", "args": -1},
            {"name": "...", "type": QLabel, "handle": lambda x: print(x), "width": 200, "ObjectName": "tipWidget", "args": 0},
        ]
        self.buttonList = TaskWidget(task_list, self)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        # 对按钮进行尺寸修正
        self.showWidget.setGeometry(0, 0, width, int(height * 0.92))
        self.buttonList.setGeometry(0, int(height * 0.92), self.buttonList.width_calc, int(height * 0.08))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = BrowserWidget()
    demo.show()
    sys.exit(app.exec_())
