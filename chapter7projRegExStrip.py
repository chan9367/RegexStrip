import re

def betterStrip(text):
    regex = re.compile(r'\s+')
    mo = regex.search(text)
    if mo is None:
        print(text)
    else:
        print(regex.sub('', text))

print('Enter text to strip():')
text = input()
betterStrip(text)
