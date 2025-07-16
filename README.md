# Pico-ade-Machine
A physical pico 8 machine with 17 push buttons, 2 joysticks, Pi pico zero 2 w, tft display and 3 orpheus picos.  

# CAD MODEL
Fitting everything without over-modeling it, thi was done so it-s tiny enough to be lightweight and have a fast 3d printing. You can always download the Fusion project file and modify as you wish.

<img width="1360" height="606" alt="CASE EXPLANATION" src="https://github.com/user-attachments/assets/aa915491-a15e-4a8e-8085-dac4cc6915f6" />

<img width="812" height="609" alt="image" src="https://github.com/user-attachments/assets/d933e1a8-4980-4493-b57e-51855702c6a8" />

# WIRING DIAGRAM 
Here's the wiring diagram
![Uploading Captura de pantalla 2025-07-14 214849.png…]()

# SOFTWARE

In the repo, there are two scripts that need to be on the orpheus pico. left.py needs to be on the orpheus pico that is only connected to a orpheus pico, and code.py needs to be on the pico that is connected to an orpheus pico and the pi zero 2w.

CircuitPython should be flashed onto the picos.

There is only one script for the raspberry pi zero 2w, which is for receiving controller inputs.

The display and speaker is powered by drivers. 

Here is the link to the installer script ![DOWNLOAD SCRIPT HERE](https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/i2samp.py)

There is a guide to how to install the script ![here](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/raspberry-pi-usage)

As for the display, it's another adafruit script. 

Clone the ![repo](https://github.com/adafruit/Raspberry-Pi-Installer-Scripts)

And run pitft-fbcp.py with sudo. 

For the first option, hit 6
For the second option, hit 2
For the third option, hit 1 or 3, ( run the script again with the other if it is upside down)
For the last option, hit 0.

As for parsing the controls, run the controls-helper.py to accept input. Add the line:

sudo python3 /path/to/controls-helper.py &

That should be all the software necessary.
# CARDBOARD CASE 
Due to taking to long on making the CAD, we didn't got to 3d print it, but that doesn't mean it's over, it can also mean diy + art!

![Imagen de WhatsApp 2025-07-14 a las 08 08 54_6958069a](https://github.com/user-attachments/assets/5b81e838-f8ab-4fb0-bcf0-44e3fde95a7b)

We used some craftsy inspired hackclub vibes and logos! and maybe a hidden orpheus somewhere hehe.

You can DM us in Slack if you have any questions/suggestions/feedback/

[Check out the Demo](https://www.youtube.com/watch?v=qOujK8my25s&feature=youtu.be)!1

