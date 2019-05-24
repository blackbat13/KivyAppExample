from kivy.app import App
from kivymd.theming import ThemeManager
import login_screen
import rv_screen


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Blue'

    def login_button_pressed(self):
        self.root.current = 'login_screen'


if __name__ == '__main__':
    MainApp().run()
