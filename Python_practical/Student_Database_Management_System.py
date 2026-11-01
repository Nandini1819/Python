students = {}
while True:
    print("1. Add student")
    print("2. Search student")
    print("3. Delete student")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter a choice:"))
    if choice == 1:
        roll = int(input("Enter Roll Number:"))
        name = input("Enter Name:")
        students[roll] = name
        print("Students added")
    elif choice == 2:
        roll = int(input("Enter roll no to Search:"))
        if roll in students:
            print("Student name:",students[roll])
        else:
            print("Student not found")
    elif choice == 3:
        roll = int(input("Enter roll number:"))
        if roll in students:
            del students[roll]
            print("Student Deleted")
        else:
            print("Student not found")
    elif choice == 4:
        for roll,name in students.items():
            print("Roll no",roll, "Name:",name)
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
