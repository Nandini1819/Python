highest = 0
lowest = 100
for i in range(1,7):
    Score = float(input("Enter Perfomance Score:"))
    if Score >= 90:
        print("Excellent")
    elif Score >= 75:
        print("Good")
    elif Score >=50:
        print("Average")
    else:
        print("Poor")
    if Score > highest:
      highest = Score
    if Score < lowest:
      lowest = Score
print("Highest Score:",highest)
print("Lowest Score:",lowest)