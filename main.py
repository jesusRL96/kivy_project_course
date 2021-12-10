from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 6
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
            offset = -int(self.V_NB_LINES/2) + 0.5
            spacing = self.width * self.V_LINES_SPACING
            # self.line.points = [self.perspective_point_x, 0, self.perspective_point_x, self.perspective_point_y]
            for line in self.vertical_lines:
                line_x = int(central_line_x + offset*spacing)
                x1, y1 = self.transform(line_x, 0)
                x2, y2 = self.transform(line_x, self.height)
                line.points = [x1, y1, x2, y2]
                offset += 1

    def transform(self, x, y):
        # return self.transform_2D(x,y)
        return self.transform_perspective(x,y)
    
    def transform_2D(self, x, y):
        return int(x), int(y)
    
    def transform_perspective(self, x, y):
        tr_y = y * self.perspective_point_y / self.height
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        proportion_y = diff_y / self.perspective_point_y # 1 when diff_y == perspective_y 
        tr_x = self.perspective_point_x + diff_x*proportion_y

        return int(tr_x), int(tr_y)


class GalaxyApp(App):
    pass

GalaxyApp().run()