#EXPLICATION DE L'ALGORITHME

#   Crée un tableau V de vecteurs de la taille du labyrinthe
#   Crée une liste T de cases que l'on va traiter
#   Ajoute la case de fin à la liste T

#   Tant que la case départ n'est pas atteinte
#       Créer une liste newT
#       Pour toutes les cases dans la liste T
#           Attribuer aux cases à gauche, à droite, en haut et en bas un vecteur dans V qui pointe vers la case courante
#           Illustration :
#                 (0,1)
#      (1,0) (case Courante) (-1, 0)
#                 (0,-1)
#           Ajouter les cases à gauche, à droite, en haut et en bas à newT
#       Définir T comme newT, Ceci donne les cases à traiter à la prochaine itération

#   Une fois que l'on a trouvé la case départ
#   On crée un tableau Res

#   En commençant par la case départ, on lui ajoute le vecteur de V de la case courante et on enregistre la nouvelle case dans Res
#   Illustration :
#       case courante : (5,3)
#       vecteur sur la case courante : V[5][3] = (1,0)

#       case courante := case courante + vecteur sur la case courante = (5,3) + (1,0) = (6,3)

#   Répéter jusqu'à ce que l'on trouve la case de fin

#   Retourner Res

import labyrinthe as laby

def pathFinding(maze, start, end):
    """Détermine le chemin le plus court entre un départ et une arrivée dans un labyrinthe
    
    IN
        maze : labyrinthe 2D | labyrinthe environnement
        start : Tuple de 2 int | case départ
        end : Tuple de 2 int | case arrivée
        
    OUT
        Tableau de Tuple de 2 int
    
    """

    mazeVectors = [[(0,0) for i in range(0, len(maze[0]))] for i in range(0, len(maze))]
    activeTiles = [end]
    trouve = False

    while not trouve:
        for tile in activeTiles:
            if tile == start:
                trouve = True

        
        newActiveTiles = []
        for tile in activeTiles:
            x = tile[0]
            y = tile[1]
            if not laby.yAMur(maze, x, y, "left"):
                if not (mazeVectors[x-1][y] != (0,0) or mazeVectors[x-1][y] == end):
                    mazeVectors[x-1][y] = (1,0)
                    newActiveTiles.append((x-1, y))
            if not laby.yAMur(maze, x, y, "right"):
                if not (mazeVectors[x+1][y] != (0,0) or mazeVectors[x+1][y] == end):
                    mazeVectors[x+1][y] = (-1,0)
                    newActiveTiles.append((x+1, y))
            if not laby.yAMur(maze, x, y, "up"):
                if not (mazeVectors[x][y-1] != (0,0) or mazeVectors[x][y-1] == end):
                    mazeVectors[x][y-1] = (0,1)
                    newActiveTiles.append((x, y-1))
            if not laby.yAMur(maze, x, y, "down"):
                if not (mazeVectors[x][y+1] != (0,0) or mazeVectors[x][y+1] == end):
                    mazeVectors[x][y+1] = (0,-1)
                    newActiveTiles.append((x, y+1))
        activeTiles = newActiveTiles

    res = []
    currentTile = start
    while currentTile != end:
        res.append(currentTile)
        
        x = currentTile[0]
        y = currentTile[1]
        currentTile = (x + mazeVectors[x][y][0], y + mazeVectors[x][y][1])
    res.append(end)
    del res[0]
    
    return res
