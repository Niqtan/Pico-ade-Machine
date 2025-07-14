# Pico-8 cartridge code

#Put this in boot.py

import time
#The storage library allows for control over the filesystem
import storage
# The USB-CDC allows for USB serial console (REPL console)
import usb-cdc
#  The MSC stands for mass storage class which us control whether the PICO shows up as a USB flash drive
import usb_msc

#For general purpose access to each pin on the Orpheus
import board

#For using digital logic and driving GPIOs
import digitalio

"""
TO do list:
- Figure how to store games in the pico_8_UART
    - Enable USB mass storage
- Transmit it through UART
"""

def storage():
    storage.remount("/", readonly=False)
    #Use USB-MSC in order to store the devices' games
    usb_msc.enable(storage_devices=[storage.getmount("/")], readonly=False)
    
def send_pico_file(uart):
    #Write the PICO-8 file using UART to the Orpheus for storage
    with open("/mygame.p8.png", "rb") as game_file:
        data = game_file.read()
        uart.write(data)

def main():
    storage()
    uart = busio.UART(board.GP0, board.GP1, baudrate=115200)
    send_pico_file(uart)
    
if __name__ == "__main__":
    main()
    
