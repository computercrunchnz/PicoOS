import time

import sys

import math

import os

print("Welcome to PicoOS 1 PC SDK!")
print("Finally in Beta!")
print("Report any issues to computercrunchnz+picoos1@gmail.com")

namefile = open("name.txt", "r")
name = namefile.read()
namefile.close()


while True:
    cmd = input("> ")
    print()
    if cmd == "about":
        print("About")
        print("PicoOS 1.0 Beta 1 PC SDK")
        print("Made by Crunch Media Group Software")
        print("This PicoPC belongs to " + name + ".")
        print("Report any issues to computercrunchnz+picoos1@gmail.com")
    elif cmd == "update":
        print("Update")
        print("To get the latest version, go to the PicoOS git repository at https://github.com/computercrunchnz/PicoOS.")
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
        print("Settings not avaliable in PC SDK.")
    elif cmd == "help":
        print("Help")
        print("COMMANDS:")
        print("'about' - About PicoOS")
        print("'update' - Where to update PicoOS")
        print("'calculator' - Calculator")
        print("'writer' - Text Editor")
        print("'reader' - Document Reader")
        print("'settings' - Settings - Not avaliable in PC SDK.")
        print("'maths-quiz' - A Maths Quiz creator with multiple levels")
        print("'war-scenario' - A war scenario generator")
        print("'random-sentence' - A random sentence generator")
        print("'temp' - Check the temperature in celcius - Not avaliable in PC SDK.")
        print("'smartlight' - Enter SmartLight Mode - Not avaliable in PC SDK - ONLY ENTER IF THIS IS A SMARTLIGHT!")
        print("'clicker' - Cookie Clicker")
        print("'marketshare' - OS Market Share")
        print("'quiz' - News Quiz")
        print("'time' - Tells the time and date - Not avaliable in PC SDK.")
        print("'ls' - Lists the files")
        print("'del' - Delete a file")
        print("'setup' - Setup PicoOS")
        print("'help' - Help")
        print("'exit' - Exit PicoOS")
        print("'reboot' - Reboot Pico - Not avaliable in PC SDK.")
        hs = input("Do you need commands for in an app? ")
        if hs == "no":
            print("Okay")
        elif hs == "marketshare":
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
        elif hs == "smartlight":
            print("SmartLight Help - SmartLight not avaliable in PC SDK.")
            print("COMMANDS:")
            print("'on.all' - Turn on all LEDs.")
            print("'on.x' - Turn on x colour led.")
            print("'off.all' - Turn off all LEDs.")
            print("'on.x' - Turn off x colour led.")
            print("'flash.all' - Flash all LEDs.")
            print("'flash.stop' - Stop flashing LEDs.")
            print("'strobe.all' - Strobe all LEDs.")
            print("'strobe.stop' - Stop strobing LEDs.")
            print("'scroll.fast' - Scroll fast.")
            print("'scroll.slow' - Scroll slow.")
            print("'scroll.stop' - Stop scrolling.")
            print("'start.5min' - 5 minute sailing start sequence.")
            print("'start.3min' - 3 minute sailing start sequence.")
            print("'start.stop' - Stop the start sequence.")
            print("'about' - About.")
            print("'trafficlight' - Traffic Light.")
            print("'restart' - Restart the pico.")
            print("'exit' - Exit SmartLight.")
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
            print("Settings Help - Settings not avaliable in PC SDK.")
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
        print("Time not avaliable in PC SDK.")
    elif cmd == "reboot":
        print("Reboot not avaliable in PC SDK.")
    elif cmd == "temp":
        print("Temperature not avaliable in PC SDK.")
    elif cmd == "ls":
        ls = os.listdir()
        print(ls)
    elif cmd == "del":
        todel = input("File name: ")
        os.remove(todel)
    elif cmd == "setup":
        import setup
    elif cmd == "smartlight":
        print("SmartLight not avaliable in PC SDK")
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
        questions = ("What does WWDC stand for?", "How old is the queen?", "Who is the founder of amazon?", "Y/N: Does the EU want a common charger on all phones?", "What does CPU stand for")
        answers = ("World Wide Developers Conference", "96", "Jeff Bezos", "Y", "Central Processing Unit")
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
        print("Latest as of 11/6/2022.")
        sector = input("Sector: ")
        if sector == "desktop":
            print("Desktop OS Market Share")
            print("Windows: 75.54%")
            print("macOS: 14.98%")
            print("Unknown: 4.81%")
            print("Linux: 2.45%")
            print("ChromeOS: 2.22%")
            print("FreeBSD: 0.01%")
        elif sector == "tablet":
            print("Tablet OS Market Share")
            print("iPadOS: 53.63%")
            print("Android: 46.3%")
            print("Windows: 0.03%")
            print("Linux: 0.02%")
            print("Unknown: 0.01%")
            print("Blackberry OS: 0.01%")
        elif sector == "mobile":
            print("Mobile OS Market Share")
            print("Android: 71.45%")
            print("iOS: 27.83%")
            print("Samsung: 0.41%")
            print("KaiOS: 0.12%")
            print("Unknown: 0.12%")
            print("Nokia Unknown: 0.01%")
        elif sector == "pico":
            print("Raspberry Pi Pico OS Market Share")
            print("CMG PicoOS: 100%")
    elif cmd =="benchmark":
        import time
        import math
        import random

        runs = input("Minutes to run for: ")

        runsa = 0
        runsb = 0

        runb = time.time() + 60 * int(runs)

        while time.time() < runb:
            calct = random.randint(0,5)
            calc1 = random.randint(0,999999999)
            calc2 = random.randint(0,999999999)
            if calct == 0:
                a = calc1 + calc2
                b = calc1 - calc2
            elif calct == 1:
                a = calc1 * calc2
                b = calc1 / calc2
            elif calct == 2:
                a = math.e
                b = math.e
            elif calct == 3:
                a = math.pi
                b = math.pi
            elif calct == 4:
                a = math.cos(calc1)
                b = math.cos(calc2)
            elif calct == 5:
                a = math.sin(calc1)
                b = math.sin(calc2)
            elif calct == 6:
                a = math.tan(calc1)
                b = math.tan(calc2)
            elif calct == 7:
                a = math.factorial(calc1)
                b = math.factorial(calc2)
            
            print(a,b)
            
            f = open("test.txt","w")
            f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce at vulputate enim, et pharetra est. Cras vitae rutrum lacus, sed iaculis tellus. Sed aliquet mi at magna euismod mattis. Sed in lorem pellentesque, blandit orci vel, scelerisque nunc. Donec a ex nibh. Maecenas a faucibus tellus, ac laoreet ligula. Ut ac ante ac ligula bibendum mollis nec viverra enim. Etiam luctus lorem purus, eget tincidunt leo sollicitudin eget. Vestibulum ac neque at arcu euismod maximus. Fusce eget pellentesque ante. Quisque vitae mauris rutrum, laoreet quam eu, iaculis nibh. Praesent lobortis mollis vestibulum. Sed imperdiet turpis vel augue fringilla vulputate. In est neque, sollicitudin id nunc nec, mollis luctus erat. Integer non congue nunc, vel consequat est. Aliquam faucibus aliquet dolor, et pharetra augue pellentesque molestie. Ut id feugiat magna. Integer quis erat erat. Maecenas elementum dolor quis nisi pulvinar, at dictum mauris auctor. Aliquam aliquam mauris nulla, ut viverra ex ultricies ut. Praesent auctor augue non nunc blandit condimentum. Vestibulum nec ipsum velit. Proin commodo pharetra libero non vestibulum. Cras porttitor lobortis mauris, sed euismod est pretium et. Ut imperdiet quam quis dolor vehicula tempus. Curabitur erat ante, convallis at lorem quis, hendrerit elementum nulla. Nullam faucibus aliquam maximus. Nam condimentum nibh vitae massa mattis, ac varius lacus semper. Proin tempor augue maximus tincidunt vestibulum. Integer consectetur tellus eu odio auctor elementum. Mauris tincidunt diam nec luctus porta. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum turpis justo, pulvinar ultricies efficitur vel, bibendum ac justo. Mauris lacinia porttitor libero, quis fermentum purus. Mauris odio tortor, egestas id odio eu, commodo finibus nibh. Suspendisse potenti. In venenatis purus sit amet ex finibus, sed consectetur eros vehicula. Donec ut maximus lacus, sit amet rhoncus justo. Fusce nec dui turpis. Cras sed efficitur ligula. Duis at ligula orci. Integer malesuada aliquet sem id consequat. Proin elit lacus, vulputate ac pharetra in, aliquam ac mi. Sed rhoncus erat ac nisl iaculis accumsan. Sed nunc lorem, finibus at eros condimentum, scelerisque eleifend metus.")
            f.close()
            
            f = open("test.txt", "r")
            print(f.read())
            f.close()
            
            runsa = runsa + 1
            
        runs = runsa + runsb

        print("Done!")
        print("Score: " + str(runsa+runsb))
        
    
    #INSERT APP HERE
    #elif cmd == "x":
    
    
    
    print()