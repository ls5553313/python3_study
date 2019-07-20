def print_list(l):
    L1 = []
    for x in l:
        if len(str(x)) > 1:
            L1 += print_list(x)
        else:
           L1.append(x)
    return(L1)

L = [[3,5,8],2,3,[2,3,3]]
print(print_list(L))
print(sum(print_list(L)))