first = "listen"
second = "silent"
frequency = {}
for char in first:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

for char in second:
    if char in frequency:
        frequency[char]-=1
    else:
        frequency[char]=-1
if all(count==0 for count in frequency.values()):
    print(True)
else:
    print(False)
