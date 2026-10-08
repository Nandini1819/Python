age=int(input("Enter your age:"))
monthly_income=float(input("Enter your monthly income:"))
credit_score=int(input("Enter your credit score:"))
existing_loan=float(input("Enter the amount of existing loan:"))
employment_year=int(input("Enter your employment year:"))

if age<21:
    print("Loan status:Rejected")
    print("Reason:Age is below required limit")
elif monthly_income<30000:
    print("Loan status:Rejected")
    print("Reason:monthly income is below required limit")
elif credit_score<700:
    print("Loan status:Rejected")
    print("Reason:credit score is below required limit")
elif employment_year<2:
    print("Loan status:Rejected")
    print("Reason:employment year is below required limit")
else:
    ("Loan status:Approved")
if credit_score>=750:
    print("Low interest")
else:
    print("normal intresest")
if existing_loan==0:
    print("Normal processing")
else:
    print("Additional processing")
if credit_score>700:
    print("Risk level:low")
else:
    print("Risk level:high")