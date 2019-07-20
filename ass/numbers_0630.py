def input_numbers():
    try:
        file = open('numbers.txt','w')
        while True:
            i1 = int(input('pls input an int: '))
            if i1 < 0:
                break
            s_write = str(i1) + '\n'
            print(s_write)
            file.write(s_write)
        file.close()
    except:
        print('os error')

def output_numbers():
    try:
        file = open('numbers.txt','r')
        l1 = file.readlines()
        l2 = []
        for x in l1:
            l2.append(int(x))
        print(l2)
    except:
        print('os error')
    return(l2)
   
  

def main():
    #input_numbers()
    output_numbers()
    print(max(output_numbers()))
    print(min(output_numbers()))
    print(sum(output_numbers()))
if __name__ == '__main__':
    main()