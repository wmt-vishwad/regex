import re
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1233

Mr. Sachafar
Mr smith
Ms Davis
Mrs. Robinston
Mr. T

cat
mat
pat
bat
'''

sentence = 'start a sentence and then bring it to an end'

pattern = re.compile(r'abc')
pattern = re.compile(r'\d\d\d')
pattern = re.compile(r'\d\d\d.\d\d\d')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[^b]at')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'Mr\.')
pattern = re.compile(r'Mr\.?')
pattern = re.compile(r'Mr\.?\s[A-Z]')
pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

#pattern = re.compile(r'sentence')
#pattern = re.compile(r'start',re.IGNORECASE)
#matches = pattern.match(sentence)
#print(matches)

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#with open('name.txt', 'r') as f:
 #   contents = f.read()
  #  matches = pattern.finditer(contents)

#for match in matches:
 #   print(match)

