import pygame
import sys
import labyrinthe as laby
import dessinLaby2 as dessLab
from pygame.locals import *
from random import*
from labyrinthe3DPrototype import*
from pathFinding3D import*


tailleCase = 60

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
                if not estDansListe(res, [tile]):
                        res = res + [tile]
                tile = (tile[0]-1, tile[1])

        tile = (posX_F4, posY_F4)
        while not laby.yAMur(maze_F4, tile[0], tile[1], "right"):
                if not estDansListe(res, [tile]):
                        res = res + [tile]
                tile = (tile[0]+1, tile[1])

        tile = (posX_F4, posY_F4)
        while not laby.yAMur(maze_F4, tile[0], tile[1], "up"):
                if not estDansListe(res, [tile]):
                        res = res + [tile]
                tile = (tile[0], tile[1]-1)

        tile = (posX_F4, posY_F4)
        while not laby.yAMur(maze_F4, tile[0], tile[1], "down"):
                tile = (tile[0], tile[1]+1)
                if not estDansListe(res, [tile]):
                        res = res + [tile]

        return res

               
class perso:

    
        def __init__(self): # Chargement du sprite et definition de sa position
                
                
                self.personnage = pygame.image.load('square.png').convert_alpha()
                self.personnage = pygame.transform.scale(self.personnage , (tailleCase, tailleCase))
                self.X = 0
                self.Y = 0
                self.Z = 0

                self.spriteX = 0
                self.spriteY = 0
         

        def update (self):

                self.position = (self.X,self.Y)
 
         
        def bouge (self, direction):  # Definition d'un fonction pour faire bouger le sprite
             
                if direction == 'droite':               
                    self.direct = self.personnage
                    self.X += 1
                if direction == 'gauche':
                    self.direct = self.personnage
                    self.X -= 1
                if direction == "haut":
                    self.direct = self.personnage
                    self.Y -= 1
                if direction == "bas":
                    self.direct = self.personnage
                    self.Y += 1

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

    shard = pygame.image.load("shard.png")
    shard = pygame.transform.scale(shard,(tailleCase,tailleCase))

    origine_x = 0
    origine_y = 0
    nbEtages = 2
    posXY = []
    shard_amount = 0
    fin = pygame.transform.scale(fin , (tailleCase,tailleCase))
    taille = 5
    dedale = generateMaze(taille,taille,taille)
    drawMaze(dedale)

    #Position des éclats
    xS1 = randint(0,taille-1)
    yS1 = randint(0,taille-1)
    zS1 = randint(0,nbEtages)
    xS2 = randint(0,taille-1)
    yS2 = randint(0,taille-1)
    zS2 = randint(0,nbEtages)
    xS3 = randint(0,taille-1)
    yS3 = randint(0,taille-1)
    zS3 = randint(0,nbEtages)

    Eclat = [(xS1,yS1,zS1),(xS2,yS2,zS2),(xS3,yS3,zS3)]

    myfont = pygame.font.SysFont("monospace",15)
    

    
    DepArr = dessLab.randDepArr3D(origine_x,origine_y,nbEtages,tailleCase,dedale)

    
    dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale[joueur.Z],screen,3,3)
    #print(dedale)

    
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

    font = pygame.font.Font(None, 24)
    text = font.render("Voici les commandes", 1, (255,255,255))
    cmd1 = font.render("Utilisez les flêches directionnelles pour se déplacer",1,(255,255,255))
    cmd2 = font.render("Utilisez H pour monter d'un étage lorsque vous êtes sur une échelle montante", 1, (255,255,255))
    cmd3 = font.render("Utilisez L pour descendre d'un étage lorsque vous êtes sur une échelle descendante", 1, (255,255,255))

    

    
    loop = True
    while loop:
        for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"left"):
                                joueur.bouge("gauche")
                                posXY.extend(revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                for i in range(0,len(Eclat)):
                                        if joueur.X == Eclat[i][0] and joueur.Y == Eclat[i][1] and joueur.Z == Eclat[i][2] :
                                                del Eclat[i]
                                                shard_amount += 1
                    
                    if event.key == K_RIGHT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"right"):
                                joueur.bouge("droite")
                                posXY.extend(revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                for i in range(0,len(Eclat)):
                                        if joueur.X == Eclat[i][0] and joueur.Y == Eclat[i][1] and joueur.Z == Eclat[i][2] :
                                                del Eclat[i]
                                                shard_amount += 1
                    
                    if event.key == K_UP:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"up"):
                                joueur.bouge("haut")
                                posXY.extend(revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                for i in range(0,len(Eclat)):
                                        if joueur.X == Eclat[i][0] and joueur.Y == Eclat[i][1] and joueur.Z == Eclat[i][2] :
                                                del Eclat[i]
                                                shard_amount += 1
                    
                    if event.key == K_DOWN:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"down"):
                                joueur.bouge("bas")
                                posXY.extend(revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y))
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                for i in range(0,len(Eclat)):
                                        if joueur.X == Eclat[i][0] and joueur.Y == Eclat[i][1] and joueur.Z == Eclat[i][2] :
                                                del Eclat[i]
                                                shard_amount += 1
                                
                    if event.key == K_l:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"low"):
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                joueur.bouge("low")
                                for i in range(0,len(Eclat)):
                                        if joueur.X == Eclat[i][0] and joueur.Y == Eclat[i][1] and joueur.Z == Eclat[i][2] :
                                                del Eclat[i]
                                                shard_amount += 1
                                
                                
                    if event.key == K_h:
                        if  not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"high"):
                                posXY = posXY + [[joueur.X,joueur.Y]]
                                joueur.bouge("high")
                                for i in range(0,len(Eclat)):
                                        if joueur.X == Eclat[i][0] and joueur.Y == Eclat[i][1] and joueur.Z == Eclat[i][2] :
                                                del Eclat[i]
                                                shard_amount += 1
                        
                if (joueur.X*tailleCase == caseFinX and joueur.Y*tailleCase == caseFinY and joueur.Z*tailleCase == caseFinZ) and shard_amount >= 3 :
                        loop = False
                

#Affichage

                    
        screen.fill(couleur)

        if Eclat:
                for i in range(0,len(Eclat)) :
                        if joueur.Z == Eclat[i][2] :
                                screen.blit(shard, (Eclat[i][0]*tailleCase,Eclat[i][1]*tailleCase))
        

        for i in range(len(posXY)):
                posX = posXY[i][0]
                posY = posXY[i][1]
                dessLab.affiche_case_V2_3D(posX, posY, joueur.Z, origine_x, origine_y, tailleCase, dedale, screen)

        if joueur.Z*tailleCase == caseFinZ :
                screen.blit(fin , caseFin)

        if joueur.spriteX != joueur.X:
                joueur.spriteX = joueur.spriteX + (joueur.X - joueur.spriteX)/3
                if abs(joueur.X - joueur.spriteX) < 0.05:
                        joueur.spriteX = joueur.X

        if joueur.spriteY != joueur.Y:
                joueur.spriteY = joueur.spriteY + (joueur.Y - joueur.spriteY)/3
                if abs(joueur.Y - joueur.spriteY) < 0.05:
                        joueur.spriteY = joueur.Y

                        
        screen.blit(joueur.personnage , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))

        screen.blit(myfont.render(str(shard_amount),1,(255,0,0)),(250,500))
        screen.blit(myfont.render(" éclat(s)",1,(255,0,0)),(260,500))
        screen.blit(myfont.render("Vous êtes actuellement à l'étage n°",1,(255,0,0)),(50,530))
        screen.blit(myfont.render(str(joueur.Z),1,(255,0,0)),(365,530))
        screen.blit(myfont.render(" du labyrinthe",1,(255,0,0)),(375,530))

        if joueur.Z*tailleCase == caseFinZ :
                screen.blit(fin , caseFin)
        screen.blit(text, (0,400))
        screen.blit(cmd1, (20,430))
        screen.blit(cmd2, (20,460))
        screen.blit(cmd3, (20,490))
        pygame.display.update()
        

    pygame.quit()


main()



