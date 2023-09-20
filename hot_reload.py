from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from database import Database


class FirstScreen(Screen):
   pass


class LoginScreen(Screen):
    pass


class Register(Screen):
    def register_user(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text


        # Criar uma instância da classe Database
        db = Database('astronomy.db')

        # Inserir o usuário no banco de dados
        db.insert_user(username, password) 

        # Fechar a conexão com o banco de dados
        db.conn.close()

        # Redirecionar para a tela de usuário criado
        self.manager.current = 'user' 

class CreatedLogin(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(LoginScreen(name = 'acess'))
sm.add_widget(FirstScreen(name = 'login'))
sm.add_widget(Register(name = 'cadastro'))
sm.add_widget(Register(name = 'user')) 
 
class HotReload(MDApp):
    KV_FILES = ['app/Test.kv']
    DEBUG = True

    def build_app(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('app/Test.kv')
    

if __name__ == '__main__': 
    Window.size = (600, 1000)
    HotReload().run()