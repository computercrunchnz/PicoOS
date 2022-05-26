#This file is the stand alone code to run the LCD
#This is already incorperated into the main.py
#This MUST HAVE 'lcd_pico' on the pico as well

from lcd_pico import *
setupLCD()
displayString(1,0,"WELCOME")
displayString(2,0,"TO")
longDelay(4000)
displayString(1,0,"PicoOS")
displayString(2,0,"/|CMG LTD|\")
longDelay(4000)
while(True):
    displayString(1,0,"INDUSTRY")
    displayString(2,0,"VERSION")
    longDelay(1000)
    clearScreen()
    longDelay(500)
