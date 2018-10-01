import pyrebase
import fb_config

firebase=pyrebase.initialize_app(fb_config.config)
auth=firebase.auth()
db=firebase.database()

class Config:
    def __init__(self):
            pass

    def create_user(self,name,email,password):
        user = auth.create_user_with_email_and_password(email, password)
        email = email.split('@')[0]
        db.child("users").child(email).set({"name":name,"balance":0})
        db.child("users").child(email).child("messages").push("Your Transactions: ")

    def sign_in_user(self,email,password):
        user = auth.sign_in_with_email_and_password(email, password)

    def get_user(self,email):
        email = email.split('@')[0]
        name = db.child("users").child(email).child("name").get()
        balance = db.child("users").child(email).child("balance").get()
        message = db.child("users").child(email).child("message").get()
        return name.val(),balance.val(),message.val()

    def add_money(self,amount,email):
        email = email.split('@')[0]
        balance = db.child("users").child(email).child("balance").get()
        amount = amount + balance.val()
        db.child("users").child(email).update({"balance":amount})


    def transfer_money(self,amount,user_email,transfer_email):            
        user_email = user_email.split('@')[0]
        transfer_email = transfer_email.split('@')[0]

        balance = db.child("users").child(user_email).child("balance").get()
        amount_user = balance.val() - amount
        db.child("users").child(user_email).update({"balance":amount_user})

        balance = db.child("users").child(transfer_email).child("balance").get()
        amount_transfer = amount + balance.val()
        db.child("users").child(transfer_email).update({"balance":amount_transfer})