def find_missing(numbers,n):
    expected_sum = n*(n+1)//2
    actual_sum = 0
    for num in numbers:
        actual_sum = actual_sum + num
    missing = expected_sum - actual_sum
    return missing
numbers = []
n = int(input("Enter the value of n:"))
for i in range(n-1):
    num = int(input("Enter a number:"))
    numbers.append(num)
result = find_missing(numbers,n)
print(result)