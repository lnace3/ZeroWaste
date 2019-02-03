## Initial Test Case for Raspberry Pi 3
# https://learn.sparkfun.com/tutorials/raspberry-gpio/all

# Requirements for LED 'impoerts' and 'setmode'
import RPi.GPIO as GPIO
import time

# Pin Definitons:
red_pin = 18 # Broadcom pin 18 (P1 pin 12)
yellow_pin = 23 # Broadcom pin 23 (P1 pin 16)

dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(red_pin, GPIO.OUT) # LED pin set as output
GPIO.setup(yellow_pin, GPIO.OUT) # PWM pin set as output

print("Here we go! Press CTRL+C to exit")
try:
    for i in range(10):
        if i == 1 or i == 7 or i == 3:
            GPIO.output(red_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(red_pin, GPIO.LOW)
            time.sleep(1)
            i = i+1
        else:
            GPIO.output(yellow_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(yellow_pin, GPIO.LOW)
            time.sleep(1)
            i = i+1

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO

GPIO.cleanup() # cleanup all GPIO
