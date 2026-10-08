Age=int(input("Enter your age: "));
isvotingcard=input("Do you have a voting card answer should be in true or false:").lower()=="true"

if(Age>=18 and isvotingcard):
    print("Eligible for voting")
    
else:
    print("Not Eligible for voting")