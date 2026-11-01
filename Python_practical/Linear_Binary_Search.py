id = [101,102,103,104,105]
target_id = int(input("Enter customer ID:"))
found = False
for i in range(len(id)):
    if id[i] == target_id:
        print("linear search:Found at position",i+1)
        found = True
        break
if not found:
    print("Linear search: Not found")

low = 0
high = len(id)-1
found = False
while low <= high:
    mid = (low+high) // 2
    if id[mid] == target_id:
        print("Binary search: Found at position:",mid+1)
        found = True 
        break
    elif target_id < id[mid]:
        high = mid - 1
    else:
        low = mid + 1
if not found:
    print("Binary search:Not Found")
