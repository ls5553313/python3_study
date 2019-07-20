score1 = int(input("请输入第一个成绩："))
score2 = int(input("请输入第2个成绩："))
score3 = int(input("请输入第3个成绩："))
if score1 > score2 and score1 > score3:
    print("the highest score is", score1)
elif score2 > score1 and score2 > score3:
    print("the highest score is", score2)
elif score3 > score1 and score3 > score2:
    print("the highest score is", score3)
if score1 < score2 and score1 < score3:
    print("the lowest score is", score1)
elif score2 < score1 and score2 < score3:
    print("the lowest score is", score2)
elif score3 < score1 and score3 < score2:
    print("the lowest score is", score3)
print("the average is ",(score3 + score1 + score2)/3)
    