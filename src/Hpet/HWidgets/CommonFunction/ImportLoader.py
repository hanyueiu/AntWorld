"""
from SearchHHY import KeySearch
from SearchHHY import KeySearch
"""
import importlib
import re
import os
import sys


def to_import(string):
    # YYH 将原导入的代码以多行字符串的形式进行解析， 但在pycharm文件中调用代码会显示无法调用的红色波浪线， 且没有代码提示
    lines = string.splitlines()
    for line in lines:
        if line and line.startswith("import"):
            module_name = re.split(" +", line)[-1]
            globals().update({module_name: importlib.import_module(module_name)})
        if line and line.startswith("from"):
            module_name = re.split(" +", line)[1]
            module = importlib.import_module(module_name)
            class_name = re.split(" +", line)[-1]
            class_object = getattr(module, class_name)
            globals().update({class_name: class_object})


def append_path(cur_path=os.path.abspath(__file__), root_name="HPet"):
    # HHY 在__init__中进行调用， 可以达到导入代码不变的目的， 但在pycharm文件中导入代码会显示无法导入的红色波浪线，且没有代码提示
    cur_list = []
    dir_path = os.path.dirname(cur_path)
    dir_name = os.path.basename(dir_path)
    print(dir_name)
    if dir_path not in sys.path:
        cur_list.append(dir_path)
    if dir_name.lower() not in root_name.lower():
        append_path(dir_path)
    else:
        return


if __name__ == '__main__':
    to_import(__doc__)
