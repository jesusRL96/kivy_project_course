from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 7
    V_LINES_SPACING = (1-0.1)/V_NB_LINES # percentage in screen width
    vertical_lines = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_vertical_lines()
    
    def on_parent(self, widget, parent):
        print('Parent ',self.width, self.height)

    def on_size(self, *args):
        print('Size ',self.width, self.height)
        self.perspective_point_x = self.width / 2
        self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()
    
    def on_perspective_point_x(self, widget, value):
        print('PX ',value)
    
    def on_perspective_point_y(self, widget, value):
        print('PY ',value)
    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[self.perspective_point_x, 0, self.perspective_point_x, self.height])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
            central_line_x = self.width / 2
            offset = -int(self.V_NB_LINES/2)
            spacing = self.width * self.V_LINES_SPACING
            # self.line.points = [self.perspective_point_x, 0, self.perspective_point_x, self.perspective_point_y]
            for line in self.vertical_lines:
                line_x = int(central_line_x + offset*spacing)
                line.points = [line_x, 0, line_x, self.height]
                offset += 1



class GalaxyApp(App):
    pass

GalaxyApp().run()