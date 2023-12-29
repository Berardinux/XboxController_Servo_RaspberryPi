import evdev
import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
servo.start(0)

def map_value(value, in_min, in_max, out_min, out_max):
  return np.interp(value, [in_min, in_max], [out_min, out_max])

controllerInput = evdev.InputDevice("/dev/input/event0")

for event in controllerInput.read_loop():
  if event.type == evdev.ecodes.EV_ABS:
    if event.code == evdev.ecodes.ABS_X:
      angle = round(map_value(event.value, 0, 65535, 2, 12))
      print(angle)
      servo.ChangeDutyCycle(angle)