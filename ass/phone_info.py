def input_phone_info():
    s = ''
    try:
        f = open('my_phone_info.txt','w')
    except:
        print('cant find the file')
    while True:
        s1 = input('pls input name: ')
        if not s1:
            break
        s2 = input('pls input phone number: ')
        while len(s2) != 11:
            s2 = input('pls input phone number again: ')
        s += s1 + ':' + s2 + '\n'
    #s = s[0:-1]
    print(s)
    f.write(s)
    f.close()

def output_phone_info():
    try:
        f = open('my_phone_info.txt')
    except:
        print('cant find file')
    name_max_len = 0
    L = f.readlines()
    print(L)
    for x in L:
        if len(x) > name_max_len:
            print(len(x))
            name_max_len = len(x)
    name_max_len -= 13
    for x in L:
        print('| ' + x[0:-13].center(name_max_len) + ' | ' 
             + x[-12:-2] + ' |')
    




    f.close()
def main():
    #input_phone_info()
    output_phone_info()
    
    


if __name__ == '__main__':
    main()