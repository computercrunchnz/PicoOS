print("PicoOS Industrial 0.1 Alpha Setup")
namefile = open("name.txt", "w")
name = input("Name: ")

namefile.write(name)

namefile.close()

print("Setup completed!")
