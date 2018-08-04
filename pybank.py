import sys

try:
    import kivy
    kivy.require("1.10.0")
    from kivy.app import App
    from kivy.uix.label import Label
    dependencies=True
    
except ImportError:
    print("\nSorry, you don't seem to have Kivy installed for the following version of Python: {}\n\nYou can try by running 'pip3 install kivy'.\n".format(sys.version))
    dependencies=False
    
if dependencies==True:
    print("Hello, world!")
    #insert code here