# RPi_GPIOZERO_mock.py
# Mock gpiozero.LED class for use on non-Raspberry Pi systems

class LED:
    def __init__(self, pin):
        print(f"[MOCK] LED initialized on pin {pin}")
        self.pin = pin
        self.state = False

    def on(self):
        self.state = True
        print(f"[MOCK] LED on pin {self.pin} turned ON")

    def off(self):
        self.state = False
        print(f"[MOCK] LED on pin {self.pin} turned OFF")