import os

if not os.path.exists('./madLibs'):
    os.makedirs('./madLibs')
os.chdir('./madLibs')

textFile = open('text.txt', 'r')
text = textFile.read()
textFile.close()

while 'adjective' in text.lower() or 'noun' in text.lower() or 'verb' in text.lower() or 'adverb' in text.lower():
    if 'adjective' in text.lower():
        rewrite = input('Enter an adjective: ')
        text = text.split()
        c = 0
        for x in text:
            if x.lower() == 'adjective':
                text[c] = rewrite
                break
            c += 1
        text = ' '.join(text)
    if 'noun' in text.lower():
        rewrite = input('Enter a noun: ')
        text = text.split()
        c = 0
        for x in text:
            if x.lower() == 'noun':
                text[c] = rewrite
                break
            c += 1
        text = ' '.join(text)
    if 'verb' in text.lower():
        rewrite = input('Enter an verb: ')
        text = text.split()
        c = 0
        for x in text:
            if x.lower() == 'verb':
                text[c] = rewrite
                break
            c += 1
        text = ' '.join(text)
    if 'adverb' in text.lower():
        rewrite = input('Enter an adverb: ')
        text = text.split()
        c = 0
        for x in text:
            if x.lower() == 'adverb':
                text[c] = rewrite
                break
            c += 1
        text = ' '.join(text)


textFile = open('text.txt', 'w')
textFile.write(text)
