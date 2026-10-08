total_days = int(input("Enter total working days:"))
present_days = 0;
absent_days = 0;
for day in range(1,total_days+1):
    attendance = int(input("Enter 1 for present and 0 for absent:"))
if attendance==1:
    present_days = present_days+1
elif attendance==0:
    absent_days = absent_days+1
else:
    print("Invalid input")
attendance_percentage = (present_days/total_days)*100

print("present days:",present_days)
print("absent days:",absent_days)
print("attendance percentage:",attendance_percentage)