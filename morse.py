import mraa, time

inputString = "SOS we want food"
morseString = ''
valueString = ''
dotLength = 0.08
dashLength = dotLength * 3
wordSpacing = dotLength * 7
words = inputString.split(' ')

pin = mraa.Gpio(2)
pin.dir(mraa.DIR_OUT)


def beep(slt):
    pin.write(1)
    time.sleep(slt)
    pin.write(0)
    time.sleep(dotLength)


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
    if c == '.':
        beep(dotLength)
    elif c == '-':
        beep(dashLength)
    elif c == '\n':
        time.sleep(wordSpacing)
    elif c == ' ':
	time.sleep(dotLength * 5)

	
print (valueString.strip( ',' ))




