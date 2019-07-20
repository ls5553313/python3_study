class bicycle:
    def __init__(self,name):
        self.name = name
    def run(self, km):
        print(self.name,'has ride',km,'KM by legs')
class Ebicycle(bicycle):
    volume = 0
    def __init__(self,name):
        super().__init__(name)
    def Charge(self,vol):
        Ebicycle.volume += vol
        print(name, 'charged',vol, 'now volume is',Ebicycle.volume)
    def run(self,km):
        if km <= 10 * Ebicycle.volume:
            print(name,'ride',km,'KM by electricity')
            Ebicycle.volume -= km/10
        if km > 10 * Ebicycle.volume:
            print(self.name,'ride',10 * Ebicycle.volume,'KM by electricity')
            super().run(km - 10 * Ebicycle.volume)
            Ebicycle.volume = 0
        print('current volume:', Ebicycle.volume)
def main():
    b1 = bicycle('b1')
    b1.run(10)
    b2 = Ebicycle('b2')
    #b2.Charge(100)
    b2.run(60)


if __name__ == '__main__':
    main()