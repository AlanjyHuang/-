class motor:
    def __init__(self) :
        try:
            import RPi.GPIO as GPIO
        except RuntimeError:
            print('RunTimeError')
        import time

        PORT = 14
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PORT, GPIO.OUT)

    def blink(self,times):
        GPIO.output(PORT, GPIO.LOW)  #GPIO.output(PORT, GPIO.TRUE)
        while times > 0:
            time.sleep(1)
            print(times)
            times -= 1
        GPIO.output(PORT, GPIO.HIGH)
        GPIO.cleanup()



if __name__ == '__main__':
    mymotor=motor()
    mymotor.blink(20)