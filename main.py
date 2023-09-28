from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder

class Test(MDApp):
    def build_app(self):
        return Builder.load_file('app/Test.kv')

if __name__ == '__main__':
    Window.size = (600, 1000)
    Test().run()