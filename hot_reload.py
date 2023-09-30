from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from database import Database


class FirstScreen(Screen):
   pass


class LoginScreen(Screen):
    def login_user(self):
        # Coletar os valores de entrada
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        db = Database('astronomy.db')
        if db.check_credentials(username, password):
            self.manager.current = 'sucess'
        else:
            print('Credenciais inválidas')
        print(username)
        print(password)
        db.conn.close()

class Register(Screen):
    def register_user(self):
        # Coletar os valores de entrada
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Criar uma instância da classe Database
        db = Database('astronomy.db')

        # Inserir o usuário no banco de dados
        db.insert_user(username, password) 
        
        # Redirecionar para a tela de usuário criado
        self.manager.current = 'sucess' 

        # Fechar a conexão com o banco de dados
        db.conn.close()
class CreatedLogin(Screen):
    pass

class LoginSucess(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(FirstScreen(name = 'login'))
sm.add_widget(LoginScreen(name = 'acess')) 
sm.add_widget(Register(name = 'cadastro'))
sm.add_widget(CreatedLogin(name = 'user')) 
sm.add_widget(LoginSucess(name = 'sucess')) 
 
class HotReload(MDApp):
    KV_FILES = ['app/Test.kv']
    DEBUG = True

    def build_app(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('app/Test.kv')
    

if __name__ == '__main__': 
    Window.size = (600, 1000)
    HotReload().run()
