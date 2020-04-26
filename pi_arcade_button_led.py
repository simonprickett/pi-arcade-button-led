import RPi.GPIO as GPIO
import signal
import sys
import time

# Definitions
BUTTON_PIN = 19
LED_PIN = 26
counter = 0

# Setup pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn off the LED at shutdown and clean up.
def shutdown(signal, frame):
  GPIO.output(LED_PIN, False)
  GPIO.cleanup()
  sys.exit(0)

# Handles button presses.
def button_press(channel):
  global counter

  if (GPIO.input(channel) == False):
    counter = counter + 1
    print("Counter: " + str(counter))

    for n in range(0, counter):
      time.sleep(0.5)
      GPIO.output(LED_PIN, True)
      time.sleep(0.5)
      GPIO.output(LED_PIN, False)

# Add button press handler.
GPIO.add_event_detect(BUTTON_PIN, edge = GPIO.BOTH, callback = button_press, bouncetime = 300)

# Main entry point.
signal.signal(signal.SIGINT, shutdown)

while True:
  time.sleep(1)
