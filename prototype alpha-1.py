import pygame
import sys
import labyrinthe as laby
import dessinLaby2 as dessLab
from pygame.locals import *
from random import*


tailleCase = 60
vel = 1

def estDansListe(liste, element):
        res = False
        i = 0
        while (i<len(liste) and not res):
                res = element == liste[i]
                i = i + 1
        return res

def revelerCouloirs(maze_F4, posX_F4, posY_F4):

        res = []
        tile = (posX_F4, posY_F4)
        while not laby.yAMur(maze_F4, tile[0], tile[1], "left"):
                res = res + [tile]
                tile = (tile[0]-1, tile[1])
        res = res + [tile]

        tile = (posX_F4, posY_F4)
        while not laby.yAMur(maze_F4, tile[0], tile[1], "right"):
                res = res + [tile]
                tile = (tile[0]+1, tile[1])
        res = res + [tile]

        tile = (posX_F4, posY_F4)
        while not laby.yAMur(maze_F4, tile[0], tile[1], "up"):
                res = res + [tile]
                tile = (tile[0], tile[1]-1)
        res = res + [tile]

        tile = (posX_F4, posY_F4)
        while not laby.yAMur(maze_F4, tile[0], tile[1], "down"):
                res = res + [tile]
                tile = (tile[0], tile[1]+1)
        res = res + [tile]

        return res
               

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
    posXY = []
    fin = pygame.transform.scale(fin , (tailleCase,tailleCase))
    taille = 10
    dedale = laby.generateMaze(taille,taille)
    laby.drawMaze(dedale)
    
    DepArr = dessLab.randDepArr(origine_x,origine_y,tailleCase,dedale)
    
    caseFinX = DepArr[1][0]*tailleCase
    caseFinY = DepArr[1][1]*tailleCase
    caseFin =(caseFinX,caseFinY)
    couleur = (0,0,0)
    

    
    print(DepArr)
    print(DepArr[0][0])
    print(DepArr[1])
    joueur.X = DepArr[0][0]
    joueur.Y = DepArr[0][1]

    
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
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y))
                                #posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_RIGHT:
                        if laby.yAMur(dedale,joueur.X,joueur.Y,"right"):
                                print("collision")
                        else:
                                joueur.bouge("droite")
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y))
                                #posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_UP:
                        if laby.yAMur(dedale,joueur.X,joueur.Y,"up"):
                                print("collision")
                        else:
                                joueur.bouge("haut")
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y))
                                #posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_DOWN:
                        if laby.yAMur(dedale,joueur.X,joueur.Y,"down"):
                                print("collision")
                        else:
                                joueur.bouge("bas")
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y))
                                #posXY = posXY + [[joueur.X,joueur.Y]]
                        
                if joueur.X*tailleCase == caseFinX and joueur.Y*tailleCase == caseFinY:
                        loop = False
                

#Affichage

                    
        screen.fill(couleur)
        screen.blit(fin , caseFin)
        for i in range(len(posXY)):
                posX = posXY[i][0]
                posY = posXY[i][1]
                #dessLab.affiche_case(origine_x,origine_y,tailleCase,dedale,screen,posX,posY)
                dessLab.affiche_case_V2(posX, posY, origine_x, origine_y, tailleCase, dedale, screen)
        #dessLab.dessineDedale_V2(0, 0, tailleCase, dedale, screen)
        screen.blit(joueur.personnage , (joueur.X*tailleCase, joueur.Y*tailleCase))
        pygame.display.update()
        

    pygame.quit()


main()



