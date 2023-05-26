"""
QWidget#MainFrame{
    background-color:rgba(255,255,255,255);
}
QWidget#title_widget {
    background: rgba(223,223,223,255);
}

QLabel#title_text {
    padding:0px;
    margin:0px;
    color:rgba(63,63,63,255);
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
    font-family:Microsoft YaHei;
}

QScrollArea#nav_bar{
    border-radius: 0px;
    border: 0px solid ;
    border-color: rgba(255,255,255,255);
    background-color:rgba%(nav_color)s;
}

QPushButton#NavPushButton{
    background-color: rgba%(nav_color)s;
    border-radius:0px;
    padding:0px;
    margin:0px;
    border:%(nav_border)spx solid rgba(150,120,100, %(transparent)s);
    color:rgba%(nav_font_color)s;
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
    font-family:Microsoft YaHei;
}
QPushButton#NavPushButton:hover {
    background: rgba(240, 255, 250, %(transparent)s);
    color:rgba%(nav_font_color)s;
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
    font-family:Microsoft YaHei;
}
QPushButton#NavPushButton:pressed {
    background: rgba(255, 255, 255, %(transparent)s);
    color:rgba%(nav_font_color)s;
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
}
QPushButton#NavPushButton:focus {
    background: rgba(255, 255, 255, %(transparent)s);
    color:rgba%(nav_font_color)s;
    font-size:%(nav_font)spx;
    font-weight: %(font_bold)s;
    font-family:Microsoft YaHei;

}

QPushButton#minimize_btn {
    border-image: url(:/images/minimize.png) no-repeat 0px 0px;
}
QPushButton#close_btn {
    border-image: url(:/images/close.png) no-repeat 0px 0px;
}

"""
from PyQt5.QtGui import QFont

nav_font = 18

white = (255, 255, 255)
font_normal = 400  # 正常字体
font_bold = 700  # 加粗字体
moon_light_color = (255, 255, 204, 200)
nav_color = (230, 248, 239, 255)
nav_font_color = (250, 200, 200, 255)
transparent = 255
nav_border = 0

QSS = __doc__ % {
    "nav_color": nav_color,
    "nav_border": nav_border,
    "nav_font_color": nav_font_color,
    "transparent": transparent,
    "font_normal": font_normal,
    "moon_light_color": moon_light_color,
    "font_bold": font_bold,
    "nav_font": nav_font,
}

"""
QLabel#LogoLabel{
    background:QLinearGradient(
        spread:pad,
        x1:0,
        y1:1,
        x2:0,
        y2:0,
        stop:0 rgba(200, 200, 200, %(transparent)s),
        stop:0.5 rgba(150, 150, 200,%(transparent)s),
        stop:1 rgba(150, 200, 200, %(transparent)s)
    );
    border-radius:0px;color:white;
    border:%(nav_border)spx solid rgba(66, 66, 66, %(transparent)s);"""


class StyleQss(object):
    @staticmethod
    def get_qss(nav_color=nav_color,
                nav_border=nav_border,
                nav_font_color=nav_font_color,
                transparent=transparent,
                font_normal=font_normal,
                moon_light_color=moon_light_color,
                font_bold=font_bold,
                qss=__doc__
                ):

        param = {}
        param.update(nav_color=nav_color,
                     nav_border=nav_border,
                     nav_font_color=nav_font_color,
                     transparent=transparent,
                     font_normal=font_normal,
                     moon_light_color=moon_light_color,
                     font_bold=font_bold,
                     nav_font=nav_font,
                     )
        return qss % param

    white = white
    nav_color = nav_color
    moon_light_color = moon_light_color


if __name__ == '__main__':
    StyleQss().get_qss()
    f = QFont()
    f.setFamily()

