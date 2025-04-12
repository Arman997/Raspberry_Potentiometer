import RPi.GPIO as GPIO
import spidev
from time import sleep

ledPin = 17

spi = None
pwm = None


def setup():
    
    global spi, pwm


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 50000
    spi.mode = 0b00
    pwm = GPIO.PWM(ledPin, 1000)
    pwm.start(0)


def read_channel(channel):
    
    if channel < 0 or channel > 7:
        return -1
    
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) | adc[2]
    return data


def destroy():
    GPIO.output(ledPin, GPIO.LOW)     
    GPIO.cleanup()
    spi.close()

if __name__ == '__main__':     
    print ('Program is starting...')
    setup()
    try:
        while True:
            value = read_channel(0)
            if value < 5:
                brightness = 0
            else:    
                brightness = (value / 1023.0) * 100
            pwm.ChangeDutyCycle(brightness)
            print(f"Potentiometer value: {value} -> LED brightness: {brightness}%")
            sleep(0.4)

    except KeyboardInterrupt:  
        destroy()    
