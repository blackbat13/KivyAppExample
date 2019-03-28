from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):

    def login_button_pressed(self):
        username = self.username_text_input.text
        password = self.password_text_input.text
        print(username, password)

    def back_button_pressed(self):
        self.manager.current = 'main_screen'
