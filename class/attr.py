class car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    def get_car_attr(self,attr_name):
        return getattr(self,attr_name,None)

c1 = car('black', 'benz')
v = c1.get_car_attr('color')
print(v)
v = c1.get_car_attr('name')
print(v)
v = c1.get_car_attr('brand')
print(v)