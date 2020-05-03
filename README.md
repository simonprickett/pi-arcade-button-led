# Raspberry Pi Arcade Button LED / Buzzer Demos

This repository contains some example code for building a Raspberry Pi project using an Adafruit LED Arcade button, a Raspberry Pi and optionally a buzzer.

## Shopping List

I used the following:

* [Adafruit Mini LED Arcade Button - 24mm Translucent Blue](https://www.adafruit.com/product/3432) (note the red and green versions of these won't work with the Pi as they need 5v, other colors are ok).
* Raspberry Pi 3 (but any model should do, I just had a 3 on hand).
* Piezo style buzzer, [got mine from Amazon](https://www.amazon.com/gp/product/B0727RGJLY/).
* Food container, the sort that you get fresh soup in.

## LED Button Counter Demo

The first demo I build uses the arcade button and its built in LED.  Whenever the button is pressed, a global variable is incremented and the LED flashes that many times.  The code for this is in `pi_arcade_button_led.py`.  This demo doesn't use the buzzer.

Click to watch a video demonstration and code walkthrough:

[![Video Thumbnail](https://img.youtube.com/vi/olSWVYz0dvE/0.jpg)](https://www.youtube.com/watch?v=olSWVYz0dvE)

## LED Button Counter Demo with Buzzer

This demo is exactly the same as the above, but the buzzer also sounds every time the LED turns on.  Code is in `pi_arcade_button_led_buzzer.py`.

## LED Button / Buzzer Game

This demo works a bit differently.  Again, every time the button is pressed, the LED will flash and a global counter is incremented.  This time, after a random number of button presses (1-5 in the demo), the buzzer will sound.

Imagine this as a game where the person that triggers the buzzer loses or has to do a forfeit, or maybe it's like a pass the parcel game where the person that triggers the buzzer is a winner!

After the buzzer has been triggered, a new random number is chosen and the game immediately restarts.

The code for this example is in `pi_arcade_button_led_buzzer_game.py`.

TODO I'll add a video demonstration and walkthrough for this...

## Running as a Service

TODO I'll add information about this.

