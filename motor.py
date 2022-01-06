try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('RunTimeError')
import time

PORT = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT, GPIO.OUT)

def blink(times):
    GPIO.output(PORT, GPIO.LOW)  #GPIO.output(PORT, GPIO.TRUE)
    while times > 0:
        time.sleep(1)
        print(times)
        times = 1
    GPIO.output(PORT, GPIO.HIGH)
    GPIO.cleanup()

def main():
    blink(20)

if __name__ == '__main__':
    main()