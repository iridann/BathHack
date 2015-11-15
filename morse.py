import mraa, time, socket, sys

dotLength = 0.08
dashLength = dotLength * 3
wordSpacing = dotLength * 7

pin = mraa.Gpio(3)
#pin.period_us(700)
#pin.enable(True)
pin.dir(mraa.DIR_OUT)
loud = 1
light = mraa.Aio(0)

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './win98'
sock.connect(server_address)

def beep(slt):
    pin.write(loud)
    time.sleep(slt)
    pin.write(0)
    time.sleep(dotLength)

def beepm(inputString):
	words = inputString.split(' ')
	morseString = ''
	valueString = ''
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


	
while 1:
	data = sock.recv(1)
	print data
	beepm(data)


