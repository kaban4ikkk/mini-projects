import math
class Line():

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distans(self):
        print(math.sqrt((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2))

    def slope(self):
        print(self.coor2[0] / self.coor1[0])

my = Line(coor1 = (3, 2), coor2 = (8, 10))
print(my.distans())
print()
print(my.slope())

#####################################################################################################

import math
class Cylinder():

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def vol(self):
        print(math.pi * self.radius ** 2 * self.height)

    def area(self):
        print((2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius ** 2))

my = Cylinder(2, 3)

print(my.vol())
print()
print(my.area())


#####################################################################################################

class Account():

    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    def n(self):
        print("Имя владельца:", self.name)

    def balans(self):
        print("Счёт в банке :", self.bank)

    def up(self):
        n = int(input())
        print("Внесение выполнено:", n)
        print('Счёт в банке:', self.bank + n)

    def los(self):
        n = int(input())
        if n > self.bank:
            print('Недостаточно средств!')
        else:
            print('Снятие со счёта:', self.bank - n)

my_Account = Account(name= input(), bank= int(input()))

print(my_Account.n())
print(my_Account.balans())
print(my_Account.up())
print(my_Account.los())