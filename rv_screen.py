from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from random import sample
from string import ascii_lowercase


class RvScreen(Screen):

    def on_enter(self, *args):
        self.populate()

    def populate(self):
        data = []
        for x in range(50):
            obj = {
                'value': ''.join(sample(ascii_lowercase, 6)),
                'row_id': x,
                'rv_screen': self
            }
            data.append(obj)

        self.rv.data = data

    def delete(self, row_id):
        index = 0
        for row in self.rv.data:
            if row['row_id'] == row_id:
                self.rv.data.pop(index)
                break
            index += 1


class Row(BoxLayout):

    def first_button_pressed(self):
        print(self.row_id, self.value)

    def delete_button_pressed(self):
        self.rv_screen.delete(self.row_id)
