#!/usr/bin/python
from flask import Flask
from play import Remote, TRANSMIT_PIN, Button, Channel
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route('/open')
def open():
    remote.button_press(Button.Up, Channel.Two)
    return "Opened!"

@app.route('/close')
def close():
    remote.button_press(Button.Down, Channel.Two)
    return "Closed!"

if __name__ == '__main__':
    remote = Remote(TRANSMIT_PIN)
    app.run(host='0.0.0.0')