import RPi.GPIO as GPIO
import time

potInp = 4
ledPin = 18

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(potInp, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    while True:
            # print(GPIO.input(potInp), 'potentiometrinp')
            # print(GPIO.PWM(potInp))
            GPIO.output(ledPin, 1)

def destroy():
    GPIO.output(ledPin, GPIO.LOW)     
    GPIO.cleanup() 

if __name__ == '__main__':     
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()