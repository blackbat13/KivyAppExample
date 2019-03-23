from kivy.app import App
import login_screen


class MainApp(App):
    def login_button_pressed(self):
        self.root.current = 'login_screen'


if __name__ == '__main__':
    MainApp().run()
