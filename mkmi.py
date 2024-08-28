import subprocess
import os
import platform
import time

config = "config.txt"
readme = "readme-edit.txt"

WinClear = "cls"
LMClear = "clear"

if platform.system() == "Windows": 
    subprocess.Popen(WinClear, shell=True)
elif platform.system() == "Linux" "Darwin":
    subprocess.Popen(LMClear, shell=True)
else: 
    print("I have no idea what you're running this on but please run the Configurator on Windows, macOS or Linux.")
    exit()

time.sleep(1)

print("""mkmi Configurator

Welcome to the mkmi Configurator Program!
This will help you make a clean and user-friendly
file structure for your modified Xiaomi mobile OS.

To start off, select one of the options listed:
""")

selection = input("""
1. Review readme-edit.txt
2. Review config.txt
3. Make!

Q. Quit

>>> """)

if selection == "1":
    r = open(readme, 'r')
    readme_content = r.read()
    print("Reviewing README...")
    time.sleep(1)
    print(readme_content)
    r.close()

elif selection == "2":
    c = open(config, 'r')
    config_content = c.read()
    print("Reviewing CONFIG...")
    time.sleep(1)
    print(config_content)
    c.close()

elif selection == "3":
    c = open(config, 'r')
    config_content = c.read()
    time.sleep(0.3)
    print(config_content)
    confirmation = input("Is your config correct? (yes/no): ")
    if confirmation == "yes":
        print("Starting to create in")
        time.sleep(0.5)
        for i in range(1,6)[::-1]:
            print(i)
            time.sleep(1)

        print("Commencing Process. Please be patient.")
        # create directory > /images
        # copy necessary stock images to /images
        # copy super and preloader to /
        # compress super to super.zst
        # generate flash.bat and flash.sh
        # generate readme.txt
        # new file explorer window with contents
        # profit

elif selection == "q":
    print("Quitting...")
    exit()