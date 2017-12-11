import RPi.GPIO as GPIO


def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)

    GPIO.output(2, GPIO.LOW)


if __name__ == '__main__':
    main()
