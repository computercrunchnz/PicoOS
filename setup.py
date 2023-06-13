import machine

print("PicoOS 2 Setup")
namefile = open("name.txt", "w")
name = input("Name: ")

namefile.write(name)

namefile.close()

year = input("Year: ")
month = input("Month: ")
wday = input("Day of the week (0=mon, 1=tue, 2=wed, 3=thu, 4=fri, 5=sat, 6=sun):")
day = input("Day: ")
hour = input("Hour: ")
minute = input("Minute: ")
machine.RTC().datetime((int(year), int(month), int(day), int(wday), int(hour), int(minute), 0, 0))

print("Setup Done!")