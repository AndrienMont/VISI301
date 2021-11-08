import pygame
import sys
import labyrinthe as laby
import dessinLaby as dessLab
from pygame.locals import *
from labyrinthe import *
from dessinLaby import*
import random



vel = 1

class perso:

    
        def __init__(self): # Chargement du sprite et definition de sa position
         
            self.personnage = pygame.image.load('perso.png').convert_alpha()
            self.personnage = pygame.transform.scale(self.personnage , (20, 20))
            self.X = 0
            self.Y = 0
         
        def update (self):                      # Ajout d'une fonction Update
         
            self.position = (self.X,self.Y)
 
         
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
    fin = pygame.image.load('fin.png')
    

    origine_x = 0
    origine_y = 0
    tailleCase = 20
    fin = pygame.transform.scale(fin , (tailleCase,tailleCase))
    couleur = (0,0,0)
    difficulte = 10
    dedale = laby.generateMaze(difficulte,difficulte)
    laby.drawMaze(dedale)

    dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale, 10,10,screen)

    
    loop = True
    while loop:
        for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False
                if joueur.X == 180 and joueur.Y == 180:
                    loop = False
                    
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if yAMur(dedale,joueur.X,joueur.Y,"left"):
                                print("collision")
                        else:
                                joueur.bouge("gauche")
                    
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        if yAMur(dedale,joueur.X,joueur.Y,"right"):
                                print("collision")
                        else:
                                joueur.bouge("droite")
                    
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        if yAMur(dedale,joueur.X,joueur.Y,"up"):
                                print("collision")
                        else:
                                joueur.bouge("haut")
                    
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        if yAMur(dedale,joueur.X,joueur.Y,"down"):
                                print("collision")
                        else:
                                joueur.bouge("bas")
                
                        
        screen.fill(couleur)
        dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale, 10,10,screen)
        screen.blit(fin , ((tailleCase*difficulte-tailleCase),(tailleCase*difficulte-tailleCase)))
        screen.blit(joueur.personnage , (joueur.X*tailleCase, joueur.Y*tailleCase))
        pygame.display.update()             
                    
    pygame.quit()




main()



