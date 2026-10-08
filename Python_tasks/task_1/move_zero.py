def move_zero(numbers):
    result=[]
    zero_count=0
    for num in numbers:
        if num==0:
            zero_count=zero_count+1
        else:
            result.append(num)
    for i in range (zero_count):
        result.append(0)
    return(zero_count,result)
numbers=[0,1,0,3,12,0,5]
zero_count,result=(move_zero(numbers))
print(result)

    