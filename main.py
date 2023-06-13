import time

import sys

import math

import os

from sys import version

osversion = "2.0"
osversionpostnote = "Beta 1 PC SDK"

print("Welcome to PicoOS!")
print("Report any issues to computercrunchnz+picoos2@gmail.com")
print("Version: " + str(osversion) + " " + str(osversionpostnote))

namefile = open("name.txt", "r")
name = namefile.read()
namefile.close()


while True:
    cmd = input("> ")
    print()
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
    elif cmd == "help":
        print("Help")
        print("COMMANDS:")
        print("'about' - About PicoOS")
        print("'update' - Where to update PicoOS")
        print("'calculator' - Calculator")
        print("'writer' - Text Editor")
        print("'reader' - Document Reader")
        print("'maths-quiz' - A Maths Quiz creator with multiple levels")
        print("'war-scenario' - A war scenario generator")
        print("'random-sentence' - A random sentence generator")
        print("'clicker' - Cookie Clicker")
        print("'market-share' - OS Market Share (real time stock values coming soon)")
        print("'news-quiz' - News Quiz")
        print("'ls' - Lists the files")
        print("'del' - Delete a file")
        print("'setup' - Setup PicoOS")
        print("'run' - Run a program from another file")
        print("'help' - Help")
        print("'exit' - Exit PicoOS")
        print("Some PicoOS features are not available on PC as they leverage hardware on RP2040.")
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
        elif hs == "run":
            print("Run Help")
            print("HOW TO USE")
            print("Type in the file name of the program you want to use.")
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
    elif cmd == "news-quiz":
        print("Welcome to News Quiz!")
        questions = ("When will PicoOS 2 be released? (DD/MM/YYYY) ", "What month is WWDC usually in?", "How old does Windows 98 turn this year?", "What does PC stand for?", "How many subscribers does Computer Crunch have as of 2/6/2023?")
        answers = ("04/09/2023", "June", "25", "Personal Computer", "101")
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
    
    elif cmd == "market-share":
        print("Welcome to Market Share!")
        print("Latest as of 2/6/2023.")
        print("From statcounter")
        sector = input("Sector: ")
        if sector == "desktop":
            print("Desktop OS Market Share")
            print("Windows: 61.87%")
            print("macOS: 18.87%")
            print("Unknown: 13.01%")
            print("Linux: 2.69%")
            print("ChromeOS: 3.54%")
            print("FreeBSD: 0%")
        elif sector == "tablet":
            print("Tablet OS Market Share")
            print("iPadOS: 55.89%")
            print("Android: 43.92%")
            print("Windows: 0.02%")
            print("Linux: 0.12%")
            print("Unknown: 0.03%")
            print("Blackberry OS: 0.01%")
        elif sector == "mobile":
            print("Mobile OS Market Share")
            print("Android: 67.56%")
            print("iOS: 31.6%")
            print("Samsung: 0.43%")
            print("KaiOS: 0.2%")
            print("Unknown: 0.15%")
            print("Windows: 0.02%")
        elif sector == "pico":
            print("Raspberry Pi Pico OS Market Share")
            print("CMG PicoOS: 100%")
            
    elif cmd == "run":
        run = input("File Name: ")
        __import__(run)
        
    
    
    print()