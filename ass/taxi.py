km = int(input ("please input km:"))
if km < 3:
    print("the price is", 13, "yuan")
elif 3 <= km <= 15:
    print("the price is", round((km-3)*2.3 + 13), "yuan")
elif km > 15:
    print("the price is", round(12*2.3 + 13 + (km - 15)*3.45), "yuan")
else:
    print("km is not valid")