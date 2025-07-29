# RPi_GPIO_mock.py
class GPIO:
    BOARD = 'BOARD'
    OUT = 'OUT'
    LOW = 0
    HIGH = 1

    @staticmethod
    def setmode(mode):
        print(f"GPIO setmode({mode})")

    @staticmethod
    def setup(pin, mode):
        print(f"GPIO setup(pin={pin}, mode={mode})")

    @staticmethod
    def output(pin, state):
        print(f"GPIO output(pin={pin}, state={state})")

    @staticmethod
    def cleanup():
        print("GPIO cleanup()")