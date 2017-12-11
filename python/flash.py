import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    for i in range(10):
        GPIO.output(2, True)
        time.sleep(0.1)
        GPIO.output(2, False)
        time.sleep(0.1)
    GPIO.output(2, GPIO.LOW)
    #GPIO.cleanup()
