# PicoOS
An OS for boards with the RP2040 Processor.

# Compatibility
Boards with the RP2040 processor and Micropython.

# Support Lifecycle
Each full release of PicoOS (1.x 2.x etc) gets 2 years of updates from the release date.

PicoOS 1 End Of Support: 11/1/2025

# Setup 1 - For Windows, macOS and Linux to add files to the RP2040 Board.
1) Download and Install Thonny ```wget -O thonny-latest.sh https://thonny.org/installer-for-linux``` (example for Linux).
2) Connect the Pico or RP2040 board to your computer.
3) Clone this Repository ```git clone https://github.com/computercrunchnz/PicoOS.git``` (example for Linux). 
4) Once Thonny and PicoOS is downloaded enter Thonny.
5) At the Right-Hand side on the bottom there should be a line saying what interprepter you are in.
6) Click that and choose MicroPython Raspberry Pi Pico.
7) If you don't have MicroPython installed on your Pico or RP2040 board, Thonny will ask if you want to install MicroPython. Click install and it may take a few minutes to install MicroPython.
8) Now open **main.py, setup.py, name.txt and smartlight.py** from the git folder and **save it to the Pico or RP2040 board**.
9) Once that is done run main.py.
10) Type in the ```setup``` command in PicoOS to change the name of the Pico or RP2040 board.
11) Type in the ```help``` command for a list of all commands.

# Setup 2 - For use on Linux.
1) If you have not put PicoOS on your Pico or RP2040 board, please refer to Setup 1 before this.
2) Open the terminal.
3) Install python3 ```sudo apt install python3``` (Debian & Ubuntu). ```sudo pamac install python3``` (Manjaro).
4) Run the command to get Python Pip. ```sudo apt-get install python-pip``` (Debian & Ubuntu). ```sudo pamac install python-pip``` (Manjaro).
5) Run the command to install rshell. ```sudo pip3 install rshell```.
6) Connect the Pico or RP2040 board to your computer.
7) Run the command ```sudo rshell```.
8) Type in repl.
9) Press ```control-d```
10) You are now in the PicoOS CLI!
11) Type in the ```help``` command for a list of all commands.
12) To exit, type ```exit``` into PicoOS then confirm exit by typing ```Y```, then press ```control-x``` and finally press ```control-d``` to get back to the Linux terminal.

# Setup 3 - For use on macOS.
1) If you have not put PicoOS on your Pico or RP2040 board, please refer to Setup 1 before this.
2) Open the terminal.
3) Run the command to install rshell. ```sudo pip3 install rshell```.
4) Connect the Pico or RP2040 board to your computer.
5) Run the command ```sudo rshell```.
6) Type in repl.
7) Press ```control-d```
8) You are now in the PicoOS CLI!
9) Type in the ```help``` command for a list of all commands.
10) To exit, type ```exit``` into PicoOS then confirm exit by typing ```Y```, then press ```control-x``` and finally press ```control-d``` to get back to the Linux terminal.

# Update PicoOS
1) Connect the Pico or RP2040 board to your computer.
2) Clone this Repository ```git clone https://github.com/computercrunchnz/PicoOS.git``` (example for Linux). 
3) Enter Thonny.
5) At the Right-Hand side on the bottom there should be a line saying what interprepter you are in.
6) Now open **main.py, setup.py, name.txt and smartlight.py** from the git folder and **save it to the Pico or RP2040 board**.
7) Once that is done run main.py.
10) Type in the ```setup``` command in PicoOS to change the name of the Pico or RP2040 board.
11) Type in the ```help``` command for a list of all commands.


# Help
We are available on Github, if there is a problem open an issue and we will attend to it as fast as possible.

# Further Support
If you have any questions, please contact us at computercrunchnz+picoos1@gmail.com or reach out to us on our discord server or Github.

# Credit
Software written by @ComputerCrunch and @STESROS6309wastaken.

# All Builds
All of the PicoOS builds, including the betas and alphas, are located in Releases.
