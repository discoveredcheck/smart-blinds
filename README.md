# smart-blinds

This project controls motorised window blinds from a phone.

## How it works

The blinds come with a radio frequency remote control. The project learns the signal of that remote and sends the same signal from a Raspberry Pi. The blinds and the original remote stay unchanged.

The project has three parts. The first part is a set of scripts on the Raspberry Pi that record and replay the remote signal. The second part is a small web server on the Raspberry Pi. The third part is an Android app that calls the server.

## Hardware

The project needs a Raspberry Pi. A radio frequency receiver module connects to GPIO 15, using BCM numbering. A radio frequency transmitter module connects to GPIO 27, using BCM numbering.

## The signal

A 1 bit is 0.6 ms high and then 0.3 ms low. A 0 bit is 0.3 ms high and then 0.6 ms low.

Each press starts with a sync pulse. The sync pulse is 5 ms high, 2.5 ms low and then 1 ms high.

After the sync pulse comes a frame of 41 bits. The frame starts with a 16 bit preamble and a 5 bit channel code. Then come a 4 bit button code, a 12 bit second channel code and a 4 bit second button code.

The `play.py` script repeats each press 7 times, as the original remote does.

I decoded the bits by hand from the plotted waveform.

## Files

The Raspberry Pi files are in the `pi/` folder.

- `pi/read_raw.py` samples the receiver input in a loop for 5 seconds. It stores each sample with its time and saves the capture to `out.pkl`.
- `pi/record.py` records each signal edge with its time for 5 seconds. A signal edge is a change of the input level. The script saves the capture to `out.pkl`. It gives a smaller and cleaner capture than `pi/read_raw.py`.
- `pi/plot_waveform.py` plots a capture as a step waveform with matplotlib.
- `pi/out.json` is one raw capture of a button press.
- `pi/down_or_stop.txt` holds my notes with the decoded codes for channel 1, channel 2 and all channels, and the bit timings.
- `pi/play.py` sends a button press. It has the class `Remote`, the buttons `Up`, `Down` and `Stop`, and the channels `One` and `Two`.
- `pi/server.py` is a Flask server with the routes `/`, `/open`, `/close` and `/stop`. It sends the press on channel `Two`, writes a log to `/var/log/blinds.log` and listens on port 5000.
- `android/BlindsControl` is the Android app, written in Java.

## How to run

Follow the steps for the Raspberry Pi first, then the steps for the phone.

### On the Raspberry Pi

Run the commands in the `pi/` folder.

1. Connect the receiver to GPIO 15 and the transmitter to GPIO 27.
2. Install the Python packages `RPi.GPIO`, `flask` and `matplotlib`.
3. Record a button press with `python3 record.py`. Press the button on the remote during the 5 seconds.
4. Look at the capture with `python3 plot_waveform.py out.pkl`.
5. Send a press with `python3 play.py --button Up --channel Two`.
6. Start the server with `sudo python3 server.py`. The server needs to write to `/var/log/blinds.log`.

### On the phone

1. Open `android/BlindsControl` in Android Studio.
2. Set `SERVER` in `MainActivity.java` to the address of the Raspberry Pi, with port 5000.
3. Build the app and install it on the phone.

The phone and the Raspberry Pi must be on the same network.

## Limits

- The codes in `play.py` are the codes of my remote. Another remote needs its own codes.
- The server uses only channel `Two`.
- The server has no login and uses plain HTTP. Use it only on a home network.
- There are no tests and no requirements file.

## Plans

The plans for the project are in `ROADMAP.md`.

## License

The project is under the MIT license. See the `LICENSE` file.
