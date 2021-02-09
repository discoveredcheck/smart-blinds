# Introduction

The goal of this project to convert a set of motorised blinds (anything connected to a radio operated motor, really) into smart blinds. Generally this means adding support to operate the device from smartphones, voice assistants or any other platform that interfaces with the device via http(s). We are starting out with a device (blinds) which is already works with a radio frequency remote. The task at hand is to send the same commands to the device as sent by the remote. One way to do this by simply sending signals to the remote's original circuitry by hooking up the remote to a microcontroller. But that mean we wont be able to use the original remote provided by the device anymore. Another way is to "learn" the remote and have a microcontroller mimick its outputs. We will use the latter method. The high level plan is to do the following

1. Use a RF receiver to read and learn the codes sent by each button of the remote.
2. Use a RF transmittor connected to a Raspberry Pi to generate the codes learned above.
3. Build an Alexa interface to send commands to Raspberri Pi.

# Resources

Several projects are available for steps 1 and 2. For the most part we will follow [this](https://github.com/milaq/rpi-rf) repo to build and "train" the RF module. For makming it "smart", we have two options, each with their pros and cons.

## Option 1 - Alexa enabled device

## Option 2 - Alexa "skill"

## Comnparison

# Hardware
