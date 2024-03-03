from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from database import Database
#from scraping import Scraping

class FirstScreen(Screen):
   pass

class LoginScreen(Screen):
  
    def login_user(self):
        try:
            # Coletar os valores de entrada
            username = self.ids.username_input.text
            password = self.ids.password_input.text

            # Criar uma instância da classe Database
            db = Database('astronomy.db')

            # Checar as credencias no banco de dados
            if db.check_credentials(username, password):
                    self.manager.current = 'suced'
            db.conn.close()
        except ValueError:
            print('error')

class RegisterScreen(Screen):
    def register_user(self):
        # Coletar os valores de entrada
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Criar uma instância da classe Database
        db = Database('astronomy.db') 

        # Inserir o usuário no banco de dados
        db.insert_user(username, password) 
        self.manager.current = 'suced' 

        # Fechar a conexão com o banco de dados
        db.conn.close()

class ConsultScreen(Screen):
    pass 

class ResultScreen(Screen):
    pass

    def button_search(self):
        
        '''  # Obter a imagem do banco APOC
        ano = self.ano
        mes = self.mes
        data = self.data 
        
        imagem = get(datas) # instanciando a classe
        imagem.get(ano, mes, data) # capturar os dados da variáveis
        self.manager.current = 'scraping' '''
        self.manager.current = 'scraping'
    

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(FirstScreen(name = 'init'))
sm.add_widget(LoginScreen(name = 'login')) 
sm.add_widget(RegisterScreen(name = 'register'))
sm.add_widget(ResultScreen(name = 'suced')) 
sm.add_widget(ConsultScreen(name = 'scraping'))


class HotReload(MDApp):
    KV_FILES = ['app/Test.kv']
    DEBUG = True

    def build_app(self):    
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('app/Test.kv')
        
if __name__ == '__main__': 
    Window.size = (500, 800)
    HotReload().run()
