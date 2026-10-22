highest=0
second_highest=0
for i in range(1,6):
    Salary = float(input("Enter your salary:"))
    if Salary>highest:
      second_highest=highest
      highest=Salary
    elif Salary>second_highest and Salary!=highest:
       second_highest=Salary

print("Second Highest Salary is:",second_highest)
print("Highest Salary is:",highest)
