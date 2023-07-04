# STEP-1 CREATE A APP
# STEP-1 CREATE Game
# STEP-1 Build the Game
# STEP-1 Run The app


from kivy.app import App
from kivy.uix.widget import Widget

class Working(Widget):
    pass

class StockSnap(App):
    def build(self):
        return Working()

StockSnap().run()
print("Running")

