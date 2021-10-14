import pygame
from pygame.locals import *

width = 100
height = 100

FPS = 10
FramePerSec = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

while True:
        screen.fill((255,255,255))
        screen = pygame.display.set_mode((200, 200), pygame.RESIZABLE)

        width, height = pygame.display.get_surface().get_size()
        print(str(width) + " " + str(height))
        
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
        #pygame.draw.circle(screen, color(255,255,255), (80,50),  30)
        pygame.display.update()
        FramePerSec.tick(FPS)
