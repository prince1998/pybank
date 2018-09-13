import sys
import shlex,subprocess
import config #config.py file for Firebase

try:
    import kivy
    from kivy.app import App
    from kivy.lang import Builder
    from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
    from kivy.properties import ObjectProperty,StringProperty
    
    import pyrebase
    
    dependencies_exist=True #if all packages are installed
    
except ImportError:
    print("\nSorry, you don't seem to have the required dependencies installed for the following version of Python: {}\n".format(sys.version))
    
    if input("Would you like to install Kivy? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip3 install Kivy")) #installs Kivy
        
    if input("Would you like to install Pyrebase? Y/N:\n")=="y":
        subprocess.Popen(shlex.split("pip install Pyrebase")) #installs Pyrebase
        
    print("Please restart the program")
    dependencies_exist=False
    
if dependencies_exist: #only if everything is installed
    
    class ScreenManagement(ScreenManager):
        pass
              
    class RegisterScreen(Screen):
        pass

    class LoginScreen(Screen):
        def validate(self):
            self.email = self.ids.email.text
            self.password = self.ids.password.text
            obj = SetGetLoginInfo()
            obj.setLoginInfo(self.email)
            self.manager.current = 'user' 
                            
    class UserScreen(Screen):
        def getname(self):
            obj = SetGetLoginInfo()
            self.ids.label.text = obj.getLoginInfo()
    
    class SetGetLoginInfo:
        email_id = ""

        def __init__(self):
            pass
            
        def setLoginInfo(self,email):
            SetGetLoginInfo.email_id = email

        def getLoginInfo(self):
            return SetGetLoginInfo.email_id
    
    presentation = Builder.load_file('layout.kv')
    
    class PyBank(App):
        def build(self):
            return presentation
    
    if __name__ == '__main__':
        PyBank().run()