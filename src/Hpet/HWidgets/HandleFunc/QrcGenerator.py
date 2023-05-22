"""
import ProcessManager
"""
import os
import re
import importlib
ProcessManager = importlib.import_module('ProcessManager')
ProcessManage = ProcessManager.ProcessManage
# from ProcessManager import ProcessManage
# ProcessManagerModule = __import__("HWidgets.HandleFunc.ProcessManager", fromlist=['ProcessManage'])
# ProcessManagerModule = __import__("ProcessManager", fromlist=['ProcessManage'])

# from HWidgets.HandleFunc.ProcessManager import ProcessManage


def generate_py(qrc_file, script_file, out_file):
    pm = ProcessManage()  # type:  ProcessManager.ProcessManage
    # pm.run_command(" ".join([script_file, qrc_file, "-o", out_file]))


if __name__ == '__main__':
    script_path = r"D:\SOFTSPACE\Anaconda3\pkgs\pyqt-5.9.2-py39hd77b12b_6\Library\bin\pyrcc5.bat"
    aim_dir_path = r"D:\Donnie\Notes\AntDev\src\Qpet\test\test002"
    qrc_path = aim_dir_path + os.sep + "test.qrc"
    out_path = aim_dir_path + os.sep + "test_qrc.py"
    generate_py(qrc_path, script_path, out_path)
