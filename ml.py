import time
import numpy as np
import matplotlib.pyplot as plt


def f(x):  # функция
    return x ** 2 - 5 * x + 1


def df(x):  # производная
    return 2 * x - 5


# определяю параметры алгоритма
N = int(input())  # число итераций
print(f"число итераций: {N}")

x_0 = int(input())  # начальное значение
print(f"начальное значение: {x_0}")

lmd = float(
    input())  # шаг сходимости(lmd должен быть = 0.1, 0,01, 0,001... "если взять шаг 1, то программа будет перескакивать т.лок. min")
while lmd < 1:
    print(f"шаг сходимости: {lmd}")
else:
    print("введите значение lmd < 1")
    lmd = float(input())

x_plt = np.arange(0, 10, 0.2)  # изменение аргумента
f_plt = [f(x) for x in x_plt]  # вызов функции(визуализация т-ки)

plt.ion()  # вкл график
fig, ax = plt.subplots()  # создание окна и осей графа
ax.grid(True)  # сетка на графике

ax.plot(x_plt, f_plt)  # отображение начального графа
point = ax.scatter(x_0, f(x_0), c='green')  # цвет точки на графе

# запуск алгоритма:

for i in range(N):
    x_0 = x_0 - lmd * df(x_0)  # изменение аргумента на текущей итерации
    point.set_offsets([x_0, f(x_0)])  # новое положение точки

    # рисовка графика и задержка(30мс)

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.03)  # задержка

plt.ioff()  # выкл отобр-ия графиков
print(x_0)
ax.scatter(x_0, f(x_0), c='red')
plt.show()
