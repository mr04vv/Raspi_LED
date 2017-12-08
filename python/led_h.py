import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)

    GPIO.output(25, GPIO.HIGH)
    # time.sleep(2)
    # GPIO.cleanup()
