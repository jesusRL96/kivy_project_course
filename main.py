from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('Init ',self.width, self.height)
    
    def on_parent(self, widget, parent):
        print('Parent ',self.width, self.height)

    def on_size(self, *args):
        print('Size ',self.width, self.height)
        self.perspective_point_x = self.width / 2
        self.perspective_point_y = self.height * 0.75
    
    def on_perspective_point_x(self, widget, value):
        print('PX ',value)
    
    def on_perspective_point_y(self, widget, value):
        print('PY ',value)


class GalaxyApp(App):
    pass

GalaxyApp().run()