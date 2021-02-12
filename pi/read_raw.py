from datetime import datetime
import RPi.GPIO as GPIO

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 5
RECEIVE_PIN = 15

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    cumulative_time = 0
    beginning_time = datetime.now()
    print('**Started recording**')
    while cumulative_time < MAX_DURATION:
        time_delta = datetime.now() - beginning_time
        RECEIVED_SIGNAL[0].append(time_delta)
        RECEIVED_SIGNAL[1].append(GPIO.input(RECEIVE_PIN))
        cumulative_time = time_delta.seconds
    print('**Ended recording**')
    print(len(RECEIVED_SIGNAL[0]), 'samples recorded')
    GPIO.cleanup()

