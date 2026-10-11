def max_consecutive(numbers):
    if len(numbers)==0:
        return 0
    count = 1
    maximum = 1
    for i in range(1,len(numbers)):
        if numbers[i]==numbers[i-1]:
            count = count + 1
        else:
            count = 1
        if count > maximum:
            maximum = count
    return maximum
numbers = [1,1,2,2,2,3,3,1,1,1,1]
result = max_consecutive(numbers)
print(result)