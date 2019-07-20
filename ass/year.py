year = int(input("year:"))
if (not year % 4 and year % 100) or not year % 400: 
    print("yes")
else:
    print("no")