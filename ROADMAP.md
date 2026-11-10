# Roadmap

This is my plan for the next six months of work on the project. I do the work alone, with one milestone for each month.

## Where the project is today

The Raspberry Pi can record the signal of the remote, and I decoded the codes by hand from the plotted waveform. `play.py` sends the up, down and stop presses for two channels. A Flask server on the Pi has the routes `/open`, `/close` and `/stop`. An Android app with three buttons calls the server.

Some points are still open. The codes and the GPIO numbers are fixed in the code. The server address is fixed in the app. The server uses one channel and has no login. There are no tests. The voice control from my first plan is not built.

## Month 1. A clean base

At the end of this month, the code runs from a fresh checkout with one configuration file.

- Add a requirements file with fixed versions.
- Move the GPIO numbers, the bit timings, the codes and the server port into one configuration file.
- Fix the command line of `play.py`. Today `--duration` and `--gpio-pin` are read as text instead of as numbers.
- Remove the debugger stop from `plot_waveform.py`.
- Use one capture format. Today the scripts write `out.pkl` and the repository holds `out.json`.
- Add unit tests for the bit patterns that `Remote` sends, with the GPIO library replaced by a test double.
- Add continuous integration that runs a linter and the tests on each push.

## Month 2. Decode a remote with a script

At the end of this month, a new remote can be learned without reading a waveform by hand.

- Write a decoder that turns a capture into bits. It sorts each pulse into long or short and finds the sync pulse.
- Split a decoded press into preamble, channel code and button code, and compare the repeats of one press.
- Add a learn command that records one button, decodes it and stores the code in the configuration file.
- Add the code for all channels to `play.py`. Today it is only in my notes in `down_or_stop.txt`.
- Use `out.json` as test data for the decoder.

## Month 3. A real server

At the end of this month, the server controls each channel and runs as a service.

- Add the channel as a parameter of each route. Today the server uses only channel `Two`.
- Return JSON with the result of each request.
- Add a token that each request must carry. Today the server has no login.
- Run the server as a systemd service, with an install script and a log path from the configuration file.
- Estimate the position of the blinds from the travel time, and add a route that moves the blinds to a position in percent.
- Add schedules, for example open at a fixed time each morning.

## Month 4. The Android app

At the end of this month, the app works on a new phone without a change to the code.

- Add a settings screen for the server address and the token. Today the address is fixed in `MainActivity.java`.
- Find the Pi on the home network using the service it advertises.
- Add a channel selector and show the position of the blinds.
- Show an error message when the server does not answer. Today the app only prints the error to the log.
- Update the Gradle version and the target Android version of the app.
- Add tests for the code that builds the requests.

## Month 5. Voice control and home automation

At the end of this month, the blinds work from a voice assistant, as in my first plan.

- Build the Alexa interface from the first plan.
- Publish the blinds over MQTT so that a home automation system can control them.
- Add a small web page on the Pi with the same three buttons, for a device without the app.

## Month 6. Reliability, documents and release

At the end of this month, another person can build the same setup from the repository.

- Measure how many repeats and which transmitter power give a reliable press at a distance, and set the defaults from that.
- Write the hardware guide with the parts list and the wiring diagram.
- Write the guide for a new remote, from the first recording to the stored codes.
- Package the Pi code so that one command installs it.
- Tag version 1.0.

## Out of scope

I do not use machine learning, and the decoder uses fixed rules on pulse lengths. I do not use data of other people.
