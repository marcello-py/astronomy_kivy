import os

class Image:
    
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

            
    def verificar_caminho(caminho_arquivo):
        
        # Abre o arquivo usando o aplicativo padrão do sistema operacional
        os.system(f'start {caminho_arquivo}')
            

            
    ano = '15'
    mes = '02'
    data = '05'
    datas = ano+mes+data
    imagem = get(datas)
    caminho_arquivo = f'../APOC/{datas}.jpg'
    verificar_caminho(caminho_arquivo)
    if imagem is not None:
        print(f"Arquivo {datas} encontrado!")
    else:
        print("Arquivo não encontrado.")
        
        
