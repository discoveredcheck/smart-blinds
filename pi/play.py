import time
import RPi.GPIO as GPIO

TRANSMIT_PIN = 27

class Remote:
    def __init__(self, pin, long_time_ms=0.6, short_time_ms=0.3):
        self.long_time_ms = long_time_ms
        self.short_time_ms = short_time_ms
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
    
    def _set_pin(self, val):
        GPIO.output(self.pin, val)

    def _pull_line(self, val, time_ms=None):
        GPIO.output(self.pin, val)
        if time_ms:
            time.sleep(time_ms*0.001)

    def _send_bit(self, bit: bool):
        if bit:
            self._pull_line(1, self.long_time_ms)
            self._pull_line(0, self.short_time_ms)
        else:
            self._pull_line(1, self.short_time_ms)
            self._pull_line(0, self.long_time_ms)
