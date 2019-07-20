for i in range(100):
    if i * (i + 1) % 11 == 8:
        print(i)

i = 0
j = 0
for i in range(1, 100, 2):
    j += i
print(j)

i = 1
j = 0
while i < 100:
    j = j + i
    i += 2
print(j)

