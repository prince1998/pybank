from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty,StringProperty


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




presentation = Builder.load_file('layouts.kv')

class PyBank(App):

          def build(self):
                    return presentation

if __name__ == '__main__':
          PyBank().run()
