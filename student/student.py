from class_student import student


def input_student_info():
    while True:
        input_name = input('pls input name: ')
        if not input_name:
            break

        input_age = int(input('pls input age: '))
        while (not isinstance(int(input_age), int) 
                   or input_age < 0 
                   or input_age >150): 
            print('age is not acceptable.')
            input_age = int(input('pls input age again: '))

        input_score = int(input('pls input score: '))
        while (not isinstance(input_score, int) 
                   or input_score < 0 or input_score >100): 
            print('score is not acceptable.')
            input_score = int(input('pls input score again: '))  

        x = student(input_name,input_age,input_score)
        yield x

def save_student_info(filename = 'student_info.txt'):
    try:
        file = open(filename, 'w')
        for i in input_student_info():
            i.write_to_file(file)
        file.close()
    except OSError:
        print('OS error')

def show_student_info(filename):
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.rstrip()
            name, age, score = line.split(',')
            print(name, age, score)
        file.close()
    except:
        print('OS error')

def modify_student_info(filename,name,age,score):
    try:
        file = open(filename,'r+')
        for line in file:
            line = line.rstrip()
            name1, age1, score1 = line.split(',')
            if name1 == name:
                file.write(name)
                file.write(',')
                file.write(str(age))
                file.write(',')
                file.write(str(score))
                file.write('\n')
        file.close()
    except OSError:
        print('OS error')


        #file = open('student_info.txt', 'w')
        #file.write(x)


def main():
    #input_student_info()
    #save_student_info()
    #show_student_info('student_info.txt')
    modify_student_info('student_info.txt','abc',333,111)



if __name__ == '__main__':
    main()
