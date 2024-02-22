from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window



class HotReload(MDApp):
    KV_FILES = ['app/Test.kv']
    DEBUG = True
    def build_app(self):
        return Builder.load_file('app/Test.kv')

if __name__ == '__main__':
    HotReload().run()