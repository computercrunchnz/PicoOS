import time

import sys

from machine import Pin

import machine

import math

import os

from sys import version

led = Pin(25, Pin.OUT)

led.value(1)

time.sleep(0.10)

led.value(0)

time.sleep(0.10)

led.value(1)

time.sleep(0.10)

led.value(0)

pin0 = Pin(0, Pin.OUT)
pin1 = Pin(1, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
pin3 = Pin(3, Pin.OUT)
pin4 = Pin(4, Pin.OUT)
pin5 = Pin(5, Pin.OUT)
pin6 = Pin(6, Pin.OUT)
pin7 = Pin(7, Pin.OUT)
pin8 = Pin(8, Pin.OUT)
pin9 = Pin(9, Pin.OUT)
pin10 = Pin(10, Pin.OUT)
pin11 = Pin(11, Pin.OUT)
pin12 = Pin(12, Pin.OUT)
pin13 = Pin(13, Pin.OUT)
pin14 = Pin(14, Pin.OUT)
pin15 = Pin(15, Pin.OUT)
pin16 = Pin(16, Pin.OUT)
pin17 = Pin(17, Pin.OUT)
pin18 = Pin(18, Pin.OUT)
pin19 = Pin(19, Pin.OUT)
pin20 = Pin(20, Pin.OUT)
pin21 = Pin(21, Pin.OUT)
pin26 = Pin(26, Pin.OUT)
pin27 = Pin(27, Pin.OUT)
pin28 = Pin(28, Pin.OUT)

osversion = "2.0"
osversionpostnote = ""

print("Welcome to PicoOS!")
print("Report any issues to computercrunchnz+picoos2@gmail.com")
print("Version: " + str(osversion) + " " + str(osversionpostnote))

namefile = open("name.txt", "r")
name = namefile.read()
namefile.close()


while True:
    cmd = input("> ")
    print()
    led.value(1)
    if cmd == "about":
        print("About")
        print("PicoOS " + str(osversion) + " " + str(osversionpostnote))
        print("Made by Crunch Media Group Software LTD")
        print("This PicoPC belongs to " + name + ".")
        print("Report any issues to computercrunchnz+picoos2@gmail.com")
        print("Micropython version: " + version)
    elif cmd == "update":
        print("Update")
        print("To download the latest version, go to the PicoOS git repository at https://github.com/computercrunchnz/PicoOS/.")
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
            print("Exiting Now")
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
        print("'clicker' - Cookie Clicker")
        print("'market-share' - OS Market Share (real time stock values coming soon)")
        print("'news-quiz' - News Quiz")
        print("'time' - Tells the time and date")
        print("'ls' - Lists the files")
        print("'del' - Delete a file")
        print("'setup' - Setup PicoOS")
        print("'run' - Run a program from another file")
        print("'pin-control' - Control GPIO Pins")
        print("'pin-viewer' - View GPIO Pin Values")
        print("'help' - Help")
        print("'reboot' - Restart PicoOS")
        print("'exit' - Exit PicoOS")
        hs = input("Do you need commands for in an app? ")
        if hs == "no":
            print("Okay")
        elif hs == "market-share":
            print("Market Share Help")
            print("SECTORS:")
            print("'desktop' - Desktop OS Market Share")
            print("'tablet' - Tablet OS Market Share")
            print("'mobile' - Mobile OS Market Share")
        elif hs == "clicker":
            print("Cookie Clicker Help")
            print("COMMANDS:")
            print("'Enter Key' - Click 1 cookie.")
            print("'cookies' - Number of cookies.")
            print("'exit' - Exit Cookie Clicker.")
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
        elif hs == "reader":
            print("Reader Help")
            print("HOW TO USE:")
            print("1. Enter Reader")
            print("2. Type in the name a file you want to view with an extension (example - hi.txt)")
            print("3. Read the contents of the file")
        elif hs == "settings":
            print("Settings Help")
            print("SETTINGS:")
            print("'set-rtc' - Set the onboard clock")
            print("'exit' - Exit Settings")
        elif hs == "run":
            print("Run Help")
            print("HOW TO USE")
            print("Type in the file name of the program you want to use.")
        elif hs == "pin-control":
            print("Pin Control Help")
            print("COMMANDS")
            print("Enter '999' into 'Pin GPIO Number' to exit.")
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
        
        a = 1

        nq = 1
        
        answers = [0, ]
        
        print("QUESTIONS")
        
        print("ROUND TO 2 DECIMAL PLACES")

        while q < 100:
            if lev == "H":
                n1 = randint(1, 1000)
                n2 = randint(1, 1000)
                t = randint(1, 4)
                if t == 1:
                    print("Q",nq, ". What is ", n1, "+", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 + n2
                elif t == 2:
                    print("Q",nq, ". What is ", n1, "-", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 - n2
                elif t == 3:
                    print("Q", nq, ". What is ", n1, "*", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 * n2
                elif t == 4:
                    print("Q", nq, ". What is ", n1, "/", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 / n2
            elif lev == "M":
                n1 = randint(1, 100)
                n2 = randint(1, 100)
                t = randint(1, 4)
                if t == 1:
                    print("Q",nq, ". What is ", n1, "+", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 + n2
                elif t == 2:
                    print("Q",nq, ". What is ", n1, "-", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 - n2
                elif t == 3:
                    print("Q", nq, ". What is ", n1, "*", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 * n2
                elif t == 4:
                    print("Q", nq, ". What is ", n1, "/", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 / n2
            
            elif lev == "E":
                n1 = randint(1, 10)
                n2 = randint(1, 10)
                t = randint(1, 4)
                if t == 1:
                    print("Q",nq, ". What is ", n1, "+", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 + n2
                elif t == 2:
                    print("Q",nq, ". What is ", n1, "-", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 - n2
                elif t == 3:
                    print("Q", nq, ". What is ", n1, "*", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 * n2
                elif t == 4:
                    print("Q", nq, ". What is ", n1, "/", n2, "?")
                    q = q + 1
                    nq = nq + 1
                    answer = n1 / n2
            af = round(answer, 2)
            answers.append(af)
        print("ANSWERS")
        while a < 101:
            print("Q" + " " + str(a) + ": " + str(answers[a]))
            a = a + 1
    elif cmd == "war-scenario":
        from random import randint
        
        country = ["New Zealand", "Australia", "Austria", "South Africa", "You", "Russia", "Ukraine", "The United Kingdom", "France", "The United States", "India", "China", "Fiji", "Brazil", "Mexico", "Singapore", "Hong Kong", "Germany", "Poland", "Spain", "Mongolia", "Samoa", "Finland", "Ireland", "Italy", "Sweeden", "Japan", "Taiwan", "Chile", "Canada",]

        wartype = ["is starting a Nuclear War with", "is starting a war with", "is invading", "is pooping on", "is bombing", "is punching", "is starting a civil war with", "is starting a cyber war with", "is Italianing with", "is starting an AI war with", "is starting a space war with",]
        
        ctry = randint(0, len(country)-1)

        ctry2 = randint(0, len(country)-1)

            
        tpe = randint(0, len(wartype)-1)
        
        print("DISCLAIMER: THIS IS FICTIONAL - DO NOT TAKE IT AS BEING REAL")

        print(country[ctry], wartype[tpe], country[ctry2] + ".")

    elif cmd == "random-sentence":
        from random import randint
        
        w = ["Ur Mum", "Ur Dad", "Computer Crunch", "Your Cat", "Your Dog", "Donald Trump", "Raspberry Pi", "Apple", "Microsoft", "Google", "Meta", "Your friend", "Your teacher", ]
        
        w2 = ["did", "is doing", "saw", "calculated", "is on planet", "fixed", "created", "helped", "is in", "started up", "typed", "is a", "is", "is on the", "ate", ]
        
        w3 = ["YouTube", "Earth", "Ur Mum", "Ur Dad", "Ur Cat", "Your Computer", "grass", "mars", "macOS", "failure", "poem", "maintenance", "piano", "disaster", "customer", "software", "stranger", "bird", "guest", "orange", "spray tan", "guitar", "Interislander", "bad", "good", "Bluebridge", "train", "bus", "plane",]
        
        

        word = randint(0, len(w)-1)

        word2 = randint(0, len(w2)-1)

        word3 = randint(0, len(w3)-1)
        
            
        print("DISCLAIMER: THIS IS FICTIONAL - DO NOT TAKE IT AS BEING REAL")

        print(w[word], w2[word2], w3[word3])
        
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
        conosversion_factor = 3.3 / (65535)
        reading = sensor_temp.read_u16() * conosversion_factor 
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
    elif cmd == "clicker":
        click = 1
        cookies = 0
        print("Welcome to Cookie Clicker! Press enter to click cookies.")
        while click == 1:
            clickput = input("Cookie: ")
            if clickput == "exit":
                click = 0
                print("Goodbye")
                print("No. of cookies: " + str(cookies) + ".")
            elif clickput == "cookies":
                print("No. of cookies: " + str(cookies) + ".")
            elif clickput == "":
                print("COOKIE!")
                cookies = cookies+1
    elif cmd == "quiz":
        print("Welcome to News Quiz!")
        questions = ("When is the 2023 NZ Election (DD/MM/YYYY) ", "How many videos does Crunch TV & Radio Archives release per week?", "How old is Windows 11?", "What does PSU stand for?", "How many subscribers does Computer Crunch have as of 21/9/2023?")
        answers = ("14/10/2023", "35", "2", "Power Supply Unit", "127")
        quizq = 0
        quizs = 0
        while quizq < len(questions):
            print(questions[quizq])
            answer = input("Answer: ")
            if answer == answers[quizq]:
                quizs = quizs+1
                print("You got it correct! The answer is " + answers[quizq])
            else:
                print("Wrong. The correct answer is " + answers[quizq])
            quizq = quizq+1
        print("Score: " + str(quizs) + " out of " + str(len(questions)) + ".")
    
    elif cmd == "marketshare":
        print("Welcome to Market Share!")
        print("Latest as of 21/9/2023.")
        print("From statcounter")
        sector = input("Sector: ")
        if sector == "desktop":
            print("Desktop OS Market Share")
            print("Windows: 69.27%")
            print("macOS: 20.19%")
            print("Unknown: 4.02%")
            print("Linux: 3.19%")
            print("ChromeOS: 3.32%")
            print("FreeBSD: 0.01%")
        elif sector == "tablet":
            print("Tablet OS Market Share")
            print("iPadOS: 54.68%")
            print("Android: 45.11%")
            print("Windows: 0.02%")
            print("Linux: 0.13%")
            print("Unknown: 0.04%")
            print("Blackberry OS: 0.03%")
        elif sector == "mobile":
            print("Mobile OS Market Share")
            print("Android: 70.77%")
            print("iOS: 28.52%")
            print("Samsung: 0.37%")
            print("KaiOS: 0.1%")
            print("Unknown: 0.17%")
            print("Windows: 0.02%")
        elif sector == "pico":
            print("Raspberry Pi Pico OS Market Share")
            print("CMG PicoOS: 100%")
            
    elif cmd == "run":
        run = input("File Name: ")
        __import__(run)
    
    elif cmd == "pin-control":
        pincontrol = True
        while pincontrol == True:
            pinno = input("Pin GPIO Number: ")
            pinac = input("Value (1 or 0): ")
            if int(pinno) == 0:
                if int(pinac) == 1:
                    pin0.value(1)
                elif int(pinac) == 0:
                    pin0.value(0)
            elif int(pinno) == 1:
                if int(pinac) == 1:
                    pin1.value(1)
                elif int(pinac) == 0:
                    pin1.value(0)
            elif int(pinno) == 2:
                if int(pinac) == 1:
                    pin2.value(1)
                elif int(pinac) == 0:
                    pin2.value(0)
            elif int(pinno) == 3:
                if int(pinac) == 1:
                    pin3.value(1)
                elif int(pinac) == 0:
                    pin3.value(0)
            elif int(pinno) == 4:
                if int(pinac) == 1:
                    pin4.value(1)
                elif int(pinac) == 0:
                    pin4.value(0)
            elif int(pinno) == 5:
                if int(pinac) == 1:
                    pin5.value(1)
                elif int(pinac) == 0:
                    pin5.value(0)
            elif int(pinno) == 6:
                if int(pinac) == 1:
                    pin6.value(1)
                elif int(pinac) == 0:
                    pin6.value(0)
            elif int(pinno) == 7:
                if int(pinac) == 1:
                    pin7.value(1)
                elif int(pinac) == 0:
                    pin7.value(0)
            elif int(pinno) == 8:
                if int(pinac) == 1:
                    pin8.value(1)
                elif int(pinac) == 0:
                    pin8.value(0)
            elif int(pinno) == 9:
                if int(pinac) == 1:
                    pin9.value(1)
                elif int(pinac) == 0:
                    pin9.value(0)
            elif int(pinno) == 10:
                if int(pinac) == 1:
                    pin10.value(1)
                elif int(pinac) == 0:
                    pin10.value(0)
            elif int(pinno) == 11:
                if int(pinac) == 1:
                    pin11.value(1)
                elif int(pinac) == 0:
                    pin11.value(0)
            elif int(pinno) == 12:
                if int(pinac) == 1:
                    pin12.value(1)
                elif int(pinac) == 0:
                    pin12.value(0)
            elif int(pinno) == 13:
                if int(pinac) == 1:
                    pin13.value(1)
                elif int(pinac) == 0:
                    pin13.value(0)
            elif int(pinno) == 14:
                if int(pinac) == 1:
                    pin14.value(1)
                elif int(pinac) == 0:
                    pin14.value(0)
            elif int(pinno) == 15:
                if int(pinac) == 1:
                    pin15.value(1)
                elif int(pinac) == 0:
                    pin15.value(0)
            elif int(pinno) == 16:
                if int(pinac) == 1:
                    pin16.value(1)
                elif int(pinac) == 0:
                    pin16.value(0)
            elif int(pinno) == 17:
                if int(pinac) == 1:
                    pin17.value(1)
                elif int(pinac) == 0:
                    pin17.value(0)
            elif int(pinno) == 18:
                if int(pinac) == 1:
                    pin18.value(1)
                elif int(pinac) == 0:
                    pin18.value(0)
            elif int(pinno) == 19:
                if int(pinac) == 1:
                    pin19.value(1)
                elif int(pinac) == 0:
                    pin19.value(0)
            elif int(pinno) == 20:
                if int(pinac) == 1:
                    pin20.value(1)
                elif int(pinac) == 0:
                    pin20.value(0)
            elif int(pinno) == 21:
                if int(pinac) == 1:
                    pin21.value(1)
                elif int(pinac) == 0:
                    pin21.value(0)
            elif int(pinno) == 26:
                if int(pinac) == 1:
                    pin26.value(1)
                elif int(pinac) == 0:
                    pin26.value(0)
            elif int(pinno) == 27:
                if int(pinac) == 1:
                    pin27.value(1)
                elif int(pinac) == 0:
                    pin27.value(0)
            elif int(pinno) == 28:
                if int(pinac) == 1:
                    pin28.value(1)
                elif int(pinac) == 0:
                    pin28.value(0)
            elif int(pinno) ==  999:
                pincontrol = False
                print("Exiting...")
            else:
                print("Invalid Pin")
            print(" ")
    elif cmd == "pin-viewer":
        print("Current Pin Values: ")
        print("Pin 0: " + str(pin0.value()))
        print("Pin 1: " + str(pin1.value()))
        print("Pin 2: " + str(pin2.value()))
        print("Pin 3: " + str(pin3.value()))
        print("Pin 4: " + str(pin4.value()))
        print("Pin 5: " + str(pin5.value()))
        print("Pin 6: " + str(pin6.value()))
        print("Pin 7: " + str(pin7.value()))
        print("Pin 8: " + str(pin8.value()))
        print("Pin 9: " + str(pin9.value()))
        print("Pin 10: " + str(pin10.value()))
        print("Pin 11: " + str(pin11.value()))
        print("Pin 12: " + str(pin12.value()))
        print("Pin 13: " + str(pin13.value()))
        print("Pin 14: " + str(pin14.value()))
        print("Pin 15: " + str(pin15.value()))
        print("Pin 16: " + str(pin16.value()))
        print("Pin 17: " + str(pin17.value()))
        print("Pin 18: " + str(pin18.value()))
        print("Pin 19: " + str(pin19.value()))
        print("Pin 20: " + str(pin20.value()))
        print("Pin 21: " + str(pin21.value()))
        print("Pin 26: " + str(pin26.value()))
        print("Pin 27: " + str(pin27.value()))
        print("Pin 28: " + str(pin28.value()))
        
    
    
    print()
    led.value(0)