import pygame
import random
import pathFinding as path
import labyrinthe as laby
from pathFinding3D import*
from labyrinthe3DPrototype import*


def affiche_case_V2(x_F2, y_F2, origine_xF2, origine_yF2, tailleCase_F2, maze_F2, screen_F2):
    posX = origine_xF2 + tailleCase_F2*x_F2
    posY = origine_yF2 + tailleCase_F2*y_F2

    tileTextureIndex = 0
    if laby.yAMur(maze_F2, x_F2, y_F2, "up"):
        tileTextureIndex = tileTextureIndex + 1

    if laby.yAMur(maze_F2, x_F2, y_F2, "left"):
        tileTextureIndex = tileTextureIndex + 2

    if laby.yAMur(maze_F2, x_F2, y_F2, "down"):
        tileTextureIndex = tileTextureIndex + 4

    if laby.yAMur(maze_F2, x_F2, y_F2, "right"):
        tileTextureIndex = tileTextureIndex + 8
    
    if not laby.yAMur(maze_F2, x_F2, y_F2, "low") or not laby.yAMur(maze_F2, x_F2, y_F2, "high"):
        

        if laby.yAMur(maze_F2, x_F2, y_F2, "high"):
            fileName = "ladders/ladderDown.png"

        if laby.yAMur(maze_F2, x_F2, y_F2, "high"):
            fileName = "ladders/ladderUp.png"
            
    if laby.yAMur(maze_F2, x_F2, y_F2, "low") and laby.yAMur(maze_F2, x_F2, y_F2, "high"):
        fileName = "ladders/ladderBoth.png"
        
        

    fileName = "mazetexture/"+str(tileTextureIndex) + ".png"
    tile = pygame.image.load(fileName)
    tile = pygame.transform.scale(tile, (tailleCase_F2, tailleCase_F2))
    screen_F2.blit(tile, (posX, posY))
            



def dessineDedale (origine_xF1, origine_yF1, tailleCaseF1, mazeF1, screenF1,posX,posY):
    """Dessine un labyrinthe dans une fenêtre pygame

        IN
            origine_xF1 : abscisse du début du labyrinthe dans la fenêtre | int
            origine_yF1 : ordonnée du début du labyrinthe dans la fenêtre | int
            tailleCaseF1 : taille des cases du labyrinthe | int
            mazeF1 : tableau de tableau de dictionnaire de deux booléens | labyrinthe généré
            screenF1 : écran où dessiner le labyrinthe | display pygame

        OUT
            Lignes sur la fenêtre pygame
        """
    largF1 = len(mazeF1)
    longF1 = len(mazeF1[0])
    
    for i in range(len(mazeF1[0])):
        for j in range(len(mazeF1)):
            if mazeF1[i][j]["wallLeft"]:
                
                Start_left = (origine_xF1+i*tailleCaseF1, origine_yF1+(j*tailleCaseF1)) 
                End_left = (origine_xF1+i*tailleCaseF1, origine_yF1+(j*tailleCaseF1)+tailleCaseF1)
                pygame.draw.line(screenF1, (166,15,64), Start_left, End_left, 2)
            if mazeF1[i][j]["wallUp"]:
                Start_up = (origine_xF1+(i*tailleCaseF1),origine_yF1+j*tailleCaseF1)
                End_up = (origine_xF1+(i*tailleCaseF1)+tailleCaseF1,origine_yF1+j*tailleCaseF1)
                pygame.draw.line(screenF1, (166,15,64), Start_up, End_up,2)
            
    End_vertical = (origine_xF1,origine_yF1+ largF1 * tailleCaseF1)
    End_horizontal = (origine_xF1+longF1 * tailleCaseF1, origine_yF1)
    End_vertic_horiz = (origine_xF1+longF1 * tailleCaseF1,origine_yF1+ largF1 * tailleCaseF1)
    pygame.draw.line(screenF1,(166,15,64),End_vertical, End_vertic_horiz,2)
    pygame.draw.line(screenF1,(166,15,64), End_horizontal,End_vertic_horiz,2)







def affiche_case(origine_xF2,origine_yF2,tailleCaseF2,mazeF2,screenF2,posX,posY):

    #meme principe que la fonction dessinDedale mais affiche seulement une case

    longF2 = len(mazeF2[0])
    largF2 = len(mazeF2)
    
    if mazeF2[posX][posY]["wallLeft"]: #Affiche le mur de gauche
        
        Start_left = (origine_xF2+posX*tailleCaseF2, origine_yF2+(posY*tailleCaseF2)) 
        End_left = (origine_xF2+posX*tailleCaseF2, origine_yF2+(posY*tailleCaseF2)+tailleCaseF2)
        pygame.draw.line(screenF2, (166,15,64), Start_left, End_left, 2)


    if mazeF2[posX][posY]["wallUp"]: #Affiche le mur du dessus
        
        Start_up = (origine_xF2+(posX*tailleCaseF2),origine_yF2+posY*tailleCaseF2)
        End_up = (origine_xF2+(posX*tailleCaseF2)+tailleCaseF2,origine_yF2+posY*tailleCaseF2)
        pygame.draw.line(screenF2, (166,15,64), Start_up, End_up,2)
        

    if posY+1 < len(mazeF2):
        if mazeF2[posX][posY+1]["wallUp"]: #Affiche le mur du dessous
        
            Start_up = (origine_xF2+(posX*tailleCaseF2),origine_yF2+(posY*tailleCaseF2)+tailleCaseF2)
            End_up = (origine_xF2+(posX*tailleCaseF2)+tailleCaseF2,origine_yF2+(posY*tailleCaseF2)+tailleCaseF2)
            pygame.draw.line(screenF2, (166,15,64), Start_up, End_up,2)

    if posX+1 < len(mazeF2):
        if mazeF2[posX+1][posY]["wallLeft"]: #Affiche le mur de droite
        
            Start_left = (origine_xF2+(posX*tailleCaseF2)+tailleCaseF2, origine_yF2+(posY*tailleCaseF2)) 
            End_left = (origine_xF2+(posX*tailleCaseF2)+tailleCaseF2, origine_yF2+(posY*tailleCaseF2)+tailleCaseF2)
            pygame.draw.line(screenF2, (166,15,64), Start_left, End_left, 2)

        
            
    End_vertical = (origine_xF2,origine_yF2+ largF2 * tailleCaseF2)
    End_horizontal = (origine_xF2+longF2 * tailleCaseF2, origine_yF2)
    End_vertic_horiz = (origine_xF2+longF2 * tailleCaseF2,origine_yF2+ largF2 * tailleCaseF2)
    pygame.draw.line(screenF2,(166,15,64),End_vertical, End_vertic_horiz,2)
    pygame.draw.line(screenF2,(166,15,64), End_horizontal,End_vertic_horiz,2)


def randDepArr(posXminF1, posYminF1, tailleCaseF3, mazeF3):
    """Permet de générer un départ et une arrivée aléatoire dans un labyrinthe et les regénère en cas de nécessité

    IN

    posXminF1, posYminF1: integer | coordonnées des points extrêmes du labyrinthe
    tailleCaseF3 : integer | taille des cases sur l'affichage du labyrinthe
    mazeF3 : tableau de tableaux de dictionnaires | labyrinthe

    OUT

    Deux tuples, correspondant à la case de départ et d'arrivée"""


    largF3 = len(mazeF3)
    longF3 = len(mazeF3[0])
    
    posXmax = posXminF1 + longF3 -1
    posYmax = posYminF1 + largF3 -1
    
    nbDepArr = 0

    while (nbDepArr < (largF3*longF3*0.4)) :
        
        xDep = random.randint(posXminF1,posXmax)
        yDep = random.randint(posYminF1,posXmax)
        xArr = random.randint(posXminF1,posXmax)
        yArr = random.randint(posYminF1,posYmax)
        DepHyp = (xDep,yDep)
        ArrHyp = (xArr,yArr)

        DepArr = path.pathFinding(mazeF3,DepHyp,ArrHyp)
        nbDepArr = len(DepArr)

    return DepHyp,ArrHyp
    





def randDepArr3D(posXminF1, posYminF1,nbEtages, tailleCaseF3, mazeF3):
    """Permet de générer un départ et une arrivée aléatoire dans un labyrinthe et les regénère en cas de nécessité

    IN

    posXminF1, posYminF1: integer | coordonnées des points extrêmes du labyrinthe
    tailleCaseF3 : integer | taille des cases sur l'affichage du labyrinthe
    mazeF3 : tableau de tableaux de dictionnaires | labyrinthe

    OUT

    Deux tuples, correspondant à la case de départ et d'arrivée"""


    largF3 = len(mazeF3)
    longF3 = len(mazeF3[0])
    
    posXmax = posXminF1 + longF3 -1
    posYmax = posYminF1 + largF3 -1
    posZminF1 = 0
    posZmax = nbEtages
    
    nbDepArr = 0

    while (nbDepArr < (largF3*longF3*nbEtages*0.4)) :
        
        xDep = random.randint(posXminF1,posXmax)
        yDep = random.randint(posYminF1,posXmax)
        zDep = random.randint(posZminF1,posZmax)
        xArr = random.randint(posXminF1,posXmax)
        yArr = random.randint(posYminF1,posYmax)
        zArr = random.randint(posZminF1,posZmax)
        DepHyp = (xDep,yDep,zDep)
        ArrHyp = (xArr,yArr,zArr)

        DepArr = pathFinding3D(mazeF3,DepHyp,ArrHyp)
        nbDepArr = len(DepArr)

    return DepHyp,ArrHyp




def affiche_case_V2_3D(x_F2, y_F2,z_F2, origine_xF2, origine_yF2, tailleCase_F2, maze_F2, screen_F2):
    posX = origine_xF2 + tailleCase_F2*x_F2
    posY = origine_yF2 + tailleCase_F2*y_F2

    tileTextureIndex = 0
    fileName2 = ""
    
    if yAMur(maze_F2, x_F2, y_F2, z_F2,  "up"):
        tileTextureIndex = tileTextureIndex + 1

    if yAMur(maze_F2, x_F2, y_F2,z_F2, "left"):
        tileTextureIndex = tileTextureIndex + 2

    if yAMur(maze_F2, x_F2, y_F2, z_F2,  "down"):
        tileTextureIndex = tileTextureIndex + 4

    if yAMur(maze_F2, x_F2, y_F2, z_F2, "right"):
        tileTextureIndex = tileTextureIndex + 8


    fileName = "mazetexture/"+str(tileTextureIndex) + ".png"
    tile = pygame.image.load(fileName)
    tile = pygame.transform.scale(tile, (tailleCase_F2, tailleCase_F2))
    screen_F2.blit(tile, (posX, posY))


    if not yAMur(maze_F2, x_F2, y_F2,z_F2, "low") or not yAMur(maze_F2, x_F2, y_F2,z_F2,"high"):

        if yAMur(maze_F2, x_F2, y_F2,z_F2,"high"):
            tile2 = pygame.image.load("ladders/ladderDown.png")
            tile2 = pygame.transform.scale(tile2, (tailleCase_F2, tailleCase_F2))
            screen_F2.blit(tile2, (posX, posY))

        if yAMur(maze_F2, x_F2, y_F2,z_F2,"low"):
            tile2 = pygame.image.load("ladders/ladderUp.png")
            tile2 = pygame.transform.scale(tile2, (tailleCase_F2, tailleCase_F2))
            screen_F2.blit(tile2, (posX, posY))

        




