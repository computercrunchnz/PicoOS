#this script is exclusive to the personal version of PicoOS, 
#make sure lights are plugged into the Pico AND ALWAYS USE A RESISTOR 
#GP13 (white), GP9 (white2), GP5 (red), GP1 (green), GP18 (blue), GP22 (yellow), GP25 (green2)
from machine import Pin, Timer
import _thread
import sys
import time

run = False

print("Welcome to PicoOS SmartLight")
print("GP13 (white), GP9 (white2), GP5 (red), GP1 (green), GP18 (blue), GP22 (yellow), GP25 (green2)")
print("ALWAYS USE RESISTORS")

white1 = Pin(13, Pin.OUT) 
white2 = Pin(9, Pin.OUT)
red = Pin(5, Pin.OUT)
green = Pin(1, Pin.OUT)
blue = Pin(18, Pin.OUT)
yellow = Pin(22, Pin.OUT)
green2 = Pin(25, Pin.OUT)
    
green2.value(1)

time.sleep(0.10)

green2.value(0)

time.sleep(0.10)

green2.value(1)

time.sleep(0.10)

white1.value(1)

white2.value(1)
red.value(0)
green.value(0)
green2.value(0)
blue.value(0)
yellow.value(0)

def onall():
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    
    time.sleep(1)
    
    white1.value(1)
    white2.value(1)
    red.value(1)
    green.value(1)
    green2.value(1)
    blue.value(1)
    yellow.value(1)

def onw():
    time.sleep(1)
    
    white1.value(1)
    white2.value(1)
    
def onr():
    time.sleep(1)
    
    red.value(1)
    
def ong():
    time.sleep(1)
    
    green.value(1)
    green2.value(1)
    
def onb():
    time.sleep(1)
    
    blue.value(1)
    
def ony():
    time.sleep(1)
    
    yellow.value(1)

def offall():
    time.sleep(1)
    
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    
def offw():
    time.sleep(1)
    
    white1.value(0)
    white2.value(0)
    
def offr():
    time.sleep(1)
    
    red.value(0)

def offg():
    time.sleep(1)
    
    green.value(0)
    green2.value(0)
    
def offb():
    time.sleep(1)
    
    blue.value(0)
    
def offy():
    time.sleep(1)
    
    yellow.value(0)
    
def flashall():
    while run == True:
        white1.value(0)
        white2.value(0)
        red.value(0)
        green.value(0)
        green2.value(0)
        blue.value(0)
        yellow.value(0)
        
        time.sleep(0.15)
        
        white1.value(1)
        white2.value(1)
        red.value(1)
        green.value(1)
        green2.value(1)
        blue.value(1)
        yellow.value(1)
        
        time.sleep(0.15)
        
def strobe():
    while run == True:
        white1.value(0)
        white2.value(0)
        red.value(0)
        green.value(0)
        green2.value(0)
        blue.value(0)
        yellow.value(0)
        
        time.sleep(0.05)
        
        white1.value(1)
        white2.value(1)
        red.value(1)
        green.value(1)
        green2.value(1)
        blue.value(1)
        yellow.value(1)
        
        time.sleep(0.05) 
    
def flashstop():
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    
def scrollfast():
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    while run == True:
        white1.value(1)
        time.sleep(0.1)
        white1.value(0)
        white2.value(1)
        time.sleep(0.1)
        white2.value(0)
        red.value(1)
        time.sleep(0.1)
        red.value(0)
        green.value(1)
        green2.value(1)
        time.sleep(0.1)
        green.value(0)
        green2.value(0)
        blue.value(1)
        time.sleep(0.1)
        blue.value(0)
        yellow.value(1)
        time.sleep(0.1)
        yellow.value(0)
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
        
def scrollslow():
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    while run == True:
        white1.value(1)
        time.sleep(0.2)
        white1.value(0)
        white2.value(1)
        time.sleep(0.2)
        white2.value(0)
        red.value(1)
        time.sleep(0.2)
        red.value(0)
        green.value(1)
        green2.value(1)
        time.sleep(0.2)
        green.value(0)
        green2.value(0)
        blue.value(1)
        time.sleep(0.2)
        blue.value(0)
        yellow.value(1)
        time.sleep(0.2)
        yellow.value(0)
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    
def start5min():
    time.sleep(1)
    white1.value(1)
    white2.value(1)
    red.value(1)
    green.value(1)
    green2.value(1)
    blue.value(1)
    yellow.value(0)
    print("5 Minutes Remaining")
    time.sleep(60)
    white1.value(1)
    white2.value(1)
    red.value(1)
    green.value(1)
    green2.value(1)
    blue.value(0)
    yellow.value(0)
    print("4 Minutes Remaining")
    time.sleep(60)
    white1.value(1)
    white2.value(1)
    red.value(1)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    print("3 Minutes Remaining")
    time.sleep(60)
    white1.value(1)
    white2.value(1)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    print("2 Minutes Remaining")
    time.sleep(60)
    white1.value(1)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    print("1 Minute Remaining")
    time.sleep(55)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("0")
    time.sleep(1)
    print("Start Completed!")
    white1.value(0)
    
def start3min():
    time.sleep(1)
    white1.value(1)
    white2.value(1)
    red.value(1)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    print("3 Minutes Remaining")
    time.sleep(60)
    white1.value(1)
    white2.value(1)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    print("2 Minutes Remaining")
    time.sleep(60)
    white1.value(1)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    print("1 Minute Remaining")
    time.sleep(55)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("0")
    time.sleep(1)
    print("Start Completed!")
    white1.value(0)
    
def traffic():
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(1)
    green2.value(1)
    blue.value(0)
    yellow.value(0)
    
    time.sleep(6)
    
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(1)
    
    time.sleep(4)
    
    white1.value(0)
    white2.value(0)
    red.value(1)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    
    time.sleep(10)
    
    white1.value(0)
    white2.value(0)
    red.value(0)
    green.value(0)
    green2.value(0)
    blue.value(0)
    yellow.value(0)
    
while True:

    cmd=input("Command: ")
    if cmd=="on.all":
        _thread.start_new_thread(onall, ())
    elif cmd=="on.white":
        _thread.start_new_thread(onw, ())
    elif cmd=="on.red":
        _thread.start_new_thread(onr, ())
    elif cmd=="on.green":
        _thread.start_new_thread(ong, ())
    elif cmd=="on.blue":
        _thread.start_new_thread(onb, ())
    elif cmd=="on.yellow":
        _thread.start_new_thread(ony, ())
    elif cmd=="off.all":
        _thread.start_new_thread(offall, ())
    elif cmd=="off.white":
        _thread.start_new_thread(offw, ())
    elif cmd=="off.red":
        _thread.start_new_thread(offr, ())
    elif cmd=="off.green":
        _thread.start_new_thread(offg, ())
    elif cmd=="off.blue":
        _thread.start_new_thread(offb, ())
    elif cmd=="off.yellow":
        _thread.start_new_thread(offy, ())
    elif cmd=="flash.all":
        run = True
        _thread.start_new_thread(flashall, ())
    elif cmd=="flash.stop":
        run = False
        time.sleep(1)
        _thread.start_new_thread(flashstop, ())
    elif cmd=="strobe.all":
        run = True
        _thread.start_new_thread(strobe, ())
    elif cmd=="strobe.stop":
        run = False
        time.sleep(1)
        _thread.start_new_thread(flashstop, ())
    elif cmd =="scroll.fast":
        run = True
        time.sleep(1)
        _thread.start_new_thread(scrollfast, ())
    elif cmd =="scroll.slow":
        run = True
        time.sleep(1)
        _thread.start_new_thread(scrollslow, ())
    elif cmd =="scroll.stop":
        run = False
        time.sleep(1)
    elif cmd=="start.5min":
        run = True
        _thread.start_new_thread(start5min, ())
    elif cmd=="start.3min":
        run = True
        _thread.start_new_thread(start3min, ())
    elif cmd=="start.stop":
        machine.reset()
    elif cmd=="about":
        print("CC SmartLight 2.0")
        print("Made by Computer Crunch in 2022")
        print("Made for Raspberry Pi Pico")
    elif cmd=="hardware":
        print("Device: Raspberry Pi Pico")
        print("Processor: Dual-Core RP 2040 @ 133 MHz")
        print("Ram: 264KB")
        print("Storage: 128MB")
    elif cmd=="software":
        print("CC LightOS 2.0")
        print("Released 23rd January 2022")
        print("Kernel Version: 2.0")
    elif cmd=="trafficlight":
        _thread.start_new_thread(traffic, ())
    elif cmd=="restart":
        white1.value(0)
        white2.value(0)
        red.value(0)
        green.value(0)
        green2.value(0)
        blue.value(0)
        yellow.value(0)
        print("Restarting in 3 Seconds")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Restarting Now...")
        machine.reset()
    elif cmd=="exit":
        break
    else:
        print("Invalid Command")
