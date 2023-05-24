import re

def stripRegex(string):
    rstripRegex = re.compile(r'\s*$')
    mo = rstripRegex.sub('', string)
    lstripRegex = re.compile(r'\s*')
    mo2 = lstripRegex.sub('', mo)
    return mo2
print(stripRegex('        aaaa         '), end='')
print('b')