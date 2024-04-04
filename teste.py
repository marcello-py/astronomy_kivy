from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from database import Database
#from get_image import Image
#from scraping import Scraping

class FirstScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_once(self.setup_logo_animation, 0) #para agendar a execução da animação

    def setup_logo_animation(self, *args):
        image_cat = self.ids.logo_image
        image_moon = self.ids.logo_moon
        anim_moon = Animation(size_hint=(.40, .40), duration=1) + Animation(size_hint=(.20, .20), duration=1)
        anim = Animation(size_hint=(.40, .40), duration=1) + Animation(size_hint=(.70, .70), duration=1)
        
        #anim.repeat = True
        anim.start(image_cat)
        anim_moon.start(image_moon)


class LoginScreen(Screen):
    def login_user(self):
        try:
            # Coletar os valores de entrada
            username = self.ids.username_input.text
            password = self.ids.password_input.text
            # Criar uma instância da classe Database
            db = Database('astronomy.db')
            # Checar as credenciais no banco de dados
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


class ResultScreen(Screen):
    def button_search(self):
        
        '''  # Obter a imagem do banco APOC
        ano = self.ano
        mes = self.mes
        data = self.data 
        
        imagem = get(datas) # instanciando a classe
        imagem.get(ano, mes, data) # capturar os dados da variáveis
        self.manager.current = 'scraping' '''
        self.manager.current = 'scraping'

    def button_profile(self):
        db = Database('astronomy.db')
        db.view_all_users()

class CardConsultScreen(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(FirstScreen(name='init'))
sm.add_widget(LoginScreen(name='login')) 
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(ResultScreen(name='suced')) 
sm.add_widget(CardConsultScreen(name='scraping'))

class Test(MDApp):
    KV_FILES = ['astronomy_kivy/app/test.kv']
    DEBUG = True
    

    def build_app(self):    
        self.theme_cls.primary_palette = 'Gray' 
        return Builder.load_file('astronomy_kivy/app/test.kv')
        
if __name__ == '__main__': 
    Window.size = (500, 800)
    Test().run()