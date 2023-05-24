import os

a = 0
os.chdir('/home/solas/Documentos/Solas/Programming/Python/testZone')
for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        a += os.path.getsize(os.path.join('.', filename))

print(a/1024/1024, 'MB')
