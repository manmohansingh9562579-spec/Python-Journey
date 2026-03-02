s1 = int(input("Enter marks of  subject 1: "))
s2 = int(input("Enter marks of  subject 2: "))
s3 = int(input("Enter marks of  subject 3: "))

# check for total percentage

total = s1 + s2 + s3

percentage = total/300 * 100

if(percentage>=40):
    print("You have passed with", percentage, "%")
else:
    print("You have failed with", percentage, "%")

# check for individual subject marks    

if(s1>=33 and s2>=33 and s3>=33):
    print("You have passed in all subjects")
else:
    print("You have failed in one or more subjects")
    