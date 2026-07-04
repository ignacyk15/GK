import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 1")

wielokat_surf = pygame.Surface((300, 300), pygame.SRCALPHA)
punkty = []

for i in range(17):
    kat = i * (2 * math.pi / 17)
    x = 150 + 150 * math.cos(kat)
    y = 150 + 150 * math.sin(kat)
    punkty.append((x, y))

pygame.draw.polygon(wielokat_surf, (255, 255, 0), punkty)
pygame.draw.polygon(wielokat_surf, (0, 0, 0), punkty, 3)

run = True
tryb = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                tryb = event.key

    win.fill((255, 255, 255))
    
    surf = wielokat_surf
    x, y = 150, 150

    if tryb == pygame.K_1:
        surf = pygame.transform.scale(wielokat_surf, (150, 150))
        x, y = 225, 225
    elif tryb == pygame.K_2:
        surf = pygame.transform.rotozoom(wielokat_surf, 45, 1)
        r = surf.get_rect()
        x, y = 300 - r.width // 2, 300 - r.height // 2
    elif tryb == pygame.K_3:
        surf = pygame.transform.scale(pygame.transform.flip(wielokat_surf, False, True), (200, 200))
        x, y = 200, 200
    elif tryb == pygame.K_4:
        surf = pygame.transform.scale(wielokat_surf, (300, 100))
        x, y = 150, 250
    elif tryb == pygame.K_5:
        surf = pygame.transform.scale(wielokat_surf, (300, 50))
        x, y = 150, 100
    elif tryb == pygame.K_6:
        surf = pygame.transform.scale(wielokat_surf, (100, 300))
        x, y = 250, 150
    elif tryb == pygame.K_7:
        surf = pygame.transform.scale(pygame.transform.flip(wielokat_surf, True, True), (150, 150))
        x, y = 225, 225
    elif tryb == pygame.K_8:
        surf = pygame.transform.rotozoom(wielokat_surf, -45, 0.5)
        r = surf.get_rect()
        x, y = 300 - r.width // 2, 300 - r.height // 2
    elif tryb == pygame.K_9:
        surf = pygame.transform.flip(wielokat_surf, True, False)
        x, y = 150, 150

    win.blit(surf, (x, y))
    pygame.display.update()

pygame.quit()