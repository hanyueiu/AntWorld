"""YYHKey 图片对象之间的相互转换"""
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image

# Support for PyQt5 is deprecated and will be removed in Pillow 10
from PIL import ImageQt

import io
from PIL import Image, ImageQt
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QBuffer


def img_to_pil_img(qt_obj: (QImage, QPixmap)):
    image = ImageQt.fromqimage(qt_obj)
    image = ImageQt.fromqpixmap(qt_obj)

    # Image转换成QImage,QPixmap具有相似的调用
    qimage = ImageQt.toqimage(image)
    # QPixmap转换成QImage
    qpixmap = ImageQt.toqpixmap(image)


def qimage_to_img_by_buffer(qt_obj: QImage):
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    qt_obj.save(buffer, "PNG")
    image = Image.open(io.BytesIO(buffer.data()))
    buffer.close()
    image.show()


qimage_to_img_by_buffer(QImage("img003.png"))