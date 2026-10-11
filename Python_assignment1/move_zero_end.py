def move_zeros(numbers):
    result=[]
    zero_count = 0
    for num in numbers:
      if num==0:
        zero_count = zero_count+1
      else:
        result.append(num)
    for i in range(zero_count):
       result.append(0)
    return result
numbers=[]
n=int(input("how many times do you want to enter a number:"))
for i in range(0,n):
   num=int(input("Enter a number:"))
   numbers.append(num)
result = move_zeros(numbers)
print(result)       