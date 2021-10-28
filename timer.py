import pygame
from pygame.locals import *

pygame.init()


window = pygame.display.set_mode((200, 200)) #Crée la fenêtre
clock = pygame.time.Clock() #Initialise l'horloge de pygame
font = pygame.font.SysFont(None, 100)
counter = 10 #Le temps à décompter
text = font.render(str(counter), True, (0, 128, 0)) #Spécificités pour l'affichage du compteur

timer_event = pygame.USEREVENT+1 #Définition de l'id de l'event 
pygame.time.set_timer(timer_event, 1000) #initialisation du timer

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event: #Si l'event se déroule, alors ....
            counter -= 1
            text = font.render(str(counter), True, (0, 128, 0))
            if counter == 0: #si le compteur arrive à 0, alors ...
                pygame.time.set_timer(timer_event, 0)
                print('game over!')
                run = False
                      

    window.fill((255, 255, 255))
    text_rect = text.get_rect(center = window.get_rect().center)
    window.blit(text, text_rect)
    pygame.display.flip()
pygame.quit()


