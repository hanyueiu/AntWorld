import os
Qss = """
QWidget#SecondWidget {
	background:rgba(255, 255, 0, 255);
}

"""


class StyleLoader(object):
    FONT = 'Montserrat.ttf'

    def __init__(self, stylesheet="frame_style.css", new_style: dict = None):
        self.new_style = new_style
        self.stylesheet = stylesheet

    def init_style(self):
        with open(os.path.abspath(self.stylesheet), 'r') as style_file:
            stylesheet = style_file.read()
        if self.new_style:
            stylesheet = self.update_style(stylesheet)
        return stylesheet

    def update_style(self, stylesheet):
        print(self.new_style)
        print(stylesheet)
        return stylesheet


if __name__ == '__main__':
    StyleLoader(new_style="1").init_style()
