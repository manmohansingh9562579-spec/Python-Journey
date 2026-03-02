a =int(input("Enter your age: ")) 

# if-elif-else ladder

if(a>=18):
    print("You are eligible to vote.")
    print("You can participate in elections.")

   
elif(a==0):
    print("Age cannot be zero. Please enter a valid age.")
    

elif(a<0):
    print("Invalid age entered. Please enter a valid age.")

    
else:
    print("You are not eligible to vote.")
    print("You have to wait until you turn 18.") 

print("Thank you!")

