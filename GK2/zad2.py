import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Z-Shaped Figure")



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))

    pygame.draw.rect(win, "red", (150, 150, 300, 15))

    pygame.draw.rect(win, "red", (150, 450, 300, 15))

    diagonal_surface = pygame.Surface((420, 15), pygame.SRCALPHA)
    diagonal_surface.fill("red")
    rotated_diagonal = pygame.transform.rotate(diagonal_surface, 45)
    win.blit(rotated_diagonal, (145, 155))

    pygame.display.update()

pygame.quit()