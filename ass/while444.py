i = 1
j = 0
while i <= 1000000:
    j = j + 1 / (2 * i - 1) * (- 1)**(i + 1)
    i += 1
print(j)
print(4 * j)
