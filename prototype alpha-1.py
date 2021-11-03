import pygame
import sys
import labyrinthe as laby
import dessinLaby as dessLab
from pygame.locals import *


vel = 4

class perso:

    
        def __init__(self): # Chargement du sprite et definition de sa position
         
            self.personnage = pygame.image.load('perso.png').convert_alpha()
            self.personnage = pygame.transform.scale(self.personnage , (20, 20))
            self.rect = self.personnage.get_rect()
            self.X = 0
            self.Y = 0
         
        def update (self):                      # Ajout d'une fonction Update
         
            self.position = (self.X,self.Y)
            self.rect = pygame.Rect(self.position, (100,100))      # Mise a jour du Rect par rapport à sa nouvelle position
 
         
        def bouge (self, direction):  # Definition d'un fonction pour faire bouger le sprite
             
                if direction == 'droite':               
                    self.direct = self.personnage
                    self.X += vel
                if direction == 'gauche':
                    self.direct = self.personnage
                    self.X -= vel
                if direction == "haut":
                    self.direct = self.personnage
                    self.Y -= vel
                if direction == "bas":
                    self.direct = self.personnage
                    self.Y += vel



        

def main():

    pygame.init()
    # Effectuer un deplacement plusieurs fois en laissant appuyé sur la touche
    pygame.key.set_repeat(400, 100)
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption("Prototype Alpha-1 du projet MazeRunner")
    joueur = perso()

    origine_x = 0
    origine_y = 0
    tailleCase = 20
    couleur = (0,0,0)

    dedale = laby.generateMaze(10,10)
    laby.drawMaze(dedale)

    dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale, 10,10,screen)

    
    loop = True
    while loop:
        for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        joueur.update()
                        joueur.bouge("gauche")
                    
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        joueur.update()
                        joueur.bouge("droite")
                    
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        joueur.update()
                        joueur.bouge("haut")
                    
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        joueur.update()
                        joueur.bouge("bas")
                        
        screen.fill(couleur)
        dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale, 10,10,screen)
        screen.blit(joueur.personnage , (joueur.X, joueur.Y))
        pygame.display.update()             
        
    pygame.quit()




main()



