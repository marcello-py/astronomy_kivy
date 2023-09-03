from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window

class FirstScreen(Screen):
   pass


class LoginScreen(Screen):
    pass


class Cadastro(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(LoginScreen(name = 'acess'))
sm.add_widget(FirstScreen(name = 'login'))
sm.add_widget(Cadastro(name = 'tela'))

class HotReload(MDApp):
    KV_FILES = ['app/Test.kv']
    DEBUG = True

    def build_app(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('app/Test.kv')
    

if __name__ == '__main__':
    Window.size = (600, 1000)
    HotReload().run()