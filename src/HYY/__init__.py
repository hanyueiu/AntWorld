from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import QObject, QEvent, qDebug
from PyQt5 import QtGui

import sys


class MyFilterA(QObject):
    '''
    该类的对象用作过滤器对象，使用事件过滤器需要继承自QObject
    '''

    def eventFilter(self, obj: 'QObject', event: 'QEvent') -> bool:
        if event.type() == QEvent.Type.MouseButtonPress:
            print(f'{self.objectName()} : MyFilterA: mouse press')
            # 返回true表示该事件不再进一步处理
            return True
        # 返回false，表示其余事件交还给目标对象处理，本例应返回false
        return False


class MyFilterB(QObject):
    '''
    该类的对象用作过滤器对象，使用事件过滤器需要继承自QObject
    '''

    def eventFilter(self, obj: 'QObject', event: 'QEvent') -> bool:
        if event.type() == QEvent.Type.MouseButtonPress:
            qDebug(f'{self.objectName()} : MyFilterB: mouse press')
        return False


class MyWidget(QWidget):
    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        qDebug('MyWidget: mouse press')


class MyPushButton(QPushButton):
    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        qDebug('MyPushButton: mouse press')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_filter_a = MyFilterA()
    my_filter_b = MyFilterB(my_filter_a)
    my_widget = MyWidget()
    my_btn_1 = MyPushButton('AAA', my_widget)
    my_btn_2 = MyPushButton('BBB', my_widget)

    # 设置对象名
    my_filter_a.setObjectName('my_filter_a')
    my_filter_b.setObjectName('my_filter_b')
    my_widget.setObjectName('my_widget')
    my_btn_1.setObjectName('my_btn_1')
    my_btn_2.setObjectName('my_btn_2')

    # 注册过滤器对象
    my_btn_1.installEventFilter(my_filter_a)
    my_btn_2.installEventFilter(my_filter_b)

    my_widget_layout = QHBoxLayout()
    my_widget_layout.addWidget(my_btn_1)
    my_widget_layout.addWidget(my_btn_2)
    my_widget.setLayout(my_widget_layout)

    my_widget.show()
    sys.exit(app.exec_())
