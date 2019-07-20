def get_score():
    try:
        i = int(input("pls input: "))
        if -1 < i < 101:
            return(i)
        else:
            return('1error')
    except:
        return('2error')

print(get_score())
  