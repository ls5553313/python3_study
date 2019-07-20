

def myreverse(s):
    s1 = ""
    return(s1.join(sorted(s, reverse = True)))

L = ['aqwe', 'asd', 'zxc']
print(list(map(myreverse, L)))