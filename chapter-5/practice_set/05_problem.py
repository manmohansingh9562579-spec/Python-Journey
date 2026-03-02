students_to_check = ["Charlie", "Bob", "Eve", "Alice", "David"]

name = input("Enter the name of student: ")

if name in students_to_check:
    print(name + " is in the list of students to check.")
 
else:
    print(name + " is not in the list of students to check.")