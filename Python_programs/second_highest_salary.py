highest = 0
second_highest = 0
for i in range(1,6):
    salary=float(input("Enter your salary:"))
if salary>highest:
    second_highest=highest
    highest=salary
    