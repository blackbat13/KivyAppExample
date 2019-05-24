from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from random import sample
from string import ascii_lowercase


class RvScreen(Screen):

    def populate(self):
        data = []
        for x in range(50):
            obj = {}
            obj['value'] = ''.join(sample(ascii_lowercase, 6))
            obj['id'] = str(x)
            data.append(obj)

        self.rv.data = data

    def login_button_pressed(self):
        username = self.username_text_input.text
        password = self.password_text_input.text
        print(username, password)

    def back_button_pressed(self):
        self.manager.current = 'main_screen'

    def on_enter(self, *args):
        self.populate()


class Row(BoxLayout):
    def first_button_pressed(self):
        print(self.id, self.value)

    def second_button_pressed(self):
        print(self.id, self.value)
