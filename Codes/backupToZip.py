import zipfile, os

if not os.path.exists('./backups'):
    os.makedirs('./backups')
os.chdir('./backups')

c = 1
if os.path.exists('./backup_1'):
    for x in os.listdir():
        if x.startswith('backup_'):
            c += 1

backup = zipfile.ZipFile(f'backup_{c}', 'w')

for foldername, subfolders, filenames in os.walk('/home/solas/Documentos/Solas/Programming/Python'):
    backup.write(foldername)
    for filename in filenames:
        backup.write(os.path.join(foldername, filename))
backup.close()
