print("PicoOS 1 Setup")
print("this script changes the name of the Pico")
namefile = open("name.txt", "w")
name = input("Name: ")

namefile.write(name)

namefile.close()

print("Setup Completed Successfully!")
