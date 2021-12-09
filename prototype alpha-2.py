import pygame
import sys
import labyrinthe as laby
import dessinLaby2 as dessLab
from pygame.locals import *
from random import*
from labyrinthe3DPrototype import*
from pathFinding3D import*


tailleCase = 60
vel = 1



def estDansListe(liste, element):
        res = False
        i = 0
        while (i<len(liste) and not res):
                res = element == liste[i]
                i = i + 1
        return res

def revelerCouloirs(maze_F4, posX_F4, posY_F4,Z):

        res = []
        tile = (posX_F4, posY_F4)
        while not yAMur(maze_F4, tile[0], tile[1], "left",Z):
                res = res + [tile]
                tile = (tile[0]-1, tile[1])
        res = res + [tile]

        tile = (posX_F4, posY_F4)
        while not yAMur(maze_F4, tile[0], tile[1], "right",Z):
                res = res + [tile]
                tile = (tile[0]+1, tile[1])
        res = res + [tile]

        tile = (posX_F4, posY_F4)
        while not yAMur(maze_F4, tile[0], tile[1], "up",Z):
                res = res + [tile]
                tile = (tile[0], tile[1]-1)
        res = res + [tile]

        tile = (posX_F4, posY_F4)
        while not yAMur(maze_F4, tile[0], tile[1], "down",Z):
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
            self.Z = 0
         

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

                if direction == "low":
                    self.Z -= 1

                if direction == "high":
                    self.Z += 1




def main():

    pygame.init()
    pygame.key.set_repeat(400, 100)
    
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption("Prototype Alpha-2 du projet MazeRunner")
    joueur = perso()
    fin = pygame.image.load('fin.png')
    

    origine_x = 0
    origine_y = 0
    nbEtages = 2
    posXY = []
    fin = pygame.transform.scale(fin , (tailleCase,tailleCase))
    taille = 3
    dedale = generateMaze(taille,taille,taille)
    drawMaze(dedale)

    DepArr = dessLab.randDepArr3D(origine_x,origine_y,nbEtages,tailleCase,dedale)

    
    dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale[joueur.Z],screen,3,3)
    print(dedale)

    
    caseFinX = DepArr[1][0]*tailleCase
    caseFinY = DepArr[1][1]*tailleCase
    caseFinZ= DepArr[1][2]*tailleCase
    caseFin =(caseFinX,caseFinY)
    couleur = (0,0,0)

    print(DepArr)
    print(DepArr[0][0])
    print(DepArr[1])
    joueur.X = DepArr[0][0]
    joueur.Y = DepArr[0][1]
    joueur.Z = DepArr[0][2]
    print(joueur.X)
    print(joueur.Y)
    print(joueur.Z)
    

    
    loop = True
    while loop:
        for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"left"):
                                joueur.bouge("gauche")
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y,joueur.Z))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_RIGHT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"right"):
                                joueur.bouge("droite")
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y,joueur.Z))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_UP:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"up"):
                                joueur.bouge("haut")
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y,joueur.Z))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                    
                    if event.key == K_DOWN:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"down"):
                                joueur.bouge("bas")
                                posXY.extend(revelerCouloirs(dedale, joueur.X, joueur.Y,joueur.Z))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                
                    if event.key == K_l:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"low"):
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                joueur.Z = joueur.Z -1
                                
                                
                    if event.key == K_h:
                        if  not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"high"):
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                joueur.Z = joueur.Z +1
                        
                if joueur.X*tailleCase == caseFinX and joueur.Y*tailleCase == caseFinY and joueur.Z*tailleCase == caseFinZ :
                        loop = False
                

#Affichage

                    
        screen.fill(couleur)
        if joueur.Z*tailleCase == caseFinZ :
                screen.blit(fin , caseFin)
        for i in range(len(posXY)):
                posX = posXY[i][0]
                posY = posXY[i][1]
                dessLab.affiche_case_V2_3D(posX, posY,joueur.Z, origine_x, origine_y, tailleCase, dedale, screen)
        screen.blit(joueur.personnage , (joueur.X*tailleCase, joueur.Y*tailleCase))
        pygame.display.update()
        

    pygame.quit()


main()



