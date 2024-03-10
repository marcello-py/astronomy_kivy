from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from database import Database
#from scraping import Scraping

class FirstScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_once(self.setup_logo_animation, 0) #para agendar a execução da animação

    def setup_logo_animation(self, *args):
        image = self.ids.logo_image
        anim = Animation(size_hint=(.40, .40), duration=1) + Animation(size_hint=(.70, .70), duration=1)
        #anim.repeat = True
        anim.start(image)


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

class ConsultScreen(Screen):
    pass 

class ResultScreen(Screen):
    pass

class AnimationScreen(Screen):
    def on_enter(self):
        # Criando a imagem
        image = Image(source='astronomy_kivy/saturn.png', size=(100, 100))

        # Criando a animação
        anim = Animation(x=100, y=100) + Animation(x=200, y=200)
        anim.repeat = True  # Repetir a animação indefinidamente
        anim.start(image)

        # Criando o layout e adicionando a imagem
        layout = FloatLayout()
        layout.add_widget(image)

        # Adicionando o layout à tela
        self.add_widget(layout)

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(FirstScreen(name='init'))
sm.add_widget(LoginScreen(name='login')) 
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(ResultScreen(name='suced')) 
sm.add_widget(ConsultScreen(name='scraping'))
sm.add_widget(AnimationScreen(name='animation'))

class Test(MDApp):
    KV_FILES = ['astronomy_kivy/app/test.kv']
    DEBUG = True

    def build_app(self):    
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('astronomy_kivy/app/test.kv')
        
if __name__ == '__main__': 
    Window.size = (500, 800)
    Test().run()