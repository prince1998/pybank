import sys
import shlex,subprocess
import time

try:
    import kivy
    kivy.require("1.10.0")
    from kivy.app import App
    from kivy.uix.label import Label
    import pyrebase
    dependencies=True
    
except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))
    
    if input("Would you like to install Kivy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install Kivy"))
        time.sleep(3)
        
    if input("Would you like to install Pyrebase? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip install Pyrebase"))
        time.sleep(3)
        
    print("Please restart the program")
    dependencies=False
    
if dependencies==True:
    print("Hello, world!")
    #insert code here