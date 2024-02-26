import os

class Image:
    
    @staticmethod # @statictmethod é usado para definir métodos que pertencem à classe, mas não dependem de informações específicas de cada objeto
    def get(datas):
        try:
            dados = f'../APOC/{datas}.jpg'
            if os.path.exists(dados): # Verificar se o arquivo existe dentro da pasta
                print('arquivo existe')
                with open(dados, 'rb') as file: # Abri o arquivo em binário
                    imagem = file.read()  # Lê o conteúdo do arquivo da imagem
                    return imagem  # Retorna a imagem
            else:
                print(f'o arquivo {datas}, não foi localizado.')
                
        except FileNotFoundError:
            print(f'o arquivo {datas}, não foi localizado.')

            
    @staticmethod
    def verificar_caminho(caminho_arquivo):
        os.system(f'start {caminho_arquivo}') # Abre o arquivo usando o aplicativo padrão do sistema operacional
            

    @staticmethod
    def get_image():
        pass
    
    
ano = '15'
mes = '02'
data = '05'
datas = ano+mes+data
imagem = Image.get(datas)
caminho_arquivo = f'../APOC/{datas}.jpg'
Image.verificar_caminho(caminho_arquivo)
if imagem is not None:
    print(f"Arquivo {datas} encontrado!")
else:
    print("Arquivo não encontrado.")


def casa(self):
    pass