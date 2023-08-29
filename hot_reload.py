from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window

class FirstScreen(Screen):
   pass


class NewScreen(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(NewScreen(name = 'register'))
sm.add_widget(FirstScreen(name = 'login'))

class HotReload(MDApp):
    KV_FILES = ['app/Test.kv']
    DEBUG = True

    def build_app(self):
        return Builder.load_file('app/Test.kv')
    

if __name__ == '__main__':
    Window.size = (600, 1000)
    HotReload().run()