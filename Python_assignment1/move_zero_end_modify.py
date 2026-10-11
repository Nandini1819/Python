def move_zeros(numbers):
    position = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position] = numbers[i]
            position+=1
    while position<len(numbers):
        numbers[position] = 0
        position+=1
numbers = []
n = int(input("How many numbers you want to enter:"))
for i in range(n):
    num = int(input("Enter a number:"))
    numbers.append(num)
move_zeros(numbers)
print(numbers)