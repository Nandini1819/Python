def analyze_marks(*args):
    if len(args)==0:
        print("invalid")
        return
    total=0
    highest = args[0]
    passing_count = 0

    for mark in args:
       total = total + mark
       if mark>highest:
        highest = mark
       if mark >=40:
        passing_count = passing_count +1
    average = total/len(args)
    return
    print("Total:",total)
    print("average:",average)
    print("highest:",highest)
    print("Passing count",passing_count)

