import time
import board
import digitalio
import busio

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

def init_button(pin):
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

    return btn

button_pins = [board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP11, board.GP9]

button_byte = []

for pin in button_pins:
    button_byte.append(init_button(pin))

while True:
    try:
        state = 0
        for i, button in enumerate(button_byte):
            #print(f"{i}:{button.value}", end="|")
            if not button.value:  # Pressed = 1
                state = state | (1 << i)
        data = bytes([state & 0xFF, (state >> 8) & 0xFF])
        uart.write(data) #send two bytes, lsb first.
        time.sleep(0.01)
    except KeyboardInterrupt:
        break
