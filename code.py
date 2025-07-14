import board

import digitalio
import analogio
import time

def uart_init():
    uart = busio.UART(board.TX, board.RX, baudrate=9600)

    uart.write("Hello from Orpheus 1\n")
    print("Sent a message\n")
    time.sleep(0.5)

def joystick_init():
    joystick_dictionary = {
        "x": analogio.AnalogIn(board.A2), #A.K.A GPIO 28
        "y": analogio.AnalogIn(board.A1), #A.K.A GPIO 27
        # Turn on or off buttons
        "sw": digitalio.DigitalInOut(board.GP15),
    }

    joystick_dictionary["sw"].direction = digitalio.Direction.INPUT
    joystick_dictionary["sw"].pull = digitalio.Pull.UP

    return joystick_dictionary

def joystick_control(joystick_dictionary):
    pressed = not joystick_dictionary["sw"].value

    joystick_direction(joystick_dictionary["x"], joystick_dictionary["y"])
    time.sleep(0.5)
def joystick_direction(x, y):
    # Logic for adjusting the direction according to the data using conditionals
    #Reminder max is 65535 which basically means 3.3V
    # If its 65535 that means that it is deadset on one direction
    #ex,,, 32768 = Neutral

    #Initial calibration
    min_val = 65535
    max_val = 0

    print("Calibrate the joystick")
    start_time = time.monotonic()

    while time.monotonic() - start_time < 3:
        x_val = x.value
        y_val = y.value

        x_min = min(min_val, x_val)
        x_max = max(max_val, x_val)
        y_min = min(min_val, y_val)
        y_max = max(max_val, y_val)

    x_center = x_max / 2
    y_center = y_max / 2

    print("Calibration Success!")
    print(f"X min: {x_min}, X max: {x_max}, Center: {x_center}")
    print(f"Y min: {y_min}, y max: {y_max}, Y-center: {y_center}")
        
        
    joystick_library = {
    "x_val": x_val
    "x_min": x_min,
    "x_max": x_max,
    "x_center": x_center,
    "y_val": y_val
    "y_min": y_min,
    "y_max": y_max,
    "y_center": y_center,
    }
    
    return joystick_library

def normalize_process(joystick_library):
    x_center = joystick_library["x_center"]
    x_min = joystick_library["x_min"]
    x_max = joystick_library["x_max"]

    y_center = joystick_library["y_center"]
    y_min = joystick_library["y_min"]
    y_max = joystick_library["y_max"]

    normalized_x = normalize(x_val, x_center, x_min, x_max)
    normalized_y = normalize(y_val, y_center, y_min, y_max)

    # Polish the rules
    x = apply_rules(normalized_x)
    y = apply_rules(normalized_y)

    print(f"Direction: X={x}, Y={y}")



def apply_rules(val, threshold=0.1):
    if val < threshold:
        return 0
    else:
        return val

def normalize(val, center, range_min, range_max):
    #Normalize the values from -1 to 1
    if val < center:
        return -1 * (center - val) / (center - range_min)
    else:
        return (val - center) / (range_max - center)

def keyboard_init():
    #Get it to print all of the state buttons
    #Get it to print all of the state buttons

    #R3 is when the joystick is pressed downwards

    keyboard = {
    "Select": digitalio.DigitalInOut(board.GP22),
    "X": digitalio.DigitalInOut(board.GP21),
    "Y": digitalio.DigitalInOut(board.GP17),
    "Z": digitalio.DigitalInOut(board.GP16),
    "C": digitalio.DigitalInOut(board.GP20),
    "A": digitalio.DigitalInOut(board.GP19),
    "B": digitalio.DigitalInOut(board.GP18),
    "R1": digitalio.DigitalInOut(board.GP9),
    "R2": digitalio.DigitalInOut(board.GP11),
    "R3": digitalio.DigitalInOut(board.GP26),
    }


    return keyboard

def get_button_state(keyboard):
    for key, name in keyboard.items():
        name.direction = digitalio.Direction.INPUT
        name.pull = digitalio.Pull.UP
        if name.value == 0:
            state = "pressed"
        else:
            state = "not pressed"
        print(f"{key} is set to {state}")
        time.sleep(0.5)

def main():
    print("Test Print")
    joystick_dictionary = joystick_init()
    joystick_library = joystick_control(joystick_dictionary)


    while True:
        normalize_process(joystick_library)
        #What should we do after getting the button state?
        #None yet so far

if __name__ == "__main__":
    main()# Write your code here :-)
