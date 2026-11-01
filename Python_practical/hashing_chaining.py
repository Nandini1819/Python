size = 10
table = [[] for i in range(size)]
def insert(key):
    index = key % size
    table[index].append(key)
def display():
    for i in range (size):
        print(i,":",table[i])
keys = [31,3,4,21,61,6,71]
for key in keys:
    insert(key)
print("Hash Table using Chaining:")
display()