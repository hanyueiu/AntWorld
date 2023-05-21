import os
import sys


def append_path(cur_path=os.path.abspath(__file__), root_name="QPet"):
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


append_path()

