from enum import Enum
from datetime import datetime
import time
import RPi.GPIO as GPIO
import argparse

TRANSMIT_PIN = 27
PREAMBLE = '1101100111011010'
class Channel(Enum):
    One = ('11000', '100000001010')
    Two = ('10100', '100000000010')
class Button(Enum):
    Up = ('0011', '0011')
    Down = ('1000', '1110')
    Stop = ('1010', '1100')

class Remote:
    def __init__(self, pin, long_time_ms=0.6, short_time_ms=0.3, num_reps=7):
        self.long_time_ms = long_time_ms
        self.short_time_ms = short_time_ms
        self.pin = pin
        self.num_reps = num_reps
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

    def _send_pattern(self, pattern: str):
        for ch in pattern:
            self._send_bit(ch == '1')

    def _button_press(self, btn: Button, channel: Channel):
        self._set_pin(1)
        time.sleep(0.005)
        self._set_pin(0)
        time.sleep(0.0025)
        self._set_pin(1)
        time.sleep(0.001)
        self._send_pattern(PREAMBLE)
        self._send_pattern(channel.value[0])
        self._send_pattern(btn.value[0])
        self._send_pattern(channel.value[1])
        self._send_pattern(btn.value[1])

    def button_press(self, btn: Button, channel: Channel):
        for _ in range(self.num_reps):
            self._button_press(btn, channel)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Play a RF button press')
    parser.add_argument('--button', required=True)
    parser.add_argument('--channel', required=True)
    parser.add_argument('--duration')
    parser.add_argument('--gpio-pin', default=TRANSMIT_PIN)
    args = parser.parse_args()

    remote = Remote(args.gpio_pin)
    start = time.time()
    while True:
        remote.button_press(getattr(Button, args.button), getattr(Channel, args.channel))
        if not args.duration or time.time()-start>args.duration:
            GPIO.cleanup()
            break 
        time.sleep(1.0)
