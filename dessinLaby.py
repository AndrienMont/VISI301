import pygame

def dessineDedale (origine_xF1, origine_yF1, tailleCaseF1, mazeF1, longF1, largF1, screenF1):
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
    for i in range(0,longF1):
        for j in range(0,largF1):
            if mazeF1[i][j]["wallLeft"]:
                
                Start_left = (i*tailleCaseF1, origine_yF1+(j*tailleCaseF1)) 
                End_left = (i*tailleCaseF1, origine_yF1+(j*tailleCaseF1)+tailleCaseF1)
                pygame.draw.line(screenF1, (166,15,64), Start_left, End_left, 2)
            if mazeF1[i][j]["wallUp"]:
                Start_up = (origine_xF1+(i*tailleCaseF1),j*tailleCaseF1)
                End_up = (origine_xF1+(i*tailleCaseF1)+tailleCaseF1,j*tailleCaseF1)
                pygame.draw.line(screenF1, (166,15,64), Start_up, End_up,2)
            
    End_vertical = (origine_xF1, largF1 * tailleCaseF1)
    End_horizontal = (longF1 * tailleCaseF1, origine_yF1)
    End_vertic_horiz = (longF1 * tailleCaseF1, largF1 * tailleCaseF1)
    pygame.draw.line(screenF1,(166,15,64),End_vertical, End_vertic_horiz,2)
    pygame.draw.line(screenF1,(166,15,64), End_horizontal,End_vertic_horiz,2)