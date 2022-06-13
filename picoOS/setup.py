print("PicoOS 1 Setup")
namefile = open("name.txt", "w")
name = input("Name: ")

namefile.write(name)

namefile.close()

passwordfile = open("password.txt", "w")
pwd = input("Password: ")

passwordfile.write(pwd)

passwordfile.close()

print("Setup Done!")