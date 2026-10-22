low = 0
medium = 0
high = 0
for i in range(1,11):
    amount = float(input("Enter Transaction Amount:"))
    if amount < 10000:
        print("Low Risk")
        low = low+1
    elif amount < 50000:
        print("Medium Risk")
        medium = medium+1
    else:
        print("High Risk")
        high = high+1
print("Low Risk Transactions:",low)
print("Medium Risk Transactions:",medium)
print("Low Risk Transactions:",high)

     