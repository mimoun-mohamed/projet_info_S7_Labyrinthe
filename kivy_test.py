from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import math


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
    # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)
    # let's add a Widget to this layout
    #     for k in range(3):
            # self.add_widget(
            #     Button(
            #         text="Hello World",
            #         size_hint=(.5, .5),
            #         pos_hint={'center_x': .5*k, 'center_y': .5*k}))

class MainApp(App):
    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        taille = min(root.size[0], root.size[1])
        position = min(root.pos[0], root.size[1])
        for k in range(2):
            # self.root.add_widget(Color(0, 0, 0, 1))
            self.root.add_widget(Rectangle(size=(taille/10, taille/10), pos=(math.floor(position*3*k/10), math.floor(position*3*k/10))))
        with root.canvas.before:
            Color(1, 0, 0, 0.5) # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
            taille = min(root.size[0], root.size[1])
            position = min(root.pos[0], root.size[1])
            # Color(0, 0, 0, 1)
            # for k in range(2):
            #     Rectangle(size=(taille/10, taille/10), pos=(math.floor(position*3*k/10), math.floor(position*3*k/10)))
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    # MyPaintApp().run()
    MainApp().run()