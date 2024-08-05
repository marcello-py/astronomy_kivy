from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from database import Database
#from kivy.uix.image import Image
#from kivy.uix.floatlayout import FloatLayout
#from kivymd.uix.list import ThreeLineListItem
#from get_image import Image
#from scraping import Scraping

class FirstScreen(Screen):
    # Para agendar a execução da animação
    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_once(self.setup_logo_animation, 0) 

    def setup_logo_animation(self, *args):
        image_cat = self.ids.logo_image
        image_moon = self.ids.logo_moon
        anim_moon = Animation(size_hint=(.40, .40), duration=1) + Animation(size_hint=(.20, .20), duration=1)
        anim = Animation(size_hint=(.40, .40), duration=1) + Animation(size_hint=(.70, .70), duration=1)
        
        #anim.repeat = True
        anim.start(image_cat)
        anim_moon.start(image_moon)


class LoginScreen(Screen):
    """Checar o usuário e senha e concede o login."""
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
            else:
                self.ids.error_label.text = 'Usuário ou senha incorreto!'
                Clock.schedule_once(self.clear_error_message, 3)  

        except Exception as e:
            print(f'Erro ao fazer login: {e}')
        finally:
            db.conn.close()

    def clear_error_message(self, dt):
        self.ids.error_label.text = '' 



class RegisterScreen(Screen):
    """Registra um novo usuário no banco de dados."""
    def register_user(self):
        # Coletar os valores de entrada
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Criar uma instância da classe Database
        db = Database('astronomy.db') 

        # Inserir o usuário no banco de dados
        db.insert_user(username, password)

        #Define a tela a próxima tela com o 'suced'
        self.manager.current = 'suced' 

        # Fechar a conexão com o banco de dados
        db.conn.close()

class ResultScreen(Screen):
    """Seleciona com base nos parâmetros recebidos a imagem no banco de dados"""
    def button_search(self):
        '''  # Obter a imagem do banco APOC
        ano = self.ano
        mes = self.mes
        data = self.data 
        
        imagem = get(datas) # instanciando a classe
        imagem.get(ano, mes, data) # capturar os dados da variáveis
        self.manager.current = 'scraping' '''
        self.manager.current = 'scraping'
    
    def button_settings(self):
        pass
        
    def button_profile(self):
        self.manager.current = 'profile'

class CardOptiontScreen(Screen):
    pass

class CardConsultScreen(Screen):
#    def update_user_list(self, users):
#        user_list = self.ids.user_list
#        user_list.clear_widgets()
#        for user in users:
#            user_label = MDLabel(text=user[1])
#            user_list.add_widget(user_label)
    def button_settings(self):
        self.manager.current = 'option'

class CardProfiletScreen(Screen):
    pass

sm = ScreenManager()

# Adicionando as telas ao ScreenManager
sm.add_widget(FirstScreen(name='init'))
sm.add_widget(LoginScreen(name='login')) 
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(ResultScreen(name='suced')) 
sm.add_widget(CardConsultScreen(name='scraping'))
sm.add_widget(CardProfiletScreen(name='profile'))




class Test(MDApp):
    KV_FILES = [r'app\__pycache__\test.kv']
    DEBUG = True

    def build_app(self):    
        self.theme_cls.primary_palette = 'Gray' 
        return Builder.load_file(r'app\__pycache__\test.kv')
        
if __name__ == '__main__': 
    Window.size = (500, 800)
    Test().run()
