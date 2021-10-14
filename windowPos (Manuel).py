#u/Starbuck5c sur r/pygame

import pygame
from pygame._sdl2 import Window

screen = pygame.display.set_mode((100, 100))
window = Window.from_display_module()

clock = pygame.time.Clock()

while True:
    screen.fill("purple")
    print(window.position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
    clock.tick(144)
