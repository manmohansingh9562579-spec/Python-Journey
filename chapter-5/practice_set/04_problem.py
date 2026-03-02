username = input("Enter your name:")



if len(username) < 10:
    print("Welcome to the spam comment detector, " + username)
    print("Your name is valid, you can proceed to the next step.")    
else:
    print("Your name is too long, please enter a name with less than 10 characters.")
       