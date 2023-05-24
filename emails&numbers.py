import pyperclip
import re

text = '''Olá! Recentemente, perdi meu celular, mas consegui recuperá-lo graças a um contato salvo 
com o número (11) 555-1234. É importante manter os números atualizados, então aqui estão mais algumas formas de entrar 
em contato comigo: (11) 555-5678, +1 888-999-0000 ou 555-4321 ramal 123. Você também pode me enviar um e-mail para 
meuemail@gmail.com, meu.email@yahoo.com.br, meunome@provedor.com ou meunome.1234@dominio.com. Lembre-se de manter seus 
contatos atualizados com as informações corretas!'''
emailRegex = re.compile(r'([a-zA-Z0-9.+-_%]+@[a-zA-Z0-9.+-_%]+\.\w+)')
numberRegex = re.compile(r'([0-9()+]*\s[0-9-]+)')
mo = emailRegex.findall(text)
mo2 = numberRegex.findall(text)
print('emails encontrados:')
for x in mo:
    print(x)
print('numeros encontrados:')
for x in mo2:
    print(x)
