p1 = "make a money easily by doing nothing"
p2 = "how to get a job without experience"
p3 = "how to make money online without investment"

message = input("enter your comment: ")

if p1 in message or p2 in message or p3 in message:
    print("This is a spam comment")
else:
    print("This is not a spam comment")