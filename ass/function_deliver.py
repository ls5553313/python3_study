def myadd(x,y):
    return x + y
def mymul(x,y):
    return x * y
def get_op(s):
    if s == '+':
        return myadd
    if s == '*':
        return mymul

def main():
    while True:
        s = input("pls input: ")
        l = s.split()
        print(l)
        a,s,b = l

        fn = get_op(s)
        print("the result is ", fn(int(a),int(b)))

main()