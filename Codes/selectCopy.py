import shutil, os

os.chdir('/home/solas/Documentos/Solas/imgs')
for x in os.listdir():
    if x.endswith('.jpg') or x.endswith('.pdf'):
        shutil.copy(f'./{x}', '/home/solas/Documentos')
