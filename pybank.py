import sys
import shlex,subprocess
import db_communicator #db_communicator.py file for Firebase methods

try:
    import kivy
    from kivy.app import App
    from kivy.lang import Builder
    from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
    from kivy.properties import ObjectProperty,StringProperty
    from kivy.uix.popup import Popup
    
    import pyrebase
    
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
    
    class ScreenManagement(ScreenManager):
        pass
    
    class RegisterScreen(Screen):
              
        def create_user(self):
            self.name = self.ids.name.text
            self.email = self.ids.email.text
            self.password = self.ids.password.text
            cnfig = config.Config()
            cnfig.create_user(self.name,self.email,self.password)
        

    class LoginScreen(Screen):
        def validate(self):
            self.email = self.ids.email.text
            self.password = self.ids.password.text
            cnfig = config.Config()
            cnfig.sign_in_user(self.email,self.password)
            obj = SetGetLoginInfo()
            obj.setLoginInfo(self.email)
            self.manager.current = 'user' 
                            
    class UserScreen(Screen):

        def display(self):
            obj = SetGetLoginInfo()
            email = obj.getLoginInfo()
            cnfig = config.Config()
            name,balance,message = cnfig.get_user(email)
            self.balance = str(balance)
            self.ids.name.text = "Welcome "+name
            self.ids.balance.text = "Balance = "+str(balance)
        

    class MoneyScreen(Screen):
        pass



    class AddMoney(Popup):

        def add_money(self):
            obj = SetGetLoginInfo()
            email = obj.getLoginInfo()
            amount = int(self.ids.money_add.text)
            cnfig = config.Config()
            cnfig.add_money(amount,email)

    
            
    class TransferMoney(Popup):

        def transfer_money(self):
            obj = SetGetLoginInfo()
            user_email = obj.getLoginInfo()
            transfer_email = self.ids.transfer_email.text
            amount = int(self.ids.money_transfer.text)
            cnfig = config.Config()
            cnfig.transfer_money(amount,user_email,transfer_email)

    
  
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