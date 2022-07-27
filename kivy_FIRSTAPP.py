

from kivy.app import App # gui interface creator

from kivy.uix.button import Label # button label import statement

class Sample(App):

   # display content on screen

   def build(self):
        return Label(text="this is my first app")
    


if __name__=="__main__":
	sample = Sample()
	sample.run()