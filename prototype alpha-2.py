import pygame
from pygame.locals import *
import os
import sys
import labyrinthe as laby2D
import dessinLaby2 as dessLab
from pygame.locals import *
from random import*
from labyrinthe3DPrototype import*
from pathFinding3D import*


tailleCase = 80

def estDansListe(liste, element):
        res = False
        i = 0
        while (i<len(liste) and not res):
                if (element[0] == liste[i][0] and element[1] == liste[i][1]):
                        res = True
                i = i + 1
        return res

def revelerCouloirs(maze_F4, posX_F4, posY_F4, posZ_F4, baseTiles):

        tile = (posX_F4, posY_F4, posZ_F4)
        while not laby2D.yAMur(maze_F4, tile[0], tile[1], "left"):
                if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])
                tile = (tile[0]-1, tile[1], posZ_F4)
        if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])

        tile = (posX_F4, posY_F4, posZ_F4)
        while not laby2D.yAMur(maze_F4, tile[0], tile[1], "right"):
                if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])
                tile = (tile[0]+1, tile[1], posZ_F4)
        if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])

        tile = (posX_F4, posY_F4, posZ_F4)
        while not laby2D.yAMur(maze_F4, tile[0], tile[1], "up"):
                if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])
                tile = (tile[0], tile[1]-1, posZ_F4)
        if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])

        tile = (posX_F4, posY_F4, posZ_F4)
        while not laby2D.yAMur(maze_F4, tile[0], tile[1], "down"):
                if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])
                tile = (tile[0], tile[1]+1, posZ_F4)
        if not estDansListe(baseTiles, tile):
                        baseTiles.extend([tile])
        #print(len(baseTiles))


               
class perso:

    
        def __init__(self): # Chargement du sprite et definition de sa position
                
                
                self.sprite_idle_1 = pygame.image.load('bob/idle_1.png').convert_alpha()
                self.sprite_idle_1 = pygame.transform.scale(self.sprite_idle_1 , (tailleCase, tailleCase))
                
                self.sprite_idle_2 = pygame.image.load('bob/idle_2.png').convert_alpha()
                self.sprite_idle_2 = pygame.transform.scale(self.sprite_idle_2 , (tailleCase, tailleCase))

                self.sprite_idle_3 = pygame.image.load('bob/idle_3.png').convert_alpha()
                self.sprite_idle_3 = pygame.transform.scale(self.sprite_idle_3 , (tailleCase, tailleCase))
                
                self.sprite_idle_4 = pygame.image.load('bob/idle_4.png').convert_alpha()
                self.sprite_idle_4 = pygame.transform.scale(self.sprite_idle_4 , (tailleCase, tailleCase))
                
                self.X = 0
                self.Y = 0
                self.Z = 0

                self.spriteX = 0
                self.spriteY = 0

                self.regardeGauche = False
         

        def update (self):

                self.position = (self.X,self.Y)
 
         
        def bouge (self, direction):  # Definition d'un fonction pour faire bouger le sprite
             
                if direction == 'droite':               
                    #self.direct = self.personnage
                    self.X += 1
                    self.regardeGauche = False
                if direction == 'gauche':
                    #self.direct = self.personnage
                    self.X -= 1
                    self.regardeGauche = True
                if direction == "haut":
                    #self.direct = self.personnage
                    self.Y -= 1
                if direction == "bas":
                    #self.direct = self.personnage
                    self.Y += 1

                if direction == "low":
                    self.Z -= 1

                if direction == "high":
                    self.Z += 1


def main():
    pygame.init()
     
    os.environ['SDL_VIDEO_CENTERED'] = '1'
     
    screen_width=700
    screen_height=700
    screen=pygame.display.set_mode((screen_width, screen_height))
    
    clock = pygame.time.Clock()
    counter = 0
    timer_event = pygame.USEREVENT+1 #Définition de l'id de l'event
    pygame.time.set_timer(timer_event, 1000) #initialisation du timer

    score = 3000
    NbDeplacements = 0 
     
    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
     
        return newText
     
     
    white=(255, 255, 255)
    black=(0, 0, 0)
    gray=(50, 50, 50)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    yellow=(255, 255, 0)
     
    font = "Retro.ttf"

    
    jeu = False
    menu=True
    selected="jouer"

    while menu:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            pygame.quit()
                            quit()
                    if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_UP:
                                    selected="jouer"
                            elif event.key==pygame.K_DOWN:
                                    selected="quitter"
                            if event.key==pygame.K_RETURN:
                                if selected=="jouer":
                                        jeu = True
                                        menu = False
                                if selected=="quitter":
                                        pygame.quit()
                                        quit()
     
            screen.fill(blue)
            title=text_format("MazeRunner", font, 90 , yellow)
            if selected=="jouer":
                text_start=text_format("JOUER", font, 75, white)
            else:
                text_start = text_format("JOUER", font, 75, black)
            if selected=="quitter":
                text_quit=text_format("QUITTER", font, 75, white)
            else:
                text_quit = text_format("QUITTER", font, 75, black)
     
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()
     
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
            screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
            screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
            pygame.display.update()
            pygame.display.set_caption("Prototype Alpha-2 du projet MazeRunner")
     
        


    pygame.key.set_repeat(400, 100)
    
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

    #MODIF
    spriteCycle = 0

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
    revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y, joueur.Z, posXY)

    def recolterEclats(listeEclats):
        i_ = 0
        quantiteEclatsRecoltes = 0
        while (i_<len(listeEclats)): #Eclat
                if joueur.X == listeEclats[i_][0] and joueur.Y == listeEclats[i_][1] and joueur.Z == listeEclats[i_][2] :
                        del listeEclats[i_]
                        quantiteEclatsRecoltes = quantiteEclatsRecoltes + 1 #shard_amount += 1
                        i_ = i_ - 1
                i_ = i_ + 1
        return quantiteEclatsRecoltes
    

    
    while jeu:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == QUIT:
                    jeu = False

                if event.type == timer_event: #Si l'event se déroule, alors ....
                        counter += 1

                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"left"):
                                joueur.bouge("gauche")
                                revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y, joueur.Z, posXY)
                                NbDeplacements = NbDeplacements + 1 
                                shard_amount = shard_amount + recolterEclats(Eclat)
                    
                    if event.key == K_RIGHT:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"right"):
                                joueur.bouge("droite")
                                revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y, joueur.Z, posXY)
                                NbDeplacements = NbDeplacements + 1 
                                shard_amount = shard_amount + recolterEclats(Eclat)
                    
                    if event.key == K_UP:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"up"):
                                joueur.bouge("haut")
                                revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y, joueur.Z, posXY)
                                NbDeplacements = NbDeplacements + 1 
                                shard_amount = shard_amount + recolterEclats(Eclat)
                    
                    if event.key == K_DOWN:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"down"):
                                joueur.bouge("bas")
                                revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y, joueur.Z, posXY)
                                NbDeplacements = NbDeplacements + 1 
                                shard_amount = shard_amount + recolterEclats(Eclat)
                                
                    if event.key == K_l:
                        if not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"low"):
                                joueur.bouge("low")
                                revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y, joueur.Z, posXY)
                                NbDeplacements = NbDeplacements + 1 
                                shard_amount = shard_amount + recolterEclats(Eclat)
                                
                                
                    if event.key == K_h:
                        if  not yAMur(dedale,joueur.X,joueur.Y,joueur.Z,"high"):
                                joueur.bouge("high")
                                revelerCouloirs(dedale[joueur.Z], joueur.X, joueur.Y, joueur.Z, posXY)
                                NbDeplacements = NbDeplacements + 1 
                                shard_amount = shard_amount + recolterEclats(Eclat)
                        
                if (joueur.X*tailleCase == caseFinX and joueur.Y*tailleCase == caseFinY and joueur.Z*tailleCase == caseFinZ) and shard_amount >= 3 :
                        jeu = False
                

#Affichage

                    
        screen.fill(couleur)

        for i in range(len(posXY)):
                 posX = posXY[i][0]
                 posY = posXY[i][1]
                 dessLab.affiche_case_V2_3D(posX, posY, joueur.Z, origine_x, origine_y, tailleCase, dedale, screen)
        

        if Eclat:
                for i in range(0,len(Eclat)) :
                        if joueur.Z == Eclat[i][2] :
                                screen.blit(shard, (Eclat[i][0]*tailleCase,Eclat[i][1]*tailleCase))

        if joueur.Z*tailleCase == caseFinZ :
                screen.blit(fin , caseFin)

        if joueur.spriteX != joueur.X:
                joueur.spriteX = joueur.spriteX + (joueur.X - joueur.spriteX)/5
                if abs(joueur.X - joueur.spriteX) < 0.05:
                        joueur.spriteX = joueur.X

        if joueur.spriteY != joueur.Y:
                joueur.spriteY = joueur.spriteY + (joueur.Y - joueur.spriteY)/5
                if abs(joueur.Y - joueur.spriteY) < 0.05:
                        joueur.spriteY = joueur.Y

        spriteCyclePeriod = 30
        if spriteCycle < spriteCyclePeriod/2:
                if joueur.regardeGauche:
                        screen.blit(joueur.sprite_idle_3 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))
                else:
                        screen.blit(joueur.sprite_idle_1 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))
                        
        elif spriteCycle < spriteCyclePeriod:
                if joueur.regardeGauche:
                        screen.blit(joueur.sprite_idle_4 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))
                else:
                        screen.blit(joueur.sprite_idle_2 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))
        else:
                spriteCycle = 0
        spriteCycle = spriteCycle + 1

        screen.blit(myfont.render(str(shard_amount),1,(255,0,0)),(250,520))
        screen.blit(myfont.render(" éclat(s)",1,(255,0,0)),(260,520))
        screen.blit(myfont.render("Vous êtes actuellement à l'étage n°",1,(255,0,0)),(50,540))
        screen.blit(myfont.render(str(joueur.Z),1,(255,0,0)),(365,540))
        screen.blit(myfont.render(" du labyrinthe",1,(255,0,0)),(375,540))

        screen.blit(text, (0,400))
        screen.blit(cmd1, (20,430))
        screen.blit(cmd2, (20,460))
        screen.blit(cmd3, (20,490))
        pygame.display.update()

    score = score - NbDeplacements -  counter
    print("votre score est de :")
    print(score)
    pygame.quit()


main()



