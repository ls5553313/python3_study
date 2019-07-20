print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))

for i in range(26):
    x = 65 + i
    print(chr(x), end = "")
print()
for i in range(26):
    x = 65 + i
    print(chr(x), end = "")
    print(chr(x + 32), end = "")
print()