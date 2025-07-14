import board
import busio
import digitalio
import analogio
import time
import machine

def uart_init():
    uart = busio.UART(board.TX, board.RX, baudrate=9600)

    uart.write("Hello from Orpheus 1\n")
    print("Sent a message\n")
    time.sleep(0.5)

def joystick_init():
    joystick_dictionary = {
        "x": analogio.AnalogIn(board.A0), #A.K.A GPIO 26
        "y": analogio.AnalogIn(board.A1), #A.K.A GPIO 27
        # Turn on or off buttons
        "sw": digitalio.DigitalInOut(board.GP15),
    }

    joystick_dictionary["sw"].direction = digitalio.Direction.INPUT
    joystick_dictionary["sw"].pull = digitalio.Pull.UP

    return joystick_dictionary

def joystick_control(joystick_dictionary):
    # Keep reading the values
    while True:
        VRx = joystick_dictionary["x"].read_u16()
        VRy = joystick_dictionary["y".read_u16()
        pressed = not joystick_dictionary["sw"].value


        # Adjust direction to accordingly to the data
        joystick_direction(VRx, VRy)

        time.sleep(0.5)
def joystick_direction(x, y):
    # Logic for adjusting the direction according to the data using conditionals
    #Reminder max is 65535 which basically means 3.3V
    # If its 65535 that means that it is deadset on one direction
    #ex,,, 32768 = Neutral

    #Initial calibration
    min = 65535
    max = 0

    print("Calibrate the joystick")
    start_time = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start_time) < 3000:
        x_data = x.read_u16()
        y_data = y.read_u16()
        x_min = min(min, x_data)
        x_max = max(max, x_data)
        y_min = min(min, y_data)
        y_max = max(max, y_data)

    x_center = x_data / 2
    y_center = y_data / 2

    print("Calibration Success!")
    print(f"X min: {x_min}, X max: {x_max}, Center: {x_center}")
    print(f"Y min: {y_min}, y max: {y_max}, Y-center: {y_center}")
    print()

    while True:
        normalized_x = normalize(x, center, min, max)
        normalized_y = normalize(y, center, min, max)

        #Polish the rules
        x = apply_rules(normalized_x)
        y = apply_rules(normalized_y)

        #After polishing, the VRx and VRy of the joystick should be adjusted accordingly now

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

    # Place the keys in dictionaries with their corresponding GPIOs
    keyboard = {
        "Select": digitalio.DigitalInOut(board.22),
        "X": digitalio.DigitalInOut(board.21),
        "Y": digitalio.DigitalInOut(board.17),
        "Z": digitalio.DigitalInOut(board.16),
        "C": digitalio.DigitalInOut(board.20),
        "A": digitalio.DigitalInOut(board.19),
        "B": digitalio.DigitalInOut(board.18),
        "R1": digitalio.DigitalInOut(board.9),
        "R2": digitalio.DigitalInOut(board.11),
        "R3": digitalio.DigitalInOut(board.26),
    }

    return keyboard

def get_button_state(keyboard):
    for key, name in keyboard.items():
    if key.value() == 0:
        state = "pressed"
    else:
        state = "not pressed"
    print(f"{name} is set to {state}")
    time.sleep(0.5)

def main():
    print("Test Print")
    joystick_dictionary = joystick_init()
    keyboard_dictionary = keyboard_init()

    while True:
        joystick_control(joystick_dictionary)
        get_button_state(keyboard_dictionary)
        #What should we do after getting the button state?
        #None yet so far

if __name__ == "__main__":
    main()# Write your code here :-)
