import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout



class Guess_THE_NUMBER_Grid(GridLayout):
    def __init__(self, **kwargs):
        self.rows=2
        super(Guess_THE_NUMBER_Grid, self).__init__()
        self.add_widget(Label(text="Student Name:"))
        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)


class Guess_THE_NUMBER(App):
    def build(self):
        return Guess_THE_NUMBER_Grid()


if __name__ == "__main__":
    Guess_THE_NUMBER().run()
