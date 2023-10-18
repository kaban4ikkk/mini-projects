from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
import sys


# Создание окна приложения
class SnakeGame(QMainWindow):
    def __init__(self):
        super(SnakeGame, self).__init__()
        
        # Создание области рисования
        self.canvas = Canvas(self)
        
        # Создание строки состояния для отображения статистики игры
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(False)
        
        
        # Настройка строки состояния
        self.status.setStyleSheet("background-color: #9AA6A7; border: 1px solid black")
        
        # Соединение диалогового окна соообщения со строкой состояния
        self.canvas.signal[str].connect(self.status.showMessage)
        
        # Добавление области рисования в окно приложения
        self.setCentralWidget(self.canvas)
        
        # Добавление заголовка
        self.setWindowTitle("Змейка")
        
        # Установка геометрии окна
        self.setGeometry(100, 100, 600, 400)
        
        # Запуск области рисования
        self.canvas.start()
        
        # Показ окна приложения
        self.show()

# Создание класса области рисования
class Canvas(QFrame):
    # Создание пользовательского сигнала
    signal = pyqtSignal(str)
    
    # Скорость змейки
    SPEED = 70
    
    # Ширина сегмента змейки
    S_WIDTH = 60
    
    # Высота сегмента змейки
    S_HEIGHT = 40
    
    # Конструктор класса
    def __init__(self, parent):
        super(Canvas, self).__init__(parent)
        
        # Создание таймера
        self.timer = QBasicTimer()
        
        # Массив змейки
        self.snake = [[7, 11], [5, 12]]
        
        # Текущая координата x головы змейки
        self.cur_x_head = self.snake[0][0]
        
        # Текущая координата y головы змейки
        self.cur_y_head = self.snake[0][1]
        
        # Список яблок
        self.apple = []
        
        # Флаг роста
        self.grow = False
        
        # Направление
        self.direct = 2
        
        # Вызов метода установки яблока
        self.drop_apple()
        
        # Установка фокуса
        self.setFocusPolicy(Qt.StrongFocus)
        
    # Ширина квадрата
    def square_width(self):
        return self.contentsRect().width() / Canvas.S_WIDTH
        
    # Высота квадрата
    def square_height(self):
        return self.contentsRect().height() / Canvas.S_HEIGHT
        
    # Запуск игры
    def start(self):
        # Отправка сообщения строке состояния
        self.signal.emit(str(len(self.snake) - 2))
            
        # Запуск таймера
        self.timer.start(Canvas.SPEED, self)
            
    # Переопределение метода paintEvent
    def paintEvent(self, event):
        # Создание инструмента рисования
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
            
        # Получение области рисования
        rect = self.contentsRect()
            
            
        # Верх области рисования
        canvas_top = rect.bottom() - Canvas.S_HEIGHT * self.square_height()
            
        # Прорисовка змейки
        for pos in self.snake:
            self.draw_square(painter, rect.left() + pos[0] * self.square_width(), 
                             canvas_top + pos[1] * self.square_height())
            
        # Прорисовка яблок
        for pos in self.apple:
            self.draw_ellipse(painter, rect.left() + pos[0] * self.square_width(), 
                              canvas_top + pos[1] * self.square_height())


    # Рисование яблока
    def draw_ellipse(self, painter, x, y):
        # Установка цвета яблока
        color = QColor("red")
        painter.setPen(QPen(color))
        painter.setBrush(QBrush(Qt.red))
        # Прорисовка яблока
        painter.drawEllipse(x + 1, y + 1, 
                            self.square_width() - 2, 
                            self.square_height() - 2)
        
            
    # Рисование квадрата
    def draw_square(self, painter, x, y):
        # Установка цвета змейки
        color_first = QColor(Qt.green)
        color_second = QColor(Qt.blue)
        # Установка градиента заливки змейки
        gradient = QConicalGradient(self.square_width() / 2, self.square_height() / 2, 0)
        gradient.setColorAt(0, color_first)
        gradient.setColorAt(0.4, color_second)
        gradient.setColorAt(0.8, color_second)
        gradient.setColorAt(1, color_first)
        
        # Установка стиля пера
        style = Qt.PenStyle.NoPen
        painter.setPen(QPen(style))
        # Установка кисти
        painter.setBrush(gradient)
        
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Прорисовка сегмента змейки
        painter.drawRect(x + 1, y + 1, 
                         self.square_width() + 1, 
                         self.square_height() + 1)

                
    # Переопределение обработчика нажатия клавиши клавиатуры
    def keyPressEvent(self, event):
        # Получение кода клавиши
        key = event.key()
                
        # Если нажата левая клавиша
        if key == Qt.Key_Left:
            # Если направление не вправо
            if self.direct != 2:
                # Установка направления влево
                self.direct = 1
        # Если нажата правая клавиша
        elif key == Qt.Key_Right:
            # Если направление не влево
            if self.direct != 1:
                # Установка направления вправо
                self.direct = 2
        # Если нажата нижняя клавиша
        elif key == Qt.Key_Down:
            # Если направление не вверх
            if self.direct != 4:
                # Установка направления вниз
                self.direct = 3
        # Если нажата верхняя клавиша
        elif key == Qt.Key_Up:
            # Если направление не вниз
            if self.direct != 3:
                # Установка направления вверх
                self.direct = 4
              
                
    # Перемещение змейки
    def move(self):
        # Поворот влево
        if self.direct == 1:
            self.cur_x_head, self.cur_y_head = self.cur_x_head - 1, self.cur_y_head
            # Выход за границы области рисования
            if self.cur_x_head < 0:
                self.stop_game()
        # Поворот направо
        if self.direct == 2:
            self.cur_x_head, self.cur_y_head = self.cur_x_head + 1, self.cur_y_head
            # Выход за границы области рисования
            if self.cur_x_head == Canvas.S_WIDTH:
                self.stop_game()
        # Поворот вниз
        if self.direct == 3:
            self.cur_x_head, self.cur_y_head = self.cur_x_head, self.cur_y_head + 1
            # Выход за границы области рисования
            if self.cur_y_head == Canvas.S_HEIGHT:
                self.stop_game()
        # Поворот вверх
        if self.direct == 4:
            self.cur_x_head, self.cur_y_head = self.cur_x_head, self.cur_y_head - 1
            # Выход за границы области рисования
            if self.cur_y_head < 0:
                self.stop_game()
                    
        # Изменение положения головы змейки
        head = [self.cur_x_head, self.cur_y_head]
            
        # Изменение головы змейки
        self.snake.insert(0, head)
            
        # Удаление последнего сегмента змейки
        if not self.grow:
            self.snake.pop()
        else:
            self.signal.emit(str(len(self.snake) - 2))
            self.grow = False
            
            
    # Переопределение метода timerEvent
    def timerEvent(self, event):
        # Проверка идентификатора таймера
        if event.timerId() == self.timer.timerId():
            self.move()
            self.is_apple_collision()
            self.is_snake_collision()
            # Обновление окна приложения
            self.update()
        
        
    # Проверка на столкновение змейки с самой собой
    def is_snake_collision(self):
        # Пересечение змейки
        for i in range(1, len(self.snake)):
            if self.snake[i] == self.snake[0]:
                self.stop_game()
    
    def stop_game(self):
        # Сообщение об окончании игры
                self.signal.emit(str("Конец игры! Итоговое количество очков: " + str(len(self.snake) - 2)))
                # Затемнение области рисования
                self.setStyleSheet("background-color: black")
                # Остановка таймера
                self.timer.stop()
                # Обновление окна приложения
                self.update()
                    
        
    # Проверка пересечения змейки и яблока
    def is_apple_collision(self):
        for pos in self.apple:
            if pos == self.snake[0]:
                # Удаление яблока
                self.apple.remove(pos)
                # Повторное размещение яблока
                self.drop_apple()
                self.grow = True
        
        
    # Установка яблока в области рисования
    def drop_apple(self):
        # Выбор произвольных координат
        x = random.randint(2, 57)
        y = random.randint(2, 36)
        # Попытка разместить яблоко в области рисования
        for pos in self.snake:
            # Если координаты змейки и яблока равны
            if pos == [x, y]:
                # Новая попытка размещения яблока
                self.drop_apple()
        # Добавление нового яблока
        self.apple.append([x, y])