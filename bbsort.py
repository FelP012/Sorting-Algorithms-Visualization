import pygame
import random

pygame.init()

win = pygame.display.set_mode((665, 500))

pygame.display.set_caption("Bubble sort")

programIcon = pygame.image.load("bubble.png")

pygame.display.set_icon(programIcon)

cant_rect = 20
x = 30
y = 30
width = 25
run = True
height = []

for k in range(cant_rect):
    height.append(random.randint(10, 200) * 2)


def setup_array(h):
    for c in range(cant_rect):
        h[c] = random.randint(10, 200) * 2


def show(h):
    for m in range(len(h)):
        pygame.draw.rect(win, (0, 100, 255), (x + 30 * m, y, width, h[m]))


def color(h):
    for f in range(len(h)):
        pygame.draw.rect(win, (255, 0, 100), (x + 30 * f, y, width, h[f]))

    pygame.display.update()


def array_sorted(arr):
    n = len(arr)

    if n == 1 or n == 0:
        return True

    return arr[0] <= arr[1] and array_sorted(arr[1:])


while run:

    execute = False

    pygame.time.delay(5)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        execute = True

    if not execute:

        win.fill((0, 0, 0))

        if not array_sorted(height):
            show(height)
        else:
            win.fill((0, 0, 0))
            color(height)
            pygame.time.delay(1000)
            setup_array(height)

        pygame.display.update()

    elif not array_sorted(height) and execute:

        for i in range(len(height) - 1):

            for j in range(len(height) - i - 1):

                if height[j] > height[j + 1]:
                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t

                win.fill((0, 0, 0))

                show(height)

                pygame.time.delay(100)

                pygame.display.update()
        win.fill((0, 0, 0))
        color(height)
        pygame.time.delay(1000)
        setup_array(height)
        pygame.display.update()

pygame.quit()
