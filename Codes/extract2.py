import re
import os
import requests

def extrair_urls_arquivos(texto):
    # Expressão regular para encontrar URLs de arquivos de imagem ou vídeo
    padrao = r'"([^"]*\.(?:jpg|jpeg|png|webp|gif|bmp|svg|mp4|avi|mov|mkv))"'
    # Encontrar todas as correspondências no texto
    urls = re.findall(padrao, texto, re.IGNORECASE)
    return urls

def baixar_arquivos(urls, pasta_destino):
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
            # Baixar o arquivo
            resposta = requests.get(url)
            # Verificar se a solicitação foi bem-sucedida (status code 200)
            if resposta.status_code == 200:
                # Salvar o arquivo
                with open(nome_arquivo, 'wb') as arquivo:
                    arquivo.write(resposta.content)
                print(f'Arquivo "{nome_arquivo}" baixado com sucesso.', end='\n\n')
            else:
                print(f'Erro ao baixar o arquivo "{nome_arquivo}": Status Code {resposta.status_code}', end='\n\n')
        except Exception as e:
            print(f'Erro ao baixar o arquivo "{nome_arquivo}": {str(e)}', end='\n\n')

def extrair_links_html(html):
    # Expressão regular para encontrar URLs entre aspas duplas
    padrao = r'"(http[s]?://[^"]+)"'
    # Encontrar todas as correspondências no HTML
    urls = re.findall(padrao, html)
    return urls

def baixar_arquivos_de_url(url, pasta_destino):
    try:
        # Obter o conteúdo HTML da URL
        resposta = requests.get(url)
        if resposta.status_code == 200:
            # Extrair URLs de arquivos do HTML
            urls_arquivos = extrair_urls_arquivos(resposta.text)
            # Criar pastas para imagens e vídeos dentro da pasta de destino
            pasta_imagens = os.path.join(pasta_destino, 'imagens')
            pasta_videos = os.path.join(pasta_destino, 'videos')
            # Baixar e salvar os arquivos na pasta de destino correspondente
            baixar_arquivos([url for url in urls_arquivos if url.endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.svg'))], pasta_imagens)
            baixar_arquivos([url for url in urls_arquivos if url.endswith(('.mp4', '.avi', '.mov', '.mkv'))], pasta_videos)
        else:
            print(f'Erro ao acessar a URL "{url}": Status Code {resposta.status_code}', end='\n\n')
    except Exception as e:
        print(f'Erro ao acessar a URL "{url}": {str(e)}', end='\n\n')

# URL de exemplo
url_exemplo = ''

# Pasta de destino para salvar os arquivos baixados
pasta_destino = ''

# Baixar arquivos da URL fornecida
baixar_arquivos_de_url(url_exemplo, pasta_destino)
