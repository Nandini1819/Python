correct_password = "admin112"
for attempt in range(1,4):
    password = input("Enter your Password:")
    if password == correct_password:
        print("Login Successful")
        break;
    else:
        print("Incorrect Password")
    if attempt == 3:
        print("Account locked")
