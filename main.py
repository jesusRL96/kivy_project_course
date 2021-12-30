from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import Clock

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_SPACING = 0.25 # percentage in screen width
    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_SPACING = 0.1 # percentage in screen width
    horizontal_lines = []
    current_offset_y = 0
    SPEED = 4

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()
        Clock.schedule_interval(self.update, 1/60)

    def on_parent(self, widget, parent):
        print('Parent ',self.width, self.height)

    def on_size(self, *args):
        # print('Size ',self.width, self.height)
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * 0.75
        # self.update_vertical_lines()
        # self.update_horizontal_lines()
        pass

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

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[self.perspective_point_x, 0, self.perspective_point_x, self.height])
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.width * self.V_LINES_SPACING
        offset = -int(self.V_NB_LINES/2) + 0.5

        x_min = central_line_x + offset*spacing
        x_max = central_line_x - offset*spacing
        spacing_y = self.H_LINES_SPACING*self.height
        for i, line in enumerate(self.horizontal_lines):
            line_y = i*spacing_y-self.current_offset_y
            x1, y1 = self.transform(x_min, line_y)
            x2, y2 = self.transform(x_max, line_y)
            line.points = [x1, y1, x2, y2]

    def transform(self, x, y):
        # return self.transform_2D(x,y)
        return self.transform_perspective(x,y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        lin_y = y * self.perspective_point_y / self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - lin_y
        factor_y = diff_y / self.perspective_point_y if self.perspective_point_y else 0 # 1 when diff_y == perspective_y
        factor_y = pow(factor_y, 4)
        tr_x = self.perspective_point_x + diff_x*factor_y
        tr_y = self.perspective_point_y - factor_y * self.perspective_point_y
        return int(tr_x), int(tr_y)

    def update(self, dt):
        self.perspective_point_x = self.width / 2
        self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y += self.SPEED
        spacing_y = self.H_LINES_SPACING*self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y


class GalaxyApp(App):
    pass

GalaxyApp().run()
