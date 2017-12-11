import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, GPIO.HIGH)


if __name__ == "__main__":
    main()
