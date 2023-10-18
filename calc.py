import math

class Calculator:

    def __init__(self, a = int(input()), b = int(input())):

        self.a = a
        self.b = b

    def addition(self): #сложение

        print(f"сложение: {self.a} + {self.b} = {self.a + self.b}")

    def subtraction(self): #вычитание

        print(f"вычитание: {self.a} - {self.b} = {self.a - self.b}")

    def multiplication(self): #умножение

        print(f"умножение: {self.a} * {self.b} = {self.a * self.b}")

    def division(self): #деление

        if self.b == 0:
            print(f"делить на {self.b} нельзя!")

        else:
            print(f"деление: {self.a} ÷ {self.b} = {self.a // self.b}")

    def degree(self): #степень

        print(f"квадрат: {self.a}² = {self.a ** 2}")

    def fraction(self):

        if self.b == 0:
            print(f"делить на {self.b} нельзя!")

        else:
            print(f"дробь: 1/{self.b} = {1 / self.b} ")

    def root(self): #корень

        if self.a < 0:
            print("введите значение больше 0")

        else:
            print(f"корень √{self.a} = {math.sqrt(self.a)}")


obj = Calculator()

print(obj.addition())
print()

print(obj.subtraction())
print()

print(obj.multiplication())
print()

print(obj.division())
print()

print(obj.degree())
print()

print(obj.fraction())
print()

print(obj.root())
print()