import pygame

def dessineDedale (origine_xF1, origine_yF1, tailleCaseF1, mazeF1, longF1, largF1, screenF1,posX,posY):
    """Dessine un labyrinthe dans une fenêtre pygame

        IN
            origine_xF1 : abscisse du début du labyrinthe dans la fenêtre | int
            origine_yF1 : ordonnée du début du labyrinthe dans la fenêtre | int
            tailleCaseF1 : taille des cases du labyrinthe | int
            mazeF1 : tableau de tableau de dictionnaire de deux booléens | labyrinthe généré
            longF1 : longueur du labyrinthe généré | int
            largF1 : largeur du labyrinthe généré | int
            screenF1 : écran où dessiner le labyrinthe | display pygame

        OUT
            Lignes sur la fenêtre pygame
        """
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







def affiche_case(origine_xF2,origine_yF2,tailleCaseF2,mazeF2,longF2,largF2,screenF2,posX,posY):

    #meme principe que la fonction dessinDedale mais affiche seulement une case

    
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

