correctuser="admin";
correctpass="python@123"

username=input("Enter your username:");
password=input("Enter your password:");
if(username==correctuser and password==correctpass):
    print("Login successful");
elif(username!=correctuser and password==correctpass):
    print("Incorrect username");
else:
    print("Incorrect password");
