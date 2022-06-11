print("PicoOS 1 Setup")
namefile = open("name.txt", "w")
name = input("Name: ")

namefile.write(name)

namefile.close()

print("Setup Done!")