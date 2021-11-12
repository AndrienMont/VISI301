import pygame
import sys
import labyrinthe as laby
import dessinLaby as dessLab
from pygame.locals import *
from random import*


tailleCase = 20
vel = 1

class perso:

    
        def __init__(self): # Chargement du sprite et definition de sa position
         
            self.personnage = pygame.image.load('perso.png').convert_alpha()
            self.personnage = pygame.transform.scale(self.personnage , (tailleCase, tailleCase))
            self.X = 0
            self.Y = 0
         

        def update (self):                      
         
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
    pygame.key.set_repeat(400, 100)
    
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption("Prototype Alpha-1 du projet MazeRunner")
    joueur = perso()
    fin = pygame.image.load('fin.png')
    

    origine_x = 0
    origine_y = 0
    posXmax = 0
    posYmax = 0
    fin = pygame.transform.scale(fin , (tailleCase,tailleCase))
    taille = 10
    caseFin = tailleCase*taille-tailleCase
    couleur = (0,0,0)
    dedale = laby.generateMaze(taille,taille)
    laby.drawMaze(dedale) 

    
    loop = True
    while loop:
        for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if laby.yAMur(dedale,joueur.X,joueur.Y,"left"):
                                print("collision")
                        else:
                                joueur.bouge("gauche")
                    
                    if event.key == K_RIGHT:
                        if laby.yAMur(dedale,joueur.X,joueur.Y,"right"):
                                print("collision")
                        else:
                                joueur.bouge("droite")
                    
                    if event.key == K_UP:
                        if laby.yAMur(dedale,joueur.X,joueur.Y,"up"):
                                print("collision")
                        else:
                                joueur.bouge("haut")
                    
                    if event.key == K_DOWN:
                        if laby.yAMur(dedale,joueur.X,joueur.Y,"down"):
                                print("collision")
                        else:
                                joueur.bouge("bas")

                if joueur.X > posXmax:
                        posXmax = joueur.X

                if joueur.Y > posYmax:
                        posYmax = joueur.Y
                        
                if joueur.X*tailleCase == caseFin and joueur.Y*tailleCase == caseFin:
                        loop = False
                

#Affichage
                        
        screen.fill(couleur)
        screen.blit(fin , (caseFin,caseFin))
        dessLab.affiche_case(origine_x,origine_y,tailleCase,dedale, 10,10,screen,joueur.X,joueur.Y)
        screen.blit(joueur.personnage , (joueur.X*tailleCase, joueur.Y*tailleCase))
        pygame.display.update()
        
    pygame.quit()

        


main()



