import re
import os
import requests

def extrair_urls_imagens(texto):
    # Expressão regular para encontrar substrings entre aspas duplas que terminam com uma extensão de imagem
    padrao = r'"([^"]*\.(?:jpg|jpeg|png|webp|gif|bmp|svg))"'
    # Encontrar todas as correspondências no texto
    urls = re.findall(padrao, texto, re.IGNORECASE)
    return urls

def baixar_imagens(urls, pasta_destino):
    # Criar a pasta de destino se ela não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    for url in urls:
        # Substituir barras invertidas por barras normais
        print(url)
        url = url.replace('\\/', '/')
        url = url.replace('\\', '/')
        if not url.startswith('https://influencersgonewild.com'):
            url = 'https://influencersgonewild.com' + url
        print(url)
        # Obter o nome do arquivo da URL
        nome_arquivo = os.path.join(pasta_destino, os.path.basename(url))
        try:
            # Baixar o arquivo de imagem
            resposta = requests.get(url)
            # Verificar se a solicitação foi bem-sucedida (status code 200)
            if resposta.status_code == 200:
                # Salvar o arquivo de imagem
                with open(nome_arquivo, 'wb') as arquivo:
                    arquivo.write(resposta.content)
                print(f'Arquivo "{nome_arquivo}" baixado com sucesso.', end='\n\n')
            else:
                print(f'Erro ao baixar o arquivo "{nome_arquivo}": Status Code {resposta.status_code}', end='\n\n')
        except Exception as e:
            print(f'Erro ao baixar o arquivo "{nome_arquivo}": {str(e)}', end='\n\n')

# Exemplo de texto
texto = ''''''
# Pasta de destino para salvar as imagens baixadas
pasta_destino = 'imagens'

# Extrair URLs das imagens
urls_imagens = extrair_urls_imagens(texto)
# Baixar e salvar as imagens na pasta de destino
baixar_imagens(urls_imagens, pasta_destino)
