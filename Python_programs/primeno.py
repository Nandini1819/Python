Number=int(input("Enter a number to check prime or not: "));
for i in range(2,Number+1):
    if(Number%i==0):
        print("The given number is prime")
        break;
    else:
        print("The given number is not prime")
        break;