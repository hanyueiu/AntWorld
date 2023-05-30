import os

from PyQt5 import QtGui
from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit, QLabel

from AppAlg.Solve import Solve
from AppStyle.StyleLoader import Loader
from AppStyle.StyleQss import StyleQss
from Dandelion.LineEdit import LineEdit


class TaskWidget(QWidget):
    dataSignal = pyqtSignal(object)

    def __init__(self, task_list, parent=None):
        super(TaskWidget, self).__init__(parent)

        self.width_calc = 200
        self.pro_yyh = "YYH_"
        self.task_list = task_list
        self.setTaskPushButton(self.task_list)
        self.setStyleSheet(StyleQss.get_qss())
        Loader.attrAttach(self)

    def setTaskPushButton(self, task_list):
        self.layout_bar = QHBoxLayout()
        for index, task_dict in enumerate(task_list):
            task_type = task_dict.get("type", None)
            task_name = task_dict.get("name", '')
            item_width = task_dict.get("width", 200)
            object_name = task_dict.get("ObjectName")
            self.width_calc = self.width_calc + item_width
            if not task_type:
                continue
            if task_type is QPushButton:
                item = QPushButton(str(task_name),  self)
                item.setCheckable(True)
                item.clicked.connect(self.task_handle_button)
            elif task_type is QLineEdit:
                item = LineEdit(self)
                item.setPlaceholderText(str(task_name))
            elif task_type is QLabel:
                item = QLabel(self)
                item.setText(str(task_name))
            else:
                continue
            self.layout_bar.addWidget(item)
            item.setObjectName(object_name)

        Loader.spaceAttach(self.layout_bar)
        Loader.boundAttach(self.layout_bar)

        self.setLayout(self.layout_bar)

    def handle_data(self, args):
        salts = args[2]
        mid = int(len(salts) / 2)
        salt = salts[:mid]
        print(salt)
        if len(salts) % 2 == 1 or salts[:mid] != salts[mid:] or len(salt) > 16:
            self.task_handle_label("Salt is mistake")
            return
        if args[1].startswith("sql:"):
            print()

        if not os.path.exists(args[0]) and not os.path.exists(args[1]):
            self.task_handle_label("Please input file path.")
        sl = Solve()
        second_encode_data = None
        if os.path.exists(args[1]):
            second_path = os.path.abspath(args[1])
            rl = sl.check_file(second_path)
            if not rl:
                second_encode_data = sl.file_to_encode(sl.get_file_data(second_path), salt)
            else:
                second_encode_data = sl.get_file_data(second_path)
            rl_salt = sl.check_data_salt(second_encode_data, salt)
            if rl_salt:
                self.task_handle_label("Second Path 数据已获取")
            else:
                self.task_handle_label("Second path salt not match")
                return None
        if os.path.exists(args[0]):
            first_path = os.path.abspath(args[0])
            if os.path.exists(first_path):
                rl = sl.check_file(first_path)
                if not rl:
                    first_encode_data = sl.file_to_encode(sl.get_file_data(first_path), salt)
                else:
                    first_encode_data = sl.get_file_data(first_path)
                rl_salt = sl.check_data_salt(first_encode_data, salt)
                if rl_salt:
                    self.task_handle_label("First数据已获取")
                else:
                    self.task_handle_label("First path salt not match")
                    return None
                first_encode_data = sl.map_data([first_encode_data, second_encode_data]) if second_encode_data else first_encode_data
                dir_name, base_name = os.path.dirname(first_path), os.path.basename(first_path)
                rl_salt = sl.check_data_salt(first_encode_data, salt)
                if rl_salt:
                    if base_name.startswith(self.pro_yyh):
                        to_path = first_path
                    else:
                        to_path = os.path.join(dir_name, "YYH_" + base_name)
                    sl.set_file_data(to_path, first_encode_data, mode="w")
                    return sl.file_to_decode(first_encode_data, salt)
                else:
                    self.task_handle_label("Salt not match")
        else:
            if second_encode_data:
                second_path = os.path.abspath(args[1])
                dir_name, base_name = os.path.dirname(second_path), os.path.basename(second_path)
                if base_name.startswith(self.pro_yyh):
                    to_path = second_path
                else:
                    to_path = os.path.join(dir_name, "YYH_" + base_name)
                sl.set_file_data(to_path, str(second_encode_data))
                return sl.file_to_decode(second_encode_data, salt)

    def task_handle_label(self, text):
        for item_index in range(self.layout_bar.count()):
            widget = self.layout_bar.itemAt(item_index).widget()
            item_args = self.task_list[item_index]["args"]
            if item_args == 0:
                widget.setText(text)
                break

    def task_handle_button(self, e):
        args = []
        bt_index = None
        for item_index in range(self.layout_bar.count()):
            widget = self.layout_bar.itemAt(item_index).widget()
            item_args = self.task_list[item_index]["args"]
            text = widget.text()

            if item_args and item_args != -1:
                args.append(text)
            elif item_args == -1:
                bt_index = item_index
                widget.setEnabled(False)
                self.task_handle_label("进行中...")
            else:
                continue
        func = self.task_list[bt_index]["handle"]
        button = self.layout_bar.itemAt(bt_index).widget()
        data = None
        try:
            data = self.handle_data(args)
        except Exception as err:
            self.task_handle_label("处理失败")
        finally:
            button.setEnabled(True)

        if data is None:
            return
        self.dataSignal[object].connect(func)
        self.dataSignal[object].emit(data)
        self.dataSignal[object].disconnect(func)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        # 对按钮进行尺寸修正
        for item_index in range(self.layout_bar.count()):
            widget = self.layout_bar.itemAt(item_index).widget()
            item_width = self.task_list[item_index].get("width", None)
            if item_width:
                widget.setFixedSize(item_width, height)


if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
    from PyQt5.QtWidgets import QWidget, QApplication
    app = QApplication(sys.argv)
    frame = TaskWidget(None)
    frame.show()
    sys.exit(app.exec())