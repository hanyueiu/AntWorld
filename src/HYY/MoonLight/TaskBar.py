from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit
from AppStyle.StyleLoader import Loader
from AppStyle.StyleQss import StyleQss


class TaskWidget(QWidget):

    def __init__(self, parent=None):
        super(TaskWidget, self).__init__(parent)
        self.setTaskPushButton("Debug")
        self.setStyleSheet(StyleQss.get_qss())
        Loader.attrAttach(self)

    def setTaskPushButton(self, nav_bar: (list, tuple)):
        task_list = [
            {"name": "Task_1", "type": QPushButton, "handle": lambda x: print(x), "width": None, "height": None},
            {"name": "Task_2", "type": QPushButton, "handle": lambda x: print(x), "width": None, "height": None},
            {"name": "Task_3", "type": QLineEdit, "handle": lambda x: print(x), "width": 30, "height": None},
            {"name": "Task_4", "type": QPushButton, "handle": lambda x: print(x), "width": None, "height": None},
        ]
        self.layout_bar = QHBoxLayout()
        for index, task_dict in enumerate(task_list):
            info_func = lambda x: print(x)
            print(index, task_dict)
            task_type = task_dict.get("type", None)
            print(task_type)
            task_name = task_dict.get("name", '')
            if index:
                font_task_type = task_list[index - 1].get("type", None)
            else:
                font_task_type = []
            if not task_type:
                continue
            if task_type is QPushButton:
                button = QPushButton(str(task_name),  self)
                button.setObjectName("TaskPushButton")
                button.setCheckable(True)
                if isinstance(font_task_type, QLineEdit):
                    task_handle = task_list[index].get("handle", lambda x: print(x))
                else:
                    task_handle = task_dict.get("handle", lambda x: print(x))
                # button.clicked.connect(task_handle)
                self.layout_bar.addWidget(button)
            elif task_type is QLineEdit:
                line_edit = QLineEdit(self)
                line_edit.setPlaceholderText(str(task_name))
                line_edit.setObjectName("TaskLineEdit")
                if isinstance(font_task_type, QLineEdit):
                    task_handle = task_list[index].get("handle", lambda x: print(x))
                else:
                    task_handle = task_dict.get("handle", lambda x: print(x))
                line_edit_width = task_dict.get("width", None)
                if line_edit_width:
                    line_edit.setMaximumWidth(line_edit_width)
                print(task_handle)
                self.layout_bar.addWidget(line_edit)
            else:
                print("No Support")

        Loader.spaceAttach(self.layout_bar)
        Loader.boundAttach(self.layout_bar)

        self.setLayout(self.layout_bar)

    def handle_secret(self, e):
        text = self.sender().text()
        print(text)

    def handle_file(self, e):
        text = self.sender().text()
        print(text)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        # 对按钮进行尺寸修正
        for item_index in range(self.layout_bar.count()):
            widget = self.layout_bar.itemAt(item_index).widget()
            if isinstance(widget, QPushButton):
                self.layout_bar.itemAt(item_index).widget().setFixedSize(100, height)
            elif isinstance(widget, QLineEdit):
                self.layout_bar.itemAt(item_index).widget().setFixedSize(200, height)
            else:
                print(item_index)


if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
    from PyQt5.QtWidgets import QWidget, QApplication
    app = QApplication(sys.argv)
    frame = TaskWidget(None)
    frame.show()
    sys.exit(app.exec())