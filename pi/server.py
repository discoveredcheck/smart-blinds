#!/usr/bin/python
from flask import Flask
from play import Remote, TRANSMIT_PIN, Button, Channel
import logging
app = Flask(__name__)

logger = logging.getLogger('blinds_server')

@app.route('/')
def hello():
    return "Hello!"

@app.route('/open')
def open():
    logger.info('open')
    remote.button_press(Button.Up, Channel.Two)
    return "Opened!"

@app.route('/close')
def close():
    remote.button_press(Button.Down, Channel.Two)
    return "Closed!"

@app.route('/stop')
def stop():
    remote.button_press(Button.Stop, Channel.Two)
    return "Stopped!"

if __name__ == '__main__':
    remote = Remote(TRANSMIT_PIN)
    logging.basicConfig(filename='/var/log/blinds.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')