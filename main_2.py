from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty,ListProperty
from kivy.core.window import Window
from random import randint
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.clock import Clock


class KatsuraGame(Widget):

    player1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(KatsuraGame, self).__init__(**kwargs)
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
        self.liste_enlises = []
        self.player1.lives = 3
        self.player1.score = 0

        self.difficulte = 3


        with self.canvas:
            self.rect = Rectangle(pos=(self.center_x * 1.5, 0), size=(10, self.height))
            self.label1 = Label(font_size=20, center=(self.center_x * 1.75, self.center_y * 1.8),
                                text = 'Score :' )
            self.label2 = Label(font_size=20, center=(self.center_x * 1.75, self.center_y * 1.7),
                                text=str(self.player1.score))
            self.label3 = Label(font_size=20, center=(self.center_x * 1.75, self.center_y * 1),
                                text='Vies :')
            self.label4 = Label(font_size=20, center=(self.center_x * 1.75, self.center_y * 0.9),
                                text=str(self.player1.lives))
            self.player_rect = Rectangle(pos = (self.center_x * 0.75, self.center_y * 0.25), size=(15, 15))


    def update(self, dt):

        self.rect.pos = (self.center_x * 1.5, 0)
        self.rect.size = (10, self.height)

        self.label1.center = (self.center_x * 1.75, self.center_y * 1.8)
        self.label2.center = (self.center_x * 1.75, self.center_y * 1.7)
        self.label3.center = (self.center_x * 1.75, self.center_y * 1)
        self.label4.center = (self.center_x * 1.75, self.center_y * 0.9)

        self.label1.text = 'Score :'
        self.label2.text = str(self.player1.score)
        self.label3.text = 'Vies :'
        self.label4.text = str(self.player1.lives)

        self.player_rect.pos = (self.player1.center_x, self.player1.center_y)

        if randint(1,100) < 5:
            self.difficulte += 1
        if randint(1,1000) < self.difficulte:
            self.enlise_x = self.pop_enlise()

        self.move()
        self.remove_enlise()
        self.contact()

        if self.player1.lives == 0:
            self.defaite()

        for key in self.pressed_keys:
            try:
                self.pressed_actions[key]()
            except KeyError:
                return None

    def pop_enlise(self):

        x = randint(0, 100)


        self.enlise = Enlise()

        if x <= 80:
            self.enlise.categorie = 0
            self.enlise.color = [1, 0, 0]
        elif x > 80:
            self.enlise.categorie = 1
            self.enlise.color = [0,1,0]


        self.enlise.center_x = randint(30, int(self.center_x * 1.35))
        self.enlise.center_y = self.center_y * 2
        self.add_widget(self.enlise)
        self.liste_enlises.append(self.enlise)


    def remove_enlise(self):
        for enlise in self.liste_enlises:
            if enlise.center_y < self.center_y * 0.1:
                self.remove_widget(enlise)
                self.liste_enlises.remove(enlise)

    def defaite(self):
        self.player1.score = 0
        self.player1.lives = 3
        self.difficulte = 1
        self.player1.center_x = self.center_x * 0.75
        self.player1.center_y = self.center_y * 0.25

        for enlise in self.liste_enlises:
            self.remove_widget(enlise)
        self.liste_enlises = []


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

    def contact(self):
        for enlise in self.liste_enlises:
            if self.player1.collide_widget(enlise):

                if enlise.categorie == 0:
                    self.player1.lives -= 1
                elif enlise.categorie == 1:
                    self.player1.score += 1

                self.remove_widget(enlise)
                self.liste_enlises.remove(enlise)



    def move(self):
        for enlise in self.liste_enlises:
            enlise.move()



class Player(Widget):
    lives = NumericProperty(0)
    score = NumericProperty(0)



class Enlise(Widget):

    color = ListProperty([1, 1, 1])
    categorie = NumericProperty(0)


    def move(self):
        self.center_y = self.center_y - 3



class KatsuraApp(App):
    def build(self):
        game = KatsuraGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)

        return game


if __name__ == '__main__':
    KatsuraApp().run()
