"""It takes care of the scroll area with slides."""

# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QApplication


class HScrollArea(QScrollArea):
    """ScrollArea is a personalized scroll area."""

    initial_pos = QPoint()
    pressed = False

    def __init__(self, parent=None):
        """Init UI."""

        super(HScrollArea, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        """Init all ui object requirements."""

        self.setFixedWidth(200)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("""

            QScrollArea{
                background-color:transparent;
                border-top-right-radius: 4px;
                border-top-left-radius: 4px;
                border-bottom-right-radius: 4px;
                border-bottom-left-radius: 4px;
                border: 0px solid ;
                border-color: rgb(0,0,0,100)
            }

            QScrollBar:vertical{
                border:1px solid;
                border-color: rgb(197,197,199,100);
                width: 7px;
                margin: 0px 0px 0px 0px;
                background: rgb(234,234,234,100);


            }

            QScrollBar::handle:vertical  {
                background: rgba(14,65,148,100);
            }

            QScrollBar::add-line:vertical{
                height: 0px;
            }

            QScrollBar::sub-line:vertical{
                height: 0px;
            }

        """)

        self.setWidgetResizable(True)

    def mousePressEvent(self, event):
        """Update initial click location of scroll area."""

        self.pressed = True
        self.initial_pos = self.verticalScrollBar().value() + event.pos().y()

    def mouseReleaseEvent(self, event):
        """Update next location to be used in scroll area location."""

        self.pressed = False
        self.initial_pos = self.verticalScrollBar().value()

    def mouseMoveEvent(self, event):
        """Update value location of scroll area according to init location."""
        print("w")
        if self.pressed:
            self.verticalScrollBar().setValue(
                 self.initial_pos - event.pos().y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = HScrollArea()
    frame.show()
    sys.exit(app.exec())
