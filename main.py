from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
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
        print(username, password)
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
    
        self.manager.current = 'user' 

        # Fechar a conexão com o banco de dados
        db.conn.close()


class LoginSucess(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(FirstScreen(name = 'login'))
sm.add_widget(LoginScreen(name = 'acess')) 
sm.add_widget(Register(name = 'cadastro'))
sm.add_widget(LoginSucess(name = 'suced')) 


class Test(MDApp):
    def build_app(self):
        return Builder.load_file('app/Test.kv')

if __name__ == '__main__':
    Window.size = (640, 960)
    Test().run()