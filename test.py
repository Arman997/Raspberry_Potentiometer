import RPi.GPIO as GPIO
import time

pwm_input_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_input_pin, GPIO.IN)

def read_pwm(pin):
    # Ждём начала HIGH
    while GPIO.input(pin) == 0:
        pass
    start = time.time()

    # Ждём конца HIGH
    while GPIO.input(pin) == 1:
        pass
    high = time.time()

    # Ждём конца LOW
    while GPIO.input(pin) == 0:
        pass
    low = time.time()

    high_time = high - start
    low_time = low - high
    period = high_time + low_time
    duty_cycle = (high_time / period) * 100

    return duty_cycle

try:
    while True:
        pwm = read_pwm(pwm_input_pin)
        print(f"PWM duty cycle: {pwm:.1f}%")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
