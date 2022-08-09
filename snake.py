from random import randrange
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (57, 255, 20)
RED = (255, 8, 0)

points_for_apple = [
    25,
    75,
    125,
    175,
    225,
    275,
    325,
    375,
    425,
    475,
    525,
    575,
    625,
    675,
    725,
    775,
]


def drawSnake(points):
    for point in points:
        x, y = point
        rect = pygame.Rect(x, y, 50, 50)
        rect.center = (x, y)
        pygame.draw.rect(WIN, GREEN, rect)


def drawApple(x, y):
    rect = pygame.Rect(x, y, 50, 50)
    rect.center = (x, y)
    pygame.draw.rect(WIN, RED, rect)


def main():
    run = True
    clock = pygame.time.Clock()

    grow = False

    snake_x = WIDTH / 2 + 25
    snake_y = HEIGHT / 2 + 25
    apple_x = snake_x + 150
    apple_y = snake_y

    points = [(snake_x, snake_y), (snake_x - 50, snake_y), (snake_x - 100, snake_y)]

    direction = ""

    x_change = 0
    y_change = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction is not "right" and direction is not "left":
                    x_change -= 50
                    y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction is not "left" and direction is not "right":
                    x_change += 50
                    y_change = 0
                    direction = "right"
                elif event.key == pygame.K_DOWN and direction is not "up" and direction is not "down":
                    y_change += 50
                    x_change = 0
                    direction = "down"
                elif event.key == pygame.K_UP and direction is not "down" and direction is not "up":
                    y_change -= 50
                    x_change = 0
                    direction = "up"

        snake_x += x_change
        snake_y += y_change

        if (apple_x, apple_y) == points[0]:
            grow = True
            i = randrange(0, 15)
            j = randrange(0, 15)
            apple_x = points_for_apple[i]
            apple_y = points_for_apple[j]

            while (apple_x, apple_y) in points:
                i = randrange(0, 15)
                j = randrange(0, 15)
                apple_x = points_for_apple[i]
                apple_y = points_for_apple[j]

        if x_change != 0 or y_change != 0:
            if grow == False:
                points.insert(0, (snake_x, snake_y))
                points.pop()
            else:
                points.insert(0, (snake_x, snake_y))
                grow = False

        if snake_x < 25 or snake_y < 25 or snake_x > 775 or snake_y > 775:
            snake_x = WIDTH / 2 + 25
            snake_y = HEIGHT / 2 + 25
            apple_x = snake_x + 150
            apple_y = snake_y

            points = [
                (snake_x, snake_y),
                (snake_x - 50, snake_y),
                (snake_x - 100, snake_y),
            ]

            direction = ""

            x_change = 0
            y_change = 0

        for i in range(1, len(points)):
            x, y = points[0]
            if points[i] == (x, y):
                snake_x = WIDTH / 2 + 25
                snake_y = HEIGHT / 2 + 25
                apple_x = snake_x + 150
                apple_y = snake_y

                points = [
                    (snake_x, snake_y),
                    (snake_x - 50, snake_y),
                    (snake_x - 100, snake_y),
                ]

                direction = ""

                x_change = 0
                y_change = 0
                break

        WIN.fill(BLACK)
        drawApple(apple_x, apple_y)
        drawSnake(points)

        pygame.display.update()

        clock.tick(15)

    pygame.quit()


main()
