suspicious_count = 0
total_value = 0
for i in range(1,9):
    amount = float(input("Enter Transaction amount:"))
    if amount > 100000:
        print("Suspicious Transaction")
        suspicious_count = suspicious_count + 1
        total_value = total_value + amount
    else:
        print("Normal Transaction")
print("Suspicious Transactions:",suspicious_count)
print("Total value of Suspicious Transactions:",total_value)