class student:   
    def __init__(self, name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def set_student_info(self, name, age):
        self.name = name
        self.age = age
    def show_student_info(self):
        print(self.name + ':', self.age)
    def set_score(self, score):
        self.score = score
        print(self.name, ':',self.score)
    def show_info(self):
        print(self.name, ':',self.age,':',self.score)


#s1 = student()
#s1.set_student_info('xiaoli',20)
#s1.show_student_info()
#s2 = student()
#s2.set_student_info('xiaola',2222)
#s2.show_student_info()
s1 = student('aaaaa',12,100)
s1.show_info()
s1.set_score(80)
s1.show_info()

        