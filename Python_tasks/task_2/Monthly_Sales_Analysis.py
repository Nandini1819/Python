total_sales = 0
highest = 0
lowest = 0
high_sales_months = 0

for month in range(1,13):
    Sales = float(input("Enter sales for month:"))
    total_sales = total_sales + Sales

    if month == 1:
      highest = Sales
      lowest = Sales

    if Sales>highest:
      highest = Sales

    if Sales<lowest:
      lowest = Sales

    if Sales>100000:
      high_sales_months = high_sales_months+1

average_sales = total_sales/12
percentage = (high_sales_months/12)*100

print("Total Anual sales:",total_sales)
print("Average Monthly Sales:",average_sales)
print("Highest Monthly Sales:",highest)
print("Lowest Monthly Sales:",lowest)
print("Months with Sales above 10000:",high_sales_months)
print("Percentage of high sales Months:",percentage)