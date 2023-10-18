import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры игрового поля
GAME_WIDTH = 600
GAME_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Размер одной клетки
CELL_SIZE = 20

# Скорость змейки
SNAKE_SPEED = 20

# Создание игрового поля
game_display = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Змейка")


# Объект змейки
class Snake:
    def __init__(self):
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT // 2
        self.direction = "RIGHT"
        self.body = []
        self.length = 1

    def move(self):
        if self.direction == "RIGHT":
            self.x += CELL_SIZE
        elif self.direction == "LEFT":
            self.x -= CELL_SIZE
        elif self.direction == "UP":
            self.y -= CELL_SIZE
        elif self.direction == "DOWN":
            self.y += CELL_SIZE

    def increase_length(self):
        self.length += 1

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(game_display, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(game_display, BLACK, (self.x, self.y, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        if self.x >= GAME_WIDTH or self.x < 0 or self.y >= GAME_HEIGHT or self.y < 0:
            return True
        for i in range(1, len(self.body)):
            if self.x == self.body[i][0] and self.y == self.body[i][1]:
                return True
        return False


# Объект еды
class Food:
    def __init__(self):
        self.x = random.randint(0, GAME_WIDTH - CELL_SIZE) // CELL_SIZE * CELL_SIZE
        self.y = random.randint(0, GAME_HEIGHT - CELL_SIZE) // CELL_SIZE * CELL_SIZE

    def draw(self):
        pygame.draw.rect(game_display, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))


# Функция обработки событий
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
            elif event.key == pygame.K_UP:
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN:
                snake.direction = "DOWN"


# Обновление экрана
def update_screen():
    game_display.fill(WHITE)
    snake.draw()
    food.draw()
    pygame.display.update()


# Создание объектов
snake = Snake()
food = Food()

# Главный игровой цикл
clock = pygame.time.Clock()
game_over = False

while not game_over:
    handle_events()

    snake.move()

    if snake.check_collision():
        game_over = True

    if snake.x == food.x and snake.y == food.y:
        snake.increase_length()
        food = Food()

    snake.body.append((snake.x, snake.y))
    if len(snake.body) > snake.length:
        del snake.body[0]

    update_screen()

    clock.tick(SNAKE_SPEED)

# Завершение игры
pygame.quit()
