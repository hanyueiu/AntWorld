from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QApplication, QWidget
import sys
from HWidgets.secondFrame import HMainFrame


class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        layout = QHBoxLayout()
        layout.addWidget(HMainFrame())
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainFrame()
    form.show()
    sys.exit(app.exec_())