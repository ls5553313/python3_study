def myrange(begin, end = None, step = 1):
    if end == None:
        end = begin
        begin = 0

    while begin < end:
        yield begin
        begin += step

    while begin > end and step < 0: 
        yield begin
        begin += step

print([x for x in myrange(10,-1,-1)])
print([x for x in range(10,-1,1.5)])
print()
