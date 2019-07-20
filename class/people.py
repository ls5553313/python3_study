class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def teach(self,someone,something):
        print(self.name, 'teach', someone, something)
    def make_money(self,method, money):
        print(self.name, 'earned', money, 'by',method)
    def lend(self, from_whom, money):
        print(self.name, 'lend', money, 'from',from_whom)
people1 = people('zhangsan', 35)
people2 = people('lisi', 18)
people1.teach(people2.name,'python')
people2.teach(people1.name,'tiaosheng')
people1.make_money('shangban',1000)
people2.lend(people1.name, 200)