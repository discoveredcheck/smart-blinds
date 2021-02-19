import RPi.GPIO as GPIO
import time
from threading import Timer
import json
import os
import signal
import sys
import pickle


RECEIVE_PIN = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(RECEIVE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
capture = []
print('Recording...')
start = time.time()
record_duration = 5
while True:
    channel = GPIO.wait_for_edge(RECEIVE_PIN, GPIO.BOTH, timeout=record_duration*1000)
    if channel is None:
        break
    else:
        duration = time.time() - start
        capture.append((duration, GPIO.input(RECEIVE_PIN)))
        if duration > record_duration:
            break
print('Writing to file')
print(len(capture))
pickle.dump(capture, open('out.pkl', 'wb'))
print('Cleaning up')
GPIO.cleanup()
print('Done')
