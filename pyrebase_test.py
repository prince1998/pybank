import pyrebase

config={
    
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
user=auth.sign_in_with_email_and_password('testuser@gmail.com','password')
db=firebase.database()

data={"name":"Test User"}
db.child("users").child("User1").set(data)
db.child("users").child("User1").update({"Balance":900})
data={"name":"Another User"}
db.child("users").child("User2").set(data)
db.child("users").child("User2").update({"Balance":800})

# Execute these two lines of code to change balances
# db.child("users").child("User1").update({"Balance":150})
# db.child("users").child("User2").update({"Balance":100})
