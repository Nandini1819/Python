queue = []
while True:
    print("1. Add call 2. Answer call 3. View Queue 4.Exit ")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        c_id = input("Enter customer ID: ")
        queue.append(c_id)
        print("Call added")
    elif choice == 2:
        if queue:
            print("Answered call:",queue.pop(0))
        else:
            print("Queue is Empty")
    elif choice == 3:
        print("Pending calls:",queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice")