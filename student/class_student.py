class student:
    l = []
    def __init__(self, name,age,score):
        self.name = name
        self.age= age
        self.score= score
        
    @classmethod
    def show_student_info(cls):
        print(cls.l)
    @classmethod
    def save_student_info(cls,name,age,score):
        cls.l.append((name,age,score))
    @classmethod
    def show_avg_score(cls):
        l_score = []
        for x in cls.l:
            l_score.append(int(x[2]))
            print(l_score)
            print(sum(l_score)/len(l_score))
    def write_to_file(self,file):
        i_write = (str(self.name) 
                       + ',' + str(self.age) 
                       + ',' + str(self.score) + '\n')
        file.write(i_write)


def main():
    s1 = student('xiaozhang',22,11000)
    s1.save_student_info(s1.name,s1.age,s1.score)
    s1.show_student_info()
    s2 = student('xiaowang',23,99)
    s2.save_student_info(s2.name,s2.age,s2.score)
    student.show_student_info()
    print(len(student.l))
    student.show_avg_score()
if __name__ == '__main__':
    main()