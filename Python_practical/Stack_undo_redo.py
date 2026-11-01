undo = []
redo = []
document = ""
while True:
    print("1. Make a change 2. Undo 3. Redo 4. Display 5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        undo.append(document)
        document = input("Enter new text:")
        redo.clear()
    elif choice == 2:
        if undo:
            redo.append(document)
            document = undo.pop()
            print("Undo successful")
        else:
            print("Nothing to Undo")
    elif choice == 3:
        if redo:
            undo.append(document)
            document = redo.pop()
            print("Redo Successful")
        else:
            print("Nothing to Redo")
    elif choice == 4:
        print("Document:",document)
    elif choice == 5:
        break
    else:
        print("Invalid Choice")