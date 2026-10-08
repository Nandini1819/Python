def find_duplicate(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
              return "duplicate found"
    return "no duplicate"
list=[10, 20,20, 30, 40]
result=find_duplicate(list)
print(result)
