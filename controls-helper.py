#!/usr/bin/env python3

import serial
import uinput
import time

# --- UART Configuration ---
UART_PORT = "/dev/serial0"  # GPIO UART on Pi Zero
BAUD_RATE = 9600

# --- Initialize UART ---
ser = serial.Serial(UART_PORT, baudrate=BAUD_RATE, timeout=1)

# --- Define 16 Virtual Buttons ---
button_events = [
    uinput.BTN_0, uinput.BTN_1, uinput.BTN_2, uinput.BTN_3,
    uinput.BTN_4, uinput.BTN_5, uinput.BTN_6, uinput.BTN_7,
    uinput.BTN_8, uinput.BTN_9, uinput.BTN_A, uinput.BTN_B,
    uinput.BTN_C, uinput.BTN_X, uinput.BTN_Y, uinput.BTN_Z,
]

# --- Create Virtual Joystick Device ---
device = uinput.Device(button_events)

print("✅ Virtual joystick created. Waiting for serial data...")

# --- Main Loop ---
while True:
    data = ser.read(4)
    if len(data) != 4:
        continue  # Incomplete packet

    # Combine bytes into 2 button state words (16-bit each)
    pico_a_state = data[0] | (data[1] << 8)
    pico_b_state = data[2] | (data[3] << 8)

    # Combine into a single 16-bit state
    combined = pico_a_state | (pico_b_state << 8)

    # Update virtual buttons
    for i in range(16):
        state = (combined >> i) & 1
        device.emit(button_events[i], state)

    time.sleep(0.01)  # Throttle loop slightly
