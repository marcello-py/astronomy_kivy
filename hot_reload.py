from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from database import Database
from time import sleep

class FirstScreen(Screen):
   pass

class LoginScreen(Screen):
    def login_user(self):
        # Coletar os valores de entrada
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Criar uma instância da classe Database
        db = Database('astronomy.db')
        
        # Checar as credencias no banco de dados
        if db.check_credentials(username, password):
            self.manager.current = 'suced'
        else:
            print('Credenciais inválidas')
        print(username, password)
        db.conn.close()

class RegisterScreen(Screen):
    def register_user(self):
        # Coletar os valores de entrada
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Criar uma instância da classe Database
        db = Database('astronomy.db')

        # Inserir o usuário no banco de dados
        db.insert_user(username, password) 
    
        self.manager.current = 'created' 

        # Fechar a conexão com o banco de dados
        db.conn.close()


class CreatedScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(FirstScreen(name = 'init'))
sm.add_widget(LoginScreen(name = 'login')) 
sm.add_widget(RegisterScreen(name = 'register'))
sm.add_widget(CreatedScreen(name = 'created')) 
sm.add_widget(ResultScreen(name = 'suced')) 
 
class HotReload(MDApp):
    KV_FILES = ['app/Test.kv']
    DEBUG = True

    def build_app(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('app/Test.kv')
    
if __name__ == '__main__': 
    Window.size = (640, 860)
    HotReload().run()
