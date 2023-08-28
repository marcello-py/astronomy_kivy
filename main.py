from kivymd.app import MDApp
from kivy.core.window import Window

class Test(MDApp):
    pass

if __name__ == '__main__':
    Window.size = (600, 1000)
    Test().run()