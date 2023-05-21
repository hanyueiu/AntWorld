import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect, QLine, QSize, QObject
from PyQt5.QtGui import QCursor, QPaintEvent, QColor, QPen, QPainter, QBrush, QFont, QGradient, QLinearGradient, \
    QPixmap, QIcon, QImage, qRgba
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QSplitter, QVBoxLayout, QPushButton, QTextEdit, \
    QStyleOption, QStyle, QProgressBar
from PIL import Image, ImageDraw
from HWidgets.Components.MoveComponent import DragWindow
from qss import Qss
import test_qrc
from PIL import Image, ImageQt


class TMainFrame(QWidget):
    # YYH 自定义进度条，基于PIL(pillow)图像处理的颜色替换，使用paintEvent在透明度为0的像素点忽略绘画窗口来创建进度条控件
    def __init__(self, parent):
        super(TMainFrame, self).__init__(parent)
        # YYH 将图片以源码形式保存，展示于窗口， 任务栏
        self.img_001 = ':/images/img002.png'
        # self.setObjectName("mainframe")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(self.img_001))
        print(self.testAttribute(Qt.WA_TranslucentBackground))
        self.setStyleSheet(Qss)
        self.under_color = (0, 0, 0, 0)
        self.image_fill = ImageQt.fromqimage(QImage(":/images/img003.png"))
        self.progress_val = 0

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

        # painter = QPainter(self)
        pixmap = QPixmap.fromImage(QImage(self.img_001))
        qimage = QPixmap.toImage(pixmap)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = self.img_to_pil(pixmap, self.progress_val)
        self.setFixedSize(pixmap.size())
        painter.drawPixmap(self.rect(), pixmap)

    # def paintEvent(self, a0: QPaintEvent) -> None:
    #     opt = QStyleOption()
    #     opt.initFrom(self)
    #     painter = QPainter(self)
    #     self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

    def img_to_pil(self, png_obj: QImage, value):
        import io
        from PIL import Image, ImageQt
        from PyQt5.QtGui import QImage
        from PyQt5.QtCore import QBuffer

        # # png_obj = QImage("image.png")
        # buffer = QBuffer()
        # buffer.open(QBuffer.ReadWrite)
        # png_obj.save(buffer, "PNG")
        # image = Image.open(io.BytesIO(buffer.data()))
        # buffer.close()
        # # pil_im.show()

        # 在ImageQt中的转换qpixmap与qimage相同
        image = ImageQt.fromqimage(png_obj)
        # image = ImageQt.fromqpixmap(png_obj)

        x, y = image.size
        x_ = int(x * value / 100)
        light = 255 - int(130 * value / 100)
        for i in range(x):
            if i > x_:
                break
            for k in range(y):
                # YYH PIL对图片颜色的获取与修改
                color_bg = image.getpixel((i, k))
                if len(color_bg) == 3 or color_bg == self.under_color or len(color_bg) == 4 and color_bg[-1] == 0:
                    continue
                else:
                    try:

                        color_fill = self.image_fill.getpixel((i, k))
                        if color_bg[-1] == 255 and color_fill[-1] == 0:
                            color_fill = (light, light, light, 255)
                    except:
                        color_fill = (light, light, light, 0)

                # YYH 使用PIL对图片颜色的获取与修改
                image.putpixel((i, k), color_fill)

        qpixmap = ImageQt.toqpixmap(image)
        return qpixmap

    def setValue(self, val):
        self.progress_val = val


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = TMainFrame(None)
    frame.show()
    sys.exit(app.exec())
