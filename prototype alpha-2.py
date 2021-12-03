import pygame
import sys
import labyrinthe as laby
import dessinLaby as dessLab
from pygame.locals import *
from random import*
from labyrinthe3DPrototype import*


tailleCase = 30
vel = 1

class perso:

    
        def __init__(self): # Chargement du sprite et definition de sa position
         
            self.personnage = pygame.image.load('perso.png').convert_alpha()
            self.personnage = pygame.transform.scale(self.personnage , (tailleCase, tailleCase))
            self.X = 0
            self.Y = 0
            self.Z = 2
         

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
    pygame.display.set_caption("Prototype Alpha-2 du projet MazeRunner")
    joueur = perso()
    fin = pygame.image.load('fin.png')
    

    origine_x = 0
    origine_y = 0
    posXY = []
    fin = pygame.transform.scale(fin , (tailleCase,tailleCase))
    taille = 3
    dedale = generateMaze(taille,taille,taille)
    drawMaze(dedale)
    
    dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale[joueur.Z],screen,3,3)
    print(dedale)
    
    caseFinX = 2*tailleCase
    caseFinY = 2*tailleCase
    caseFin =(caseFinX,caseFinY)
    couleur = (0,0,0)
    
    loop = True
    while loop:
        for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"left"):
                                joueur.bouge("gauche")
                                posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_RIGHT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"right"):
                                joueur.bouge("droite")
                                posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_UP:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"up"):
                                joueur.bouge("haut")
                                posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_DOWN:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"down"):
                                joueur.bouge("bas")
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                
                    if event.key == K_f:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"low"):
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                joueur.Z = joueur.Z -1 
                                
                                
                    if event.key == K_e:
                        if  not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"high"):
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                joueur.Z = joueur.Z +1 
                        
                if joueur.X*tailleCase == caseFinX and joueur.Y*tailleCase == caseFinY:
                        loop = False
                

#Affichage

                    
        screen.fill(couleur)
        screen.blit(fin , caseFin)
        dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale[joueur.Z],screen,3,3)
        screen.blit(joueur.personnage , (joueur.X*tailleCase, joueur.Y*tailleCase))
        pygame.display.update()
        

    pygame.quit()


main()



