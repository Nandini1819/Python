size = 10
table = [None] * size
def insert(key):
    index = key % size
    while table[index] is not None:
        index = (index + 1) % size
    table[index] = key
keys = [31,3,4,21,61,6,71]
for key in keys:
    insert(key)
print("Hash Table using Linear Probing: ")
for i in range(size):
    print(i,":",table[i])