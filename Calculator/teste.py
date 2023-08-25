import re

print(re.compile(r'(\d*)(\w)?').search('1a').groups()[:2])
