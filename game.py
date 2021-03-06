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
lastScore= 0

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

def listeEstDansListe(listeFille, listeMere):
        """V??rifie si listeFille se trouve dans listeMere"""

        trouve = False
        if (len(listeMere) > len(listeFille)):
                i = 0
                while (i < len(listeMere)-len(listeFille)+1 and not trouve):
                        j = 0
                        itemCorrect = True
                        while (j < len(listeFille) and itemCorrect):
                                if not listeFille[j] == listeMere[j+i]:
                                        itemCorrect = False
                                j = j + 1
                        if itemCorrect:
                                trouve = True

                        i = i + 1
        return trouve
               
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

        def afficherSprite(self, fenetre, nbSprite, x_F1, y_F1):
                if nbSprite == 1:
                        fenetre.blit(self.sprite_idle_1 , (x_F1, y_F1))
                elif nbSprite == 2:
                        fenetre.blit(self.sprite_idle_2 , (x_F1, y_F1))
                elif nbSprite == 3:
                        fenetre.blit(self.sprite_idle_3 , (x_F1, y_F1))
                else:
                        fenetre.blit(self.sprite_idle_4 , (x_F1, y_F1))
#best = [0,0,0,0,0]

def main(taille):
    global lastScore
    #global best
    pygame.init()
     
    os.environ['SDL_VIDEO_CENTERED'] = '1'
     
    screen_width=700
    screen_height=700
    screen=pygame.display.set_mode((screen_width, screen_height))

    fileR = open("highscore.txt")
    lignes = fileR.read().splitlines()
    Hscore = int(lignes[-1])
    fileR.close()
    fileW = open("highscore.txt","a")

    if lastScore > Hscore :
        fileW.write(str(lastScore)+"\n")
        Hscore = lastScore

    
    fileW.close()



    #if lastScore > best[taille-4]:
     #       best[taille-4] = lastScore
    
    clock = pygame.time.Clock()
    counter = 0
    timer_event = pygame.USEREVENT+1 #D??finition de l'id de l'event
    pygame.time.set_timer(timer_event, 1000) #initialisation du timer

    score = 3000
    NbDeplacements = 0
    choice = 1

    font3 = pygame.font.Font("Retro.ttf", 40)
     
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
    #menuScores = False
    affiche_fin = True
    selected="jouer"

    while menu:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            pygame.quit()
                            quit()
                    if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_UP and choice > 0 :
                                    choice = choice-1
                            elif event.key==pygame.K_DOWN and choice < 3 :
                                    choice = choice+1
                            if choice == 1:
                                    selected="jouer"
                            #if choice == 2:
                            #        selected="scores"
                            if choice == 2:
                                    selected="quitter"
                            if event.key==pygame.K_RETURN:
                                if selected=="jouer":
                                        jeu = True
                                        menu = False
                                        #menuScores = False
                                """if selected=="scores":
                                        jeu = False
                                        menu = False
                                        menuScores = True"""
                                        
                                if selected=="quitter":
                                        pygame.quit()
                                        quit()
     
            screen.fill(blue)
            title=text_format("Project Dedalus", font, 90 , yellow)
            if selected=="jouer":
                text_start=text_format("JOUER", font, 75, white)
            else:
                text_start = text_format("JOUER", font, 75, black)
            """if selected=="scores":
                text_score=text_format("MEILLEURS SCORES", font, 75, white)
            else:
                text_score= text_format("MEILLEURS SCORES", font, 75, black)"""
            if selected=="quitter":
                text_quit=text_format("QUITTER", font, 75, white)
            else:
                text_quit = text_format("QUITTER", font, 75, black)

            scoreDisp = text_format("Score pr??c??dent : "+str(lastScore), font, 75, white)
            meilleurScore = text_format("Highscore : "+str(Hscore), font,75,white)
     
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            #score_rect=text_score.get_rect()
            quit_rect=text_quit.get_rect()
            score_rect=scoreDisp.get_rect()
            hscore_rect=meilleurScore.get_rect()
     
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
            screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 250))
            #screen.blit(text_score, (screen_width/3 - (start_rect[2]/2), 310))
            screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 370))
            screen.blit(scoreDisp, (screen_width/2 - (score_rect[2]/2), 2*screen_height/3))
            screen.blit(meilleurScore,(screen_width/2 - (hscore_rect[2]/2), 550))
            pygame.display.update()
            pygame.display.set_caption("Prototype Alpha-2 du projet MazeRunner")
     


    """while menuScores:
        for event in pygame.event.get():
                if event.type == QUIT:
                    menuScores = False
                    affiche_fin = False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        menuScores = False
                        menu = True
                        affiche_fin = False
                    
        screen.fill(blue)
        screen.blit(font3.render("Meilleur score des diff??rents labyrinthes", 1,yellow),(10,20))
        
        screen.blit(font3.render("Taille 3 : ", 1,black),(10,100))
        screen.blit(font3.render(str(best[0]), 1,black),(150,100))
        screen.blit(font3.render(" points", 1,black),(230,100))
        
        screen.blit(font3.render("Taille 4 : ", 1,black),(10,200))
        screen.blit(font3.render(str(best[1]), 1,black),(150,200))
        screen.blit(font3.render(" points", 1,black),(230,200))
        
        screen.blit(font3.render("Taille 5 : ", 1,black),(10,300))
        screen.blit(font3.render(str(best[2]), 1,black),(150,300))
        screen.blit(font3.render(" points", 1,black),(230,300))
        
        screen.blit(font3.render("Taille 6 : ", 1,black),(10,400))
        screen.blit(font3.render(str(best[3]), 1,black),(150,400))
        screen.blit(font3.render(" points", 1,black),(230,400))
        
        screen.blit(font3.render("Taille 7 : ", 1,black),(10,500))
        screen.blit(font3.render(str(best[4]), 1,black),(150,500))
        screen.blit(font3.render(" points", 1,black),(230,500))


        screen.blit(font3.render("Appuyez sur entr??e pour retourner au menu", 1,black),(50,600))        

        pygame.display.update()"""

                
    

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
    dedale = generateMaze(taille,taille,taille)
    drawMaze(dedale)

    #MODIF
    spriteCycle = 0

    myfont = pygame.font.SysFont("monospace",15)
    

    
    DepArr = dessLab.randDepArr3D(origine_x,origine_y,nbEtages,tailleCase,dedale)

    
    dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale[joueur.Z],screen,3,3)
    #print(dedale)

    caseFinX = DepArr[1][0]*tailleCase
    caseFinY = DepArr[1][1]*tailleCase
    caseFinZ= DepArr[1][2]*tailleCase
    caseFin =(caseFinX,caseFinY)

    print(DepArr)
    print(DepArr[0][0])
    print(DepArr[1])
    joueur.X = DepArr[0][0]
    joueur.Y = DepArr[0][1]
    joueur.Z = DepArr[0][2]
    print(joueur.X)
    print(joueur.Y)
    print(joueur.Z)

        #Position des ??clats

    #Place les ??clats de sorte ?? ce qu'ils ne soient pas sur le chemin de la sortie
#Eclat 1
    xS1 = randint(0,taille-1)
    yS1 = randint(0,taille-1)
    zS1 = randint(0,nbEtages)
    eclatChemin = pathFinding3D(dedale, (joueur.X, joueur.Y, joueur.Z),(xS1, yS1, zS1))
    
    while listeEstDansListe(eclatChemin, DepArr[2]):
            xS1 = randint(0,taille-1)
            yS1 = randint(0,taille-1)
            zS1 = randint(0,nbEtages)
            eclatChemin = pathFinding3D(dedale, (joueur.X, joueur.Y, joueur.Z),(xS1, yS1, zS1))

#Eclat 2
    xS2 = randint(0,taille-1)
    yS2 = randint(0,taille-1)
    zS2 = randint(0,nbEtages)
    eclatChemin = pathFinding3D(dedale, (joueur.X, joueur.Y, joueur.Z),(xS2, yS2, zS2))
    
    while listeEstDansListe(eclatChemin, DepArr[2]):
            xS2 = randint(0,taille-1)
            yS2 = randint(0,taille-1)
            zS2 = randint(0,nbEtages)
            eclatChemin = pathFinding3D(dedale, (joueur.X, joueur.Y, joueur.Z),(xS2, yS2, zS2))
            
#Eclat 3
    xS3 = randint(0,taille-1)
    yS3 = randint(0,taille-1)
    zS3 = randint(0,nbEtages)
    eclatChemin = pathFinding3D(dedale, (joueur.X, joueur.Y, joueur.Z),(xS3, yS3, zS3))
    
    while listeEstDansListe(eclatChemin, DepArr[2]):
            xS3 = randint(0,taille-1)
            yS3 = randint(0,taille-1)
            zS3 = randint(0,nbEtages)
            eclatChemin = pathFinding3D(dedale, (joueur.X, joueur.Y, joueur.Z),(xS3, yS3, zS3))

    Eclat = [(xS1,yS1,zS1),(xS2,yS2,zS2),(xS3,yS3,zS3)]

    quitter = False
    font2 = pygame.font.Font(None, 24)
    font3 = pygame.font.Font("Retro.ttf", 40)
    text = font2.render("Voici les commandes", 1, (255,255,255))
    cmd1 = font2.render("Utilisez les fl??ches directionnelles pour se d??placer",1,(255,255,255))
    cmd2 = font2.render("Utilisez H pour monter d'un ??tage lorsque vous ??tes sur une ??chelle montante", 1, (255,255,255))
    cmd3 = font2.render("Utilisez L pour descendre d'un ??tage lorsque vous ??tes sur une ??chelle descendante", 1, (255,255,255))
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
                    affiche_fin = False

                if event.type == timer_event: #Si l'event se d??roule, alors ....
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

                    
        screen.fill(black)

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

        # (2 IFs dessous) Traitement du mouvement fluide du personnage
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
                        joueur.afficherSprite(screen, 3, joueur.spriteX*tailleCase, joueur.spriteY*tailleCase)
                        #screen.blit(joueur.sprite_idle_3 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))
                else:
                        joueur.afficherSprite(screen, 1, joueur.spriteX*tailleCase, joueur.spriteY*tailleCase)
                        #screen.blit(joueur.sprite_idle_1 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))
                        
        else:
                if joueur.regardeGauche:
                        joueur.afficherSprite(screen, 4, joueur.spriteX*tailleCase, joueur.spriteY*tailleCase)
                        #screen.blit(joueur.sprite_idle_4 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))
                else:
                        joueur.afficherSprite(screen, 2, joueur.spriteX*tailleCase, joueur.spriteY*tailleCase)
                        #screen.blit(joueur.sprite_idle_2 , (joueur.spriteX*tailleCase, joueur.spriteY*tailleCase))

                if spriteCycle > spriteCyclePeriod:
                        spriteCycle = 0
               
        spriteCycle = spriteCycle + 1

        yTexte = tailleCase * taille
        screen.blit(myfont.render(str(shard_amount),1,(255,0,0)),(250,yTexte + 120))
        screen.blit(myfont.render(" ??clat(s)",1,(255,0,0)),(260,yTexte + 120))
        screen.blit(myfont.render("Vous ??tes actuellement ?? l'??tage n??",1,(255,0,0)),(50,yTexte+140))
        screen.blit(myfont.render(str(joueur.Z),1,(255,0,0)),(365,yTexte+140))
        screen.blit(myfont.render(" du labyrinthe",1,(255,0,0)),(375,yTexte+140))

        if shard_amount == 3:
                screen.blit(font2.render("Tous les cristaux ont ??t??s ramass??s, dirigez vous vers la sortie",1,white),(20,yTexte+200))
                

        screen.blit(text, (0,yTexte))
        screen.blit(cmd1, (20,yTexte+30))
        screen.blit(cmd2, (20,yTexte+60))
        screen.blit(cmd3, (20,yTexte+90))
        pygame.display.update()


    if affiche_fin :

            score = score - NbDeplacements -  counter
            screen.fill(black)
            screen.blit(font3.render("Vous avez obtenu un score de ", 1,white),(50,100))
            screen.blit(font3.render(str(score), 1,white),(475,100))
            screen.blit(font3.render(" points", 1,white),(550,100))
            screen.blit(font3.render("Vous avez effectu??s  ", 1,white),(50,200))
            screen.blit(font3.render(str(NbDeplacements), 1,white),(375,200))
            screen.blit(font3.render(" d??placements", 1,white),(430,200))
            screen.blit(font3.render("Vous avez mit ", 1,white),(50,300))
            screen.blit(font3.render(str(counter), 1,white),(300,300))
            screen.blit(font3.render(" secondes pour sortir", 1,white),(350,300))
            fileR = open("highscore.txt")
            lignesR = fileR.read().splitlines()
            HscoreR = int(lignes[-1])
            fileR.close()
            if score > HscoreR :
                    screen.blit(font3.render("F??licitations ! Nouveau Highscore !",1,white),(100,400))
            


            pygame.display.update()
            lastScore = score

            counter_fin = 10
            run = True
            while run and not quitter:
                    clock.tick(60)
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    run = False
                            elif event.type == timer_event: #Si l'event se d??roule, alors ....
                                    counter_fin -= 1
                                    print(counter_fin)
                                    if counter_fin == 0: #si le compteur arrive ?? 0, alors ...
                                            pygame.time.set_timer(timer_event, 0)
                                            run = False

    pygame.quit()


for i in range(3,7):
        main(i)



