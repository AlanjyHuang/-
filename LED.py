import RPi.GPIO as GPIO
import time

pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}

GPIO.setmode(GPIO.BOARD)
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)
    GPIO.output(pins[i], GPIO.HIGH)

p_R = GPIO.PWM(pins['pin_R'], 2000)
p_G = GPIO.PWM(pins['pin_G'], 2000)
p_B = GPIO.PWM(pins['pin_B'], 5000)

p_R.start(100)
p_G.start(100)
p_B.start(100)


def addColor(r, g, b) :
    red = hex(r)
    green = hex(g)
    blue = hex(b)
    color = '0x' + red[2:].zfill(2) + green[2:].zfill(2) + blue[2:].zfill(2)
    return int(color, 16)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):
	R_val = (col & 0xFF0000) >> 16
	G_val = (col & 0x00FF00) >> 8
	B_val = (col & 0x0000FF) >> 0
	
	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	B_val = map(B_val, 0, 255, 0, 100)

	p_R.ChangeDutyCycle(100 - R_val)
	p_G.ChangeDutyCycle(100 - G_val)
	p_B.ChangeDutyCycle(100 - B_val)

try:
    times = 5
	while times > 0:
        #setColor(addColor())         #輸入RGB(10進位)
        time.sleep(1)
        print(times)
        times -= 1
    GPIO.cleanup()
except KeyboardInterrupt:
	p_R.stop()
	p_G.stop()
	p_B.stop()
	for i in pins:
		GPIO.output(pins[i], GPIO.HIGH)
	GPIO.cleanup()
