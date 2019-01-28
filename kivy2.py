from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty,ListProperty
from kivy.core.window import Window
from random import randint
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.clock import Clock

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.pressed_keys = set()

        self.pressed_actions = {
            'up': lambda: self.player_move('up'),
            'down': lambda: self.player_move('down'),
            'left': lambda: self.player_move('left'),
            'right': lambda: self.player_move('right')
        }
        # self.add_widget(Rectangle(pos=self.pos, size=self.size))
        # with self.canvas:
            # self.rect = Rectangle(pos=self.pos, size=self.size)
            # self.bind(pos=self.update_rect)
            # self.bind(size=self.update_rect)
    # def update_rect(self, *args):
    #     self.rect.pos = self.pos
    #     self.rect.size = self.size
        with self.canvas:
            # Add a red color
            Color(1., 0, 0)

            # Add a rectangle
            Rectangle(pos=(10, 10), size=(500, 500))

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None



    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(keycode[1])

    def _on_keyboard_up(self, keyboard, keycode):
        self.pressed_keys.remove(keycode[1])

    def player_move(self, touche):
        if touche == 'left':
            if self.player1.center_x >= self.center_x * 0.1:
                self.player1.center_x -= 4
        elif touche == 'right':
            if self.player1.center_x <= self.center_x * 1.4:
                self.player1.center_x += 4
        elif touche == 'up':
            if self.player1.center_y <= self.center_y * 1.9:
                self.player1.center_y += 4
        elif touche == 'down':
            if self.player1.center_y >= self.center_y * 0.1:
                self.player1.center_y -= 4
        return True

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
