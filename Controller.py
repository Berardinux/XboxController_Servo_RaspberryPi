import evdev

for event in evdev.InputDevice("/dev/input/event0").read_loop():
  if event.type == evdev.ecodes.EV_ABS:
    if event.code == evdev.ecodes.ABS_X:
      print(f"Left Analog stick: {event.value}")