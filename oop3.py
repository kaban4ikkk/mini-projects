from random import randint

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)


class Man:

    def __init__(self, name, nickname):
        self.name = name  # имя
        self.money = 10  # з/п
        self.foodcat = 0  # еда для кота
        self.nickname = nickname
        self.nickname = nickname
        self.fullnesscat = 30
        self.hose = 0

    def __str__(self):
        return 'я - {}, у меня {} денег'.format(self.name, self.money)

    def work(self):
        print('{} сходил на работу, купил коту еды {}'.format(self.name,
                                                              self.foodcat))
        self.money += 20
        self.foodcat += 5

    def act(self):
        if self.foodcat <= 0:
            print('кот умер(')
            return
        dice = randint(1, 5)
        if self.foodcat <= 1:
            if dice == 1 or dice == 3:
                self.work()
        else:
            print('{} умер'.format(self.nickname))

    def hunger(self):
        self.fullnesscat += 20
        self.money -= 5
        if self.fullnesscat <= 0:
            print('кот {} умер(')
        else:
            print('кот {} сыт и доволен, денег осталось {})'.format(self.nickname, self.money))

    def sleep(self):
        print('{} спит'.format(self.nickname))
        self.fullnesscat -= 10

    def eat(self):
        print('{} ест'.format(self.nickname))
        self.fullnesscat += 10


man = Man(name='Дима', nickname='Борис')

for day in range(1, 366):
    print('=========================== день{} ==========================='.format(day))
    man.act()
    print(man)


**************************************************************************************************
class Man:

    def __init__(self, name, cash = 190, hongry = 100, clear = 200, food = 50):
        self.name = name
        self.cash = cash
        self.hongry = hongry
        self.clear = clear
        self.food = food
    def __str__(self):
        return "меня зовут: {}".format(self.name)

    def cat_food(self):
        return "кол-во кошачьей еды: {}".format(self.food)


    def mony(self, n):
        print("деньги :{}".format(self.cash))
        if n == 'пойти на работу' or 'Пойти на работу':
            self.cash += 50
            return f" кол-во денег: {self.cash}"
        else:
            return print("вы не пошли на работу, денег осталось: {}".format(self.cash))

    def up_cat(self):
        return "вы подобрали кота, у него есть дом"

    def pay_food(self, food):
        if isinstance(food, (int)):
            if food == 'купить еды':
                self.cash -= 50
                return f"кол-во денег после покупки: {self.cash}"
            else:
                return f"кол-во денег не изменилось: {self.cash}"
        else:
            return ValueError("введите число)")

    def clear_up(self, derty):
        if isinstance(derty, (str)):
            print("вы хотите убраться в доме?")
            if derty == "да":
                self.hongry -= 20
                self.clear -= 100
                return print("в доме стало чище: {}, но я проголодался: {}".format(self.clear, self.hongry))
            else:
                return print('ничего не изменилось')
        else:
            return ValueError("вы ввели число)")
class Cat(Man):
    def __init__(self, nikname):
        super().__init__(nikname)
        self.eat = 20
        self.nikname = nikname
    def __str__(self):
        return "имя для кота: {}".format(self.nikname)

    def eat_up(self):
        self.eat += 20
        self.food -= 10
        return "сытость кота : {}, кол-во кошачьей еды в доме: {}".format(self.eat, self.food)

    def sleep_up(self):
        self.eat -= 10
        return "сытость кота уменьшилась: {}".format(self.eat)

    def fuck(self):
        f"{self.nikname} дерёт обои!"
        self.eat -= 10
        self.clear += 5
        return f"сытость {self.nikname} составляет: {self.eat}, степень грязи в доме {self.clear} "

man = Man(input("как тебя зовут?"))
