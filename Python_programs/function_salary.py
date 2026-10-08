def employee(salary):
    highest = salary[0]
    lowest = salary[0]
    total=0
    count=0
    for sal in salary:
        if sal>highest:
            highest=sal
        if sal<lowest:
            lowest=sal
        if sal>50000:
            count=count+1
    for sal in salary:
        total=total+sal
    average=total/len(salary)
    noofemployee=len(salary)
    

    return highest, lowest,average,noofemployee,count
salary = []
emp=int(input("Enter number of epmloyees:"))
for i in range(emp):
    s=int(input("Enter salary:"))
    salary.append(s)
highest, lowest,average,noofemployee,count=employee(salary)
print("highest salary:",highest)
print("lowest salary:",lowest)
print("employees having more than 50000:",count)
print("number of employees:",noofemployee)
print("average salary",average)
 
