salaries = [25000,45000,30000,60000,50000]
a = salaries.copy()
for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_index]:
            min_index = j
    a[i],a[min_index] = a[min_index],a[i]
print("Seletion sort:",a)
print("Top 5 Salaries:",a[::-1])

b = salaries.copy()
for i in range(len(b)):
    for j in range(len(b)-i-1):
        if b[j] > b[j+1] :
            b[j],b[j+1] = b[j+1],b[j]
print("Bubble sort:",b)