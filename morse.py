inputString = "Hello World I am a Morse Code Parser"
morseString = ''
valueString = ''
dotLength = 1
dashLength = dotLength * 3
wordSpacing = dotLength * 7
words = inputString.split(' ')

for w in words:
    for c in w.upper():
        q = '_ETIANMSURWDKGOHVF_L_PJBXCYZQ__54_3___2__+____16=/_____7___8_90'.find(
            c)
        s = ''
        while q:
            s = '-.'[q % 2] + s
            q = ~-q // 2
        morseString += (['/', '--..--', '..--..', '.-.-.-', ''][' ,?.'.find(c)] + s +' ')
    morseString += '\n'


for c in morseString:
    if c == '.' or c == '':
        valueString += str(dotLength) + ','
    elif c == '-' or c == ' ':
        valueString += str(dashLength) + ','
    elif c == '\n':
        valueString += str(wordSpacing) + ','

print (valueString.strip( ',' ))




