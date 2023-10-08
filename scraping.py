import requests
from bs4 import BeautifulSoup

class Scraping:
    def obter_imagem_apod(data):
        url_base = 'https://apod.nasa.gov/apod/archivepixFull.html'

        # Enviar uma solicitação GET para a URL
        r = requests.get(url_base)

        soup = BeautifulSoup(r.text, 'html.parser')

            # Procurar os links para as páginas individuais das imagens
        links = soup.find_all('a', href=True)

            # Iterar pelos links
        for link in links:
                # Verificar se o link contém a data especificada
            if data in link['href']:
                    # Construir a URL completa para a imagem
                imagem_url = f'https://apod.nasa.gov/apod/{link["href"]}'

                return imagem_url

        return None

# Exemplo de uso
    data = 'ap970826.html'  # Substitua pela data desejada
    url_da_imagem = obter_imagem_apod(data)

    if url_da_imagem:
        print(f'URL da imagem para a data {data}: {url_da_imagem}')
    else:
        print(f'Imagem não encontrada para a data {data}')
