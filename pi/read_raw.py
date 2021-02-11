import RPi.GPIO as GPIO

RECEIVE_PIN = 15

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    samples = []
    print('**Started recording**')
    for _ in range(100000):
        samples.append(GPIO.input(RECEIVE_PIN))
    print('**Ended recording**')
    print(len(samples), 'samples recorded')
    GPIO.cleanup()
