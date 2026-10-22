successful = 0
rejected = 0
for i in range(1,11):
    amount = int(input("Enter Withdrawal amount:"))
    if amount<=0:
        print("Rejected-Invalid Amount")
        rejected = rejected +1
    elif amount % 500 != 0:
        print("Rejected-Amount must be multiple of 500")
        rejected = rejected + 1
    elif amount>=20000:
        print("Rejected-Maximum Withdrawal limit is 20000")
        rejected = rejected + 1
    else:
        print("Withdrawal Successful")
        successful = successful + 1
print("Successful Transactions:",successful)
print("Rejected Transactions:",rejected)



     