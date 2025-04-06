import RPi.GPIO as GPIO
import time

potInp = 18
ledPin = 4

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(potInp, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    while True:
            print(GPIO.input(potInp), 'potentiometrinp')
           
            

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