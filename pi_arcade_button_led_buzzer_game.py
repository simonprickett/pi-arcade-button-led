import RPi.GPIO as GPIO
import random
import signal
import sys
import time

# Definitions
BUTTON_PIN = 19
LED_PIN = 26
BUZZER_PIN = 13
counter = 0
trigger_number = 0

# Setup pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Get a random number that the game ends at.
def get_random_number():
  r = random.randint(1, 5)
  print("Random: " + str(r))
  return r

# Turn off the LED at shutdown and clean up.
def shutdown(signal, frame):
  GPIO.output(LED_PIN, False)
  GPIO.output(BUZZER_PIN, False)
  GPIO.cleanup()
  sys.exit(0)

# Handles button presses.
def button_press(channel):
  global counter
  global trigger_number

  if (GPIO.input(channel) == False):
    counter = counter + 1
    print("Counter: " + str(counter))

    if counter == trigger_number:
      # Game over!
      for n in range(0, 5):
        time.sleep(0.1)
        GPIO.output(LED_PIN, True)
        GPIO.output(BUZZER_PIN, True)
        time.sleep(0.1)
        GPIO.output(LED_PIN, False)
        GPIO.output(BUZZER_PIN, False)

      # Get a new random number for next game, reset counter.
      trigger_number = get_random_number()
      counter = 0
    else:
      # Game continues, flash the LED.
      for n in range(0, counter):
        time.sleep(0.3)
        GPIO.output(LED_PIN, True)
        time.sleep(0.3)
        GPIO.output(LED_PIN, False)

# Set the first random end point.
trigger_number = get_random_number()

# Add button press handler.
GPIO.add_event_detect(BUTTON_PIN, edge = GPIO.BOTH, callback = button_press, bouncetime = 300)

# Main entry point.
signal.signal(signal.SIGINT, shutdown)

while True:
  time.sleep(1)
