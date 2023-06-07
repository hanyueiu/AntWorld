import os

from PyQt5.QtCore import Qt


class StyleLoader(object):
    FramelessWindowHint = Qt.FramelessWindowHint
    TranslucentBackground = Qt.WA_TranslucentBackground

    def __init__(self, stylesheet="./frame_qss.py", new_style: dict = None):
        self.new_style = new_style
        self.stylesheet = os.path.abspath(stylesheet)

