def generate():
    while True:
        s = str(input("pls input: "))
        if not s:
            break
        yield s
s = ''
for x in enumerate(generate()):
    index,element = x
    s += str(index+1)+ '.' + element + '\n'
    print(s)
