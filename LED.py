import RPi.GPIO as GPIO
import time
class LED:
	def __int__(self):
		self.pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}

		GPIO.setmode(GPIO.BOARD)
		for i in self.pins:
			GPIO.setup(self.pins[i], GPIO.OUT)
			GPIO.output(self.pins[i], GPIO.HIGH)

		self.p_R = GPIO.PWM(self.pins['pin_R'], 2000)
		self.p_G = GPIO.PWM(self.pins['pin_G'], 2000)
		self.p_B = GPIO.PWM(self.pins['pin_B'], 5000)

		self.p_R.start(100)
		self.p_G.start(100)
		self.p_B.start(100)


	def addColor(self,r, g, b) :
		red = hex(r)
		green = hex(g)
		blue = hex(b)
		color = '0x' + red[2:].zfill(2) + green[2:].zfill(2) + blue[2:].zfill(2)
		return int(color, 16)

	def map(self,x, in_min, in_max, out_min, out_max):
		return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

	def setColor(col,self):
		R_val = (col & 0xFF0000) >> 16
		G_val = (col & 0x00FF00) >> 8
		B_val = (col & 0x0000FF) >> 0
		
		R_val = map(R_val, 0, 255, 0, 100)
		G_val = map(G_val, 0, 255, 0, 100)
		B_val = map(B_val, 0, 255, 0, 100)

		self.p_R.ChangeDutyCycle(100 - R_val)
		self.p_G.ChangeDutyCycle(100 - G_val)
		self.p_B.ChangeDutyCycle(100 - B_val)
	def start(self,times,r,g,b):
		try:
			while times > 0:
				self.setColor(self.addColor(r,g,b))         #輸入RGB(10進位)
				time.sleep(1)
				print(times)
				times -= 1
			GPIO.cleanup()
		except KeyboardInterrupt:
			self.p_R.stop()
			self.p_G.stop()
			self.p_B.stop()
			for i in self.pins:
				GPIO.output(self.pins[i], GPIO.HIGH)
			GPIO.cleanup()

if __name__=="__main__":
	myLed=LED()
	myLed.start(5,255,0,0)