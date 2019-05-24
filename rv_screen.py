from kivy.uix.screenmanager import Screen
from random import sample
from string import ascii_lowercase

class RvScreen(Screen):

    def populate_button_pressed(self):
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]

    def login_button_pressed(self):
        username = self.username_text_input.text
        password = self.password_text_input.text
        print(username, password)

    def back_button_pressed(self):
        self.manager.current = 'main_screen'
