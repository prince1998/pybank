import sys
import shlex,subprocess
import config #config.py file for Firebase

try:
    import pyrebase
    
    import kivy
    from kivy.app import App
    from kivy.lang import Builder
    from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
    from kivy.properties import ObjectProperty,StringProperty
    
    dependencies_exist=True #if all packages are installed
    
except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))
    
    if input("Would you like to install Kivy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install Kivy")) #installs Kivy
        
    if input("Would you like to install Pyrebase? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install Pyrebase")) #installs Pyrebase
        
    print("Please restart the program")
    dependencies_exist=False
    
if dependencies_exist: #only if everything is installed
    email=input("Enter email to register: ")
    password=input("Enter password to register: ")
    config.create_user(email,password)
    log_in(email,password)