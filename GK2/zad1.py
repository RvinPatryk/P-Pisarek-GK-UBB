import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Moja Gra")


def draw_dodecagon(surface, color, center, radius, shear_x=0, shear_y=0):
    points = []
    for i in range(12):
        angle = i * 2 * math.pi / 12 + math.radians(rotation)
        x = center[0] + (radius * width_scale) * math.cos(angle)
        y = center[1] + (radius * height_scale) * math.sin(angle)

        # Dodanie efektu przesunięcia nożycowego
        x += shear_x * (y - center[1])
        y += shear_y * (x - center[0])

        points.append((x, y))
    pygame.draw.polygon(surface, color, points)


scale = 1
rotation = 0
width_scale = 1
height_scale = 1
move_x = 0
move_y = 0
shear_x = 0
shear_y = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scale = 0.5
                rotation = 0
                width_scale = 1
                height_scale = 1
                move_x = 0
                move_y = 0
                shear_x = 0
                shear_y = 0
            elif event.key == pygame.K_2:
                scale = 1
                rotation = 45
                width_scale = 1
                height_scale = 1
                move_x = 0
                move_y = 0
                shear_x = 0
                shear_y = 0
            elif event.key == pygame.K_3:
                scale = 1
                rotation = 180
                width_scale = 0.5
                height_scale = 1
                move_x = 0
                move_y = 0
                shear_x = 0
                shear_y = 0
            elif event.key == pygame.K_4:
                scale = 1
                rotation = 90
                width_scale = 1.5
                height_scale = 1.5
                move_x = 0
                move_y = 0
                shear_x = 0.4
                shear_y = 0
            elif event.key == pygame.K_5:
                scale = 1
                rotation = 0
                width_scale = 1
                height_scale = 0.5
                move_x = 0
                move_y = -225
                shear_x = 0
                shear_y = 0
            elif event.key == pygame.K_6:
                scale = 1.2
                rotation = 90
                width_scale = 0.8
                height_scale = 1.2
                move_x = 0
                move_y = 0
                shear_x = 0
                shear_y = 0.4
            elif event.key == pygame.K_7:
                scale = 0.6
                rotation = 180
                width_scale = 1
                height_scale = 2
                move_x = 0
                move_y = 0
                shear_x = 0
                shear_y = 0
            elif event.key == pygame.K_8:
                scale = 1
                rotation = 45
                width_scale = 1
                height_scale = 0.5
                move_x = 0
                move_y = 100
                shear_x = 0
                shear_y = 0
            elif event.key == pygame.K_9:
                scale = 1
                rotation = 180
                width_scale = 1
                height_scale = 1
                move_x = 100
                move_y = 0
                shear_x = -0.5
                shear_y = 0.5

    win.fill("yellow")
    draw_dodecagon(win, "blue", (300 + move_x, 300 + move_y), 150 * scale, shear_x, shear_y)
    pygame.display.update()

pygame.quit()