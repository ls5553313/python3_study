weight = float(input("weight:"))
high = float(input("high:"))
BMI = round(weight / high**2, 2)
if BMI < 18.5:
    print(BMI, "  less")
elif BMI > 24:
    print(BMI, "  more")
else:
    print(BMI, "  OK")