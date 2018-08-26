import pyrebase

config = {
    #Enter your config details 
  };

firebase = pyrebase.initialize_app(config)

auth = firebase.auth();

user = auth.sign_in_with_email_and_password('akhilkshah@gmail.com','123456');

db = firebase.database();

data = {"name":"Akhil Shah"}
db.child("users").child("Akhil").set(data)
db.child("users").child("Akhil").update({"Balance":50})

data = {"name":"Another User"}
db.child("users").child("User2").set(data)
db.child("users").child("User2").update({"Balance":50})

#Execute these two lines of code to change balances
#db.child("users").child("Akhil").update({"Balance":150})
#db.child("users").child("User2").update({"Balance":100})








