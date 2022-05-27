import time

import sys

from machine import Pin

import machine

import math

import os

import utime

import _thread

led = Pin(25, Pin.OUT)

led.value(1)

time.sleep(0.10)

led.value(0)

time.sleep(0.10)

led.value(1)

time.sleep(0.10)

def disp():
    from lcd_pico import *
    setupLCD()
    displayString(1,0,"WELCOME")
    displayString(2,0,"TO")
    longDelay(4000)
    displayString(1,0,"PicoOS")
    displayString(2,0,"/|CMG LTD|\ ")
    longDelay(4000)
    while(True):
        displayString(1,0,"INDUSTRY")
        displayString(2,0,"VERSION")
        longDelay(1000)
        clearScreen()
        longDelay(500)
                
_thread.start_new_thread(disp, ())

print("Welcome to PicoOS 1 Industrial!")
print("Currently under development.")
print("Report any issues to computercrunchnz+picoos1@gmail.com")

namefile = open("name.txt", "r")
name = namefile.read()
namefile.close()

while True:
    cmd = input("> ")
    print()
    if cmd == "about":
        print("About")
        print("PicoOS 1.0 Industrial Alpha _")
        print("Made by Crunch Media Group Software")
        print("This PicoPC belongs to " + name + ".")
        print("Report any issues to computercrunchnz+picoos1@gmail.com")
    elif cmd == "update":
        print("Update")
        print("To check for updates, go to the PicoOS git repository at https://github.com/computercrunchnz/PicoOS/releases.")
    elif cmd == "calculator":
        print("Calculator")
        calc = 1
        while calc == 1:
            fn = input("Function: ")
            if fn == "exit":
                calc = 0
            elif fn == "add":
                n1 = input("First Number: ")
                n2 = input("Second Number: ")
                n1 = int(n1)
                n2 = int(n2)
                nf = n1+n2
                print("Result: " + str(nf))
            elif fn == "subtract":
                n1 = input("First Number: ")
                n2 = input("Second Number: ")
                n1 = int(n1)
                n2 = int(n2)
                nf = n1-n2
                print("Result: " + str(nf))
            elif fn == "multiply":
                n1 = input("First Number: ")
                n2 = input("Second Number: ")
                n1 = int(n1)
                n2 = int(n2)
                nf = n1*n2
                print("Result: " + str(nf))
            elif fn == "divide":
                n1 = input("First Number: ")
                n2 = input("Second Number: ")
                n1 = int(n1)
                n2 = int(n2)
                nf = n1/n2
                print("Result: " + str(nf))
            elif fn == "exponent":
                n1 = input("Number: ")
                n2 = input("Exponent: ")
                n1 = int(n1)
                n2 = int(n2)
                nf = pow(n1, n2)
                print("Result: " + str(nf))
            elif fn == "sqroot":
                n1 = input("Number: ")
                n1 = int(n1)
                nf = math.sqrt(n1)
                print("Result: " + str(nf))
            elif fn == "tobase2":
                n1 = input("Number: ")
                n1 = int(n1)
                nf = math.log2(n1)
                print("Result: " + str(nf))
            elif fn == "tobase10":
                n1 = input("Number: ")
                n1 = int(n1)
                nf = math.log10(n1)
                print("Result: " + str(nf))
    elif cmd == "writer":
        print("Writer")
        file = input("File Name - remember extension: ")
        writing = open(file, "w")
        towrite = input("Write here: ")
        writing.write(towrite)
        writing.close()
    elif cmd == "reader":
        print("Reader")
        file = input
        file = input("File Name - remember extension: ")
        reading = open(file, "r")
        print()
        print(reading.read())
        reading.close()
    elif cmd == "settings":
        print("Settings")
        setting = input("What setting do you want to change? ")
        if setting == "exit":
            print("Okay")
        elif setting == "led.on":
            led.value(1)
            print("Done!")
        elif setting == "led.off":
            led.value(0)
            print("Done")
        elif setting == "led.status":
            print("LED status: " + str(led.value()))
        elif setting == "set-rtc":
            year = input("Year: ")
            month = input("Month: ")
            wday = input("Day of the week (0=mon, 1=tue, 2=wed, 3=thu, 4=fri, 5=sat, 6=sun):")
            day = input("Day: ")
            hour = input("Hour: ")
            minute = input("Minute: ")
            machine.RTC().datetime((int(year), int(month), int(day), int(wday), int(hour), int(minute), 0, 0))
    elif cmd == "help":
        print("Help")
        print("COMMANDS:")
        print("'about' - About PicoOS")
        print("'update' - Where to update PicoOS")
        print("'calculator' - Calculator")
        print("'writer' - Text Editor")
        print("'reader' - Document Reader")
        print("'settings' - Settings")
        print("'maths-quiz' - A Maths Quiz creator with multiple levels")
        print("'war-scenario' - A war scenario generator")
        print("'random-sentence' - A random sentence generator")
        print("'temp' - Check the temperature in celcius")
        print("'ls' - Lists the files")
        print("'del' - Delete a file")
        print("'setup' - Setup PicoOS")
        print("'help' - Help")
        print("'exit' - Exit PicoOS")
        hs = input("Do you need commands for in an app? ")
        if hs == "no":
            print("Okay")
        elif hs == "calculator":
            print("Calculator Help")
            print("FUNCTIONS:")
            print("'add' - Add")
            print("'subtract' - Subtract")
            print("'multiply' - Multiply")
            print("'divide' - Divide")
            print("'exponent' - Calculate exponents")
            print("'sqroot' - Square root of a number")
            print("'tobase2' - Convert number to base 2")
            print("'tobase10' - Convert number to base 10")
            print("'exit' - Exit the calculator")
        elif hs == "writer":
            print("Writer Help")
            print("HOW TO USE:")
            print("1. Enter Writer")
            print("2. Choose a file name with an extension (example - hi.txt)")
            print("3. Write the contents of the file")
        elif hs == "writer":
            print("Reader Help")
            print("HOW TO USE:")
            print("1. Enter Reader")
            print("2. Type in the name a file you want to view with an extension (example - hi.txt)")
            print("3. Read the contents of the file")
        elif hs == "settings":
            print("Settings Help")
            print("SETTINGS:")
            print("'led.on' - Turn the board LED on")
            print("'led.off' - Turn the board LED off")
            print("'led.status' - Check the status of the board LED")
            print("'set-rtc' - Set the onboard clock")
            print("'exit' - Exit Settings")
    elif cmd == "exit":
        bai = input("Exit PicoOS Y/N: ")
        if bai == "Y":
            print("Exiting PicoOS...")
            led.value(0)
            sys.exit()
        else:
            print("Exit Aborted.")
    elif cmd == "maths-quiz":
        from random import randint

        lev = input("Level: E, M or H: ")

        q = 0

        nq = 1

        while q < 100:
          if lev == "H":
            n1 = randint(1, 1000)
            n2 = randint(1, 1000)
            t = randint(1, 4)
            if t == 1:
                print("Q",nq, ". What is ", n1, "+", n2, "?")
                q = q + 1
                nq = nq + 1 
            elif t == 2:
                print("Q",nq, ". What is ", n1, "-", n2, "?")
                q = q + 1
                nq = nq + 1
            elif t == 3:
                print("Q", nq, ". What is ", n1, "*", n2, "?")
                q = q + 1
                nq = nq + 1
            elif t == 4:
                print("Q", nq, ". What is ", n1, "/", n2, "?")
                q = q + 1
                nq = nq + 1
          elif lev == "M":
            n1 = randint(1, 100)
            n2 = randint(1, 100)
            t = randint(1, 4)
            if t == 1:
                print("Q",nq, ". What is ", n1, "+", n2, "?")
                q = q + 1
                nq = nq + 1 
            elif t == 2:
                print("Q",nq, ". What is ", n1, "-", n2, "?")
                q = q + 1
                nq = nq + 1
            elif t == 3:
                print("Q", nq, ". What is ", n1, "*", n2, "?")
                q = q + 1
                nq = nq + 1
            elif t == 4:
                print("Q", nq, ". What is ", n1, "/", n2, "?")
                q = q + 1
                nq = nq + 1
          elif lev == "E":
            n1 = randint(1, 10)
            n2 = randint(1, 10)
            t = randint(1, 4)
            if t == 1:
                print("Q",nq, ". What is ", n1, "+", n2, "?")
                q = q + 1
                nq = nq + 1 
            elif t == 2:
                print("Q",nq, ". What is ", n1, "-", n2, "?")
                q = q + 1
                nq = nq + 1
            elif t == 3:
                print("Q", nq, ". What is ", n1, "*", n2, "?")
                q = q + 1
                nq = nq + 1
            elif t == 4:
                print("Q", nq, ". What is ", n1, "/", n2, "?")
                q = q + 1
                nq = nq + 1
    elif cmd == "war-scenario":
        from random import randint

        q = 0

        nq = 1

        ctry = randint(1, 18)

        ctry2 = randint(1, 18)

        if ctry == 1:
            country = "New Zealand"
        elif ctry == 2:
            country = "Australia"
        elif ctry == 3:
            country = "Austria"
        elif ctry == 4:
            country = "South Africa"
        elif ctry == 5:
            country = "Russia"
        elif ctry == 6:
            country = "Ukraine"
        elif ctry == 7:
            country = "UK"
        elif ctry == 8:
            country = "France"
        elif ctry == 9:
            country = "US"
        elif ctry == 10:
            country = "India"
        elif ctry == 11:
            country = "China"
        elif ctry == 12:
            country = "Fiji"
        elif ctry == 13:
            country = "Brazil"
        elif ctry == 14:
            country = "Canada"
        elif ctry == 15:
            country = "Mexico"
        elif ctry == 16:
            country = "Singapore"
        elif ctry == 17:
            country = "Hong Kong"
        elif ctry == 18:
            country = "Taiwan"

        if ctry2 == 1:
            country2 = "New Zealand"
        elif ctry2 == 2:
            country2 = "Australia"
        elif ctry2 == 3:
            country2 = "Austria"
        elif ctry2 == 4:
            country2 = "South Africa"
        elif ctry2 == 5:
            country2 = "Russia"
        elif ctry2 == 6:
            country2 = "Ukraine"
        elif ctry2 == 7:
            country2 = "UK"
        elif ctry2 == 8:
            country2 = "France"
        elif ctry2 == 9:
            country2 = "US"
        elif ctry2 == 10:
            country2 = "India"
        elif ctry == 11:
            country2 = "China"
        elif ctry2 == 12:
            country2 = "Fiji"
        elif ctry2 == 13:
            country2 = "Brazil"
        elif ctry2 == 14:
            country2 = "Canada"
        elif ctry2 == 15:
            country2 = "Mexico"
        elif ctry2 == 16:
            country2 = "Singapore"
        elif ctry2 == 17:
            country2 = "Hong Kong"
        elif ctry2 == 18:
            country2 = "Taiwan"
            
        type = randint(1,9)

        if type == 1:
            t = "is starting a Nuclear war with"
        elif type == 2:
            t = "is starting a war with"
        elif type == 3:
            t = "is invading"
        elif type == 4:
            t = "is pooping on"
        elif type == 5:
            t = "is bombing"
        elif type == 6:
            t = "is punching"
        elif type == 7:
            t = "is starting a civil war with"
        elif type == 8:
            t = "is starting a cyber war with"
        elif type == 9:
            t = "is italianing with"

        print(country, t, country2, ".")

    elif cmd == "random-sentence":
        from random import randint
        
        q = 0

        nq = 1

        word = randint(1, 18)

        word2 = randint(1, 18)

        word3 = randint(1, 18)

        if word == 1:
            w = "Mac"
        elif word == 2:
            w = "Apple"
        elif word == 3:
            w = "Microsoft"
        elif word == 4:
            w = "Poop"
        elif word == 5:
            w = "Ur Mum"
        elif word == 6:
            w = "Eggs"
        elif word == 7:
            w = "Bomb"
        elif word == 8:
            w = "Speaker"
        elif word == 9:
            w = "Cat"
        elif word == 10:
            w = "Dog"
        elif word == 11:
            w = "Kitten"
        elif word == 12:
            w = "Meow"
        elif word == 13:
            w = "Puppy"
        elif word == 14:
            w = "Python"
        elif word == 15:
            w = "Message"
        elif word == 16:
            w = "Macintosh"
        elif word == 17:
            w = "Sad"
        elif word == 18:
            w = "News"

        if word2 == 1:
            w2 = "is"
        elif word2 == 2:
            w2 = "are"
        elif word2 == 3:
            w2 = "is doing"
        elif word2 == 4:
            w2 = "throwing"
        elif word2 == 5:
            w2 = "war"
        elif word2 == 6:
            w2 = "calendared"
        elif word2 == 7:
            w2 = "calculated"
        elif word2 == 8:
            w2 = "did"
        elif word2 == 9:
            w2 = "ate"
        elif word2 == 10:
            w2 = "crunch"
        elif word == 11:
            w2 = "reading"
        elif word2 == 12:
            w2 = "is typing"
        elif word2 == 13:
            w2 = "is editing"
        elif word2 == 14:
            w2 = "streaming live to"
        elif word2 == 15:
            w2 = "is switching"
        elif word2 == 16:
            w2 = "listened"
        elif word2 == 17:
            w2 = "took a photo of"
        elif word2 == 18:
            w2 = "found"

        if word3 == 1:
            w3 = "1+1."
        elif word3 == 2:
            w3 = "videos."
        elif word3 == 3:
            w3 = "pooping."
        elif word3 == 4:
            w3 = "words."
        elif word3 == 5:
            w3 = "Ur Mum."
        elif word3 == 6:
            w3 = "processors."
        elif word3 == 7:
            w3 = "moved."
        elif word3 == 8:
            w3 = "food."
        elif word3 == 9:
            w3 = "computer."
        elif word3 == 10:
            w3 = "terminal."
        elif word == 11:
            w3 = "starting a war."
        elif word3 == 12:
            w3 = "doing maths."
        elif word3 == 13:
            w3 = "messaging."
        elif word3 == 14:
            w3 = "twitch."
        elif word3 == 15:
            w3 = "googling."
        elif word3 == 16:
            w3 = "writing."
        elif word3 == 17:
            w3 = "plants."
        elif word3 == 18:
            w3 = "Window."

        print(w, w2, w3)
        
    elif cmd == "time":
        tm = machine.RTC().datetime()
        year = tm[0]
        month = tm[1]
        day = tm[2]
        hour = tm[4]
        minute = tm[5]
        second = tm[6]
        print("Date: " + str(day) + "/" + str(month) + "/" + str(year))
        print("Time: " + str(hour) + ":" + str(minute) + ":" + str(second))
    elif cmd == "reboot":
        print("Rebooting...")
        led.value(0)
        machine.reset()
    elif cmd == "temp":
        sensor_temp = machine.ADC(4)
        conversion_factor = 3.3 / (65535)
        reading = sensor_temp.read_u16() * conversion_factor 
        temperature = 27 - (reading - 0.706)/0.001721
        print("Temperature: " + str(temperature))
    elif cmd == "ls":
        ls = os.listdir()
        print(ls)
    elif cmd == "del":
        todel = input("File name: ")
        os.remove(todel)
    elif cmd == "setup":
        import setup
    
    #INSERT APP HERE
    
    
    
    print()